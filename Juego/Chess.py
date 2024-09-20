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

            self.validate_turn(piece)

            if not self.__board__.is_valid_move(piece, from_pos, to_pos):
                raise InvalidMoveException("Movimiento no válido que deja al rey en jaque.")

            self.execute_move(from_pos, to_pos, piece)
            status = self.check_victory()

            if status != "No result":
                return status

            self.change_turn()
            return True

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
        self.__board__.set_piece(to_pos[0], to_pos[1], piece)
        self.__board__.remove_piece(from_pos[0], from_pos[1])

    def check_victory(self):
        pieces_alive = self.__board__.pieces_on_board()
        white_pieces, black_pieces = pieces_alive

        if white_pieces == 1 and black_pieces == 0:
            return "White wins"  # Aquí las blancas ganan
        elif black_pieces == 1 and white_pieces == 0:
            return "Black wins"  # Aquí las negras ganan
        elif white_pieces == 1 and black_pieces == 1:
            return "Draw"
        return "No result"

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
