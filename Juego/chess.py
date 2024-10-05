import os
import redis 
import pickle
from Juego.Piezas.king import King
from Juego.Piezas.piece import Piece
from Juego.board import Board
from Juego.Piezas.bishop import Bishop
from Juego.Piezas.king import King
from Juego.Piezas.knight import Knight
from Juego.Piezas.pawn import Pawn
from Juego.Piezas.queen import Queen
from Juego.Piezas.rook import Rook
from Juego.exception import (
    InvalidMoveException,
    OutOfBoundsException,
    PieceAlreadyCapturedException,
    ColorException,
    TurnException
)

class Chess:
    def __init__(self):
        # Inicializa el juego de ajedrez con un nuevo tablero y configura el estado inicial.
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__scores__ = {"WHITE": 0, "BLACK": 0}  # Inicializa el sistema de puntuación
        redis_host = os.getenv('REDIS_HOST', 'localhost')
        self.__redis_client__ = redis.Redis(host=redis_host, port=6379, db=0)

    def __add_score__(self, color, points):
        # Añade puntos al jugador del color especificado.
        self.__scores__[color.upper()] += points

    def __save_game__(self, game_id):
        # Guarda el estado actual del juego en la base de datos Redis.
        board_state = [[f"{piece.__class__.__name__}_{piece.__get_color__().lower()}" if piece else None for piece in row] 
                        for row in self.__board__.__positions__]
        game_state = {
            "board": board_state,
            "turn": self.__turn__
        }
        serialized_game = pickle.dumps(game_state)
        self.__redis_client__.set(game_id, serialized_game)
        print(f"Partida guardada con ID: {game_id}")

    def __load_game__(self, game_id):
        # Carga el estado del juego desde Redis y restaura el tablero y el turno.
        serialized_game = self.__redis_client__.get(game_id)
        if not serialized_game:
            return f"No se encontró ninguna partida con el ID: {game_id}" 

        game_state = pickle.loads(serialized_game)
        self.__restore_board__(game_state["board"])
        self.__turn__ = game_state["turn"]
        return f"Partida {game_id} cargada." 

    def __restore_board__(self, board_state):
        # Restaura el estado del tablero a partir del estado serializado.
        self.__board__.__clear_board__()
        for i in range(8):
            for j in range(8):
                piece_info = board_state[i][j]
                if piece_info:
                    piece = self.__create_piece__(piece_info)
                    if piece:
                        self.__board__.__place_piece__(piece, (i, j))

    def __create_piece__(self, piece_info):
        # Crea una pieza a partir de la información dada.
        piece_type, color = piece_info.split('_')
        piece_classes = {
            "Pawn": Pawn,
            "Rook": Rook,
            "Knight": Knight,
            "Bishop": Bishop,
            "Queen": Queen,
            "King": King
        }
        piece_class = piece_classes.get(piece_type)
        return piece_class(color.capitalize()) if piece_class else None

    def __get_board__(self):
        # Devuelve el estado actual del tablero.
        return self.__board__

    def __get_turn__(self):
        # Devuelve el turno actual del juego.
        return self.__turn__

    def __print_board__(self):
        # Imprime el tablero actual en la consola.
        print("  0 1 2 3 4 5 6 7")
        for i in range(8):
            fila = f"{i} " + " ".join(
                [str(self.__board__.__get_piece__(i, j)) if self.__board__.__get_piece__(i, j) else '.' for j in range(8)]
            )
            print(fila)

    def __move__(self, from_input, to_input):
        # Realiza un movimiento en el tablero.
        try:
            from_pos = self.__parse_position__(from_input)
            to_pos = self.__parse_position__(to_input)

            piece = self.__get_piece_or_raise__(from_pos)
            self.__validate_turn__(piece)

            if not piece.__movimiento_correcto__(from_pos[0], from_pos[1], to_pos[0], to_pos[1], self.__board__):
                raise InvalidMoveException("Movimiento no válido para esta pieza.")

            status = self.__execute_move__(from_pos, to_pos, piece)
            self.__print_board__()

            if status is None:
                self.__change_turn__()
                return "Move successful"

            return status

        except (OutOfBoundsException, InvalidMoveException, PieceAlreadyCapturedException, ColorException, TurnException, ValueError) as e:
            print(f"Error: {str(e)}")
            raise

    def __parse_position__(self, input_str):
        # Convierte una cadena de posición en coordenadas del tablero.
        try:
            row, col = map(int, input_str.split())
            if not (0 <= row <= 7 and 0 <= col <= 7):
                raise OutOfBoundsException(f"Position {input_str} está fuera de los límites.")
            return (row, col)

        except ValueError:
            raise ValueError(f"Entrada inválida: {input_str}. Debe tener el formato 'fila columna', donde ambos valores están entre 1 y 8.")

    def __get_piece_or_raise__(self, pos):
        # Obtiene una pieza de una posición o lanza una excepción si no hay pieza.
        piece = self.__board__.__get_piece__(*pos)
        if piece is None:
            raise PieceAlreadyCapturedException(f'En la posición {pos} no hay ninguna pieza.')
        return piece

    def __validate_turn__(self, piece):
        # Valida que el turno corresponda al color de la pieza que se desea mover.
        if piece.__get_color__().lower() != self.__turn__.lower():
            raise ColorException("No se puede mover una pieza de un color diferente.")

    def __execute_move__(self, from_pos, to_pos, piece):
        # Ejecuta el movimiento de una pieza a una posición final.
        captured_piece = self.__board__.__move_piece__(from_pos, to_pos)

        if captured_piece:
            color = piece.__get_color__().capitalize()
            points = captured_piece.__get_value__()  # Obtener el valor de la pieza capturada
            self.__add_score__(color, points)

        if captured_piece and isinstance(captured_piece, King):
            return f"{piece.__get_color__().capitalize()} wins"

        status = self.__check_victory__()
        if status != "No result":
            return status

        return None

    def __show_scores__(self):
        # Muestra las puntuaciones actuales de ambos jugadores.
        print(f"Puntuación: Blanco: {self.__scores__['WHITE']}, Negro: {self.__scores__['BLACK']}")

    def __check_victory__(self):
        #Verifica si alguno de los jugadores ha ganado o si hay empate.
        white_pieces, black_pieces = self.__board__.__pieces_on_board__()

        if white_pieces == 0:
            return "Black wins"
        if black_pieces == 0:
            return "White wins"

        white_king_alive = False
        black_king_alive = False

        for row in self.__board__.__positions__:
            for piece in row:
                if piece and piece.__nombre__.lower() == 'king':
                    if piece.__get_color__().lower() == 'white':
                        white_king_alive = True
                    elif piece.__get_color__().lower() == 'black':
                        black_king_alive = True

        if white_king_alive and black_king_alive and white_pieces == 1 and black_pieces == 1:
            return "Draw"

        return "No result"

    def __change_turn__(self):
        #Cambia el turno al siguiente jugador.
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
