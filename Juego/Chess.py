import copy
from Juego.board import Board
from Juego.Exception import (
    InvalidMoveException,
    OutOfBoundsException,
    PieceAlreadyCapturedException,
    ColorException,
    TurnException
)
from Juego.Piezas.King import King
from Juego.Piezas.Piece import Piece

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

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
        target_piece = self.__board__.get_piece(to_pos[0], to_pos[1])

        # Mover la pieza
        self.__board__.set_piece(to_pos[0], to_pos[1], piece)
        self.__board__.remove_piece(from_pos[0], from_pos[1])

        # Verificar si se captura el rey
        if target_piece and target_piece.__nombre__.lower() == "king":
            return f"{piece.get_color().capitalize()} wins"

        # Verificar el estado de victoria
        status = self.check_victory()
        if status != "No result":
            return status

        return None  # Retornar None si no hay estado de victoria

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
