import redis 
import pickle
from Juego.Piezas.King import King
from Juego.Piezas.Piece import Piece
from Juego.board import Board
from Juego.Piezas.Bishop import Bishop
from Juego.Piezas.King import King
from Juego.Piezas.Knight import Knight
from Juego.Piezas.Pawn import Pawn
from Juego.Piezas.Queen import Queen
from Juego.Piezas.Rook import Rook
from Juego.Exception import (
    InvalidMoveException,
    OutOfBoundsException,
    PieceAlreadyCapturedException,
    ColorException,
    TurnException
)

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__scores__ = {"WHITE": 0, "BLACK": 0} # Inicializa el sistema de puntacion 
        self.redis_client = redis.Redis(host='redis', port=6379, db=0)

    # Método para sumar puntos al jugador
    def add_score(self, color, points):
        self.__scores__[color.upper()] += points

    def save_game(self, game_id):
        # Serializa el estado del tablero y el turno actual
        board_state = [[f"{piece.__class__.__name__}_{piece.get_color().lower()}" if piece else None for piece in row] for row in self.__board__.__positions__]
        game_state = {
            "board": board_state,
            "turn": self.__turn__
        }
        serialized_game = pickle.dumps(game_state)
        # Guarda el estado en Redis
        self.redis_client.set(game_id, serialized_game)
        print(f"Partida guardada con ID: {game_id}")

    def load_game(self, game_id):
        # Carga el estado del juego desde Redis
        serialized_game = self.redis_client.get(game_id)
        if serialized_game:
            game_state = pickle.loads(serialized_game)

            # Restaura el estado del tablero
            self.__board__.clear_board()  # Limpiar el tablero actual
            for i in range(8):
                for j in range(8):
                    piece_info = game_state["board"][i][j]
                    if piece_info:  # Si hay una pieza en la posición
                        piece_type, color = piece_info.split('_')  # Separar tipo y color
                        piece = None
                    
                        # Crear una nueva instancia de la pieza
                        if piece_type == "Pawn":
                            piece = Pawn(color.capitalize())
                        elif piece_type == "Rook":
                            piece = Rook(color.capitalize())
                        elif piece_type == "Knight":
                            piece = Knight(color.capitalize())
                        elif piece_type == "Bishop":
                            piece = Bishop(color.capitalize())
                        elif piece_type == "Queen":
                            piece = Queen(color.capitalize())
                        elif piece_type == "King":
                            piece = King(color.capitalize())
                    
                        # Verifica que la pieza no sea nula antes de colocarla
                        if piece:
                            self.__board__.place_piece(piece, (i, j))

            self.__turn__ = game_state["turn"]  # Restaura el turno
            print(f"Partida {game_id} cargada.")
        else:
            print(f"No se encontró ninguna partida con el ID: {game_id}")

    def get_board(self):
        return self.__board__

    def get_turn(self):
        return self.__turn__

    def print_board(self):
        print("  0 1 2 3 4 5 6 7")
        for i in range(8):
            fila = f"{i} " + " ".join(
                [str(self.__board__.get_piece(i, j)) if self.__board__.get_piece(i, j) else '.' for j in range(8)]
            )
            print(fila)

    def move(self, from_input, to_input):
        try:
            from_pos = self.parse_position(from_input)
            to_pos = self.parse_position(to_input)

            piece = self.get_piece_or_raise(from_pos)

            # Validar turno
            self.validate_turn(piece)

            # Verificar movimiento
            if not piece.movimiento_correcto(from_pos[0], from_pos[1], to_pos[0], to_pos[1], self.__board__):
                raise InvalidMoveException("Movimiento no válido para esta pieza.")

            # Ejecutar el movimiento
            status = self.execute_move(from_pos, to_pos, piece)

            # Imprime el tablero despues del movimiento
            self.print_board()

            # Cambiar el turno si no hay resultado de victoria
            if status is None:
                self.change_turn()
                return "Move successful"

            return status  # Retornar estado de victoria o empate

        except (OutOfBoundsException, InvalidMoveException, PieceAlreadyCapturedException, ColorException, TurnException, ValueError) as e:
            print(f"Error: {str(e)}")
            raise

    def parse_position(self, input_str):
        try:
            row, col = map(int, input_str.split())
            if not (0 <= row <= 7 and 0 <= col <= 7):
                raise OutOfBoundsException(f"Position {input_str} está fuera de los límites.")
            return (row, col)

        except ValueError:
            raise ValueError(f"Entrada inválida: {input_str}. Debe tener el formato 'fila columna', donde ambos valores están entre 1 y 8.")

    def get_piece_or_raise(self, pos):
        piece = self.__board__.get_piece(*pos)
        if piece is None:
            raise PieceAlreadyCapturedException(f'En la posición {pos} no hay ninguna pieza.')
        return piece

    def validate_turn(self, piece):
        if piece.get_color().lower() != self.__turn__.lower():
            raise ColorException("No se puede mover una pieza de un color diferente.")

    def execute_move(self, from_pos, to_pos, piece):
        # Mover la pieza y capturar si es necesario
        captured_piece = self.__board__.move_piece(from_pos, to_pos)

        # Si se captura una pieza
        if captured_piece:
            color = piece.get_color().capitalize()
            points = captured_piece.get_value()  # Obtener el valor de la pieza capturada
            self.add_score(color, points)  # Añadir puntos al jugador

        # Verificar si se captura el rey
        if captured_piece and isinstance(captured_piece, King):
            return f"{piece.get_color().capitalize()} wins"

        # Verificar el estado de victoria
        status = self.check_victory()
        if status != "No result":
            return status

        return None  # Retornar None si no hay estado de victoria

    # Método para mostrar las puntuaciones actuales
    def show_scores(self):
        print(f"Puntuación: Blanco: {self.__scores__['WHITE']}, Negro: {self.__scores__['BLACK']}")

    def check_victory(self):
        # Obtener las piezas blancas y negras que están en el tablero
        white_pieces, black_pieces = self.__board__.pieces_on_board()

        # Condiciones de victoria: Si no hay más piezas blancas o negras
        if white_pieces == 0:
            return "Black wins"
        if black_pieces == 0:
            return "White wins"

        # Verificación de que solo los reyes queden en el tablero
        white_king_alive = False
        black_king_alive = False

        for row in self.__board__.__positions__:
            for piece in row:
                if piece and piece.__nombre__.lower() == 'king':
                    if piece.get_color().lower() == 'white':
                        white_king_alive = True
                    elif piece.get_color().lower() == 'black':
                        black_king_alive = True

        # Empate si solo quedan los dos reyes
        if white_king_alive and black_king_alive and white_pieces == 1 and black_pieces == 1:
            return "Draw"

        return "No result"

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
