from Juego.board import Board
from Juego.Exception import (
    InvalidMoveException,
    OutOfBoundsException,
    PieceAlreadyCapturedException,
    CheckException,
    CheckmateException,
    ColorException,
    TurnException
)
from Juego.Piezas.Piece import Piece

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(self, from_input, to_input):
        try:
            from_pos = self.parse_position(from_input)
            to_pos = self.parse_position(to_input)
            piece = self.get_piece_or_raise(from_pos)
            self.validate_turn(piece)
            self.execute_move(from_pos, to_pos, piece)
            status = self.check_victory()

            if status != True:
                return status
            self.change_turn()
            return True

        except (OutOfBoundsException, InvalidMoveException, PieceAlreadyCapturedException,
                ColorException, TurnException, ValueError) as e:
            print(f"Error: {str(e)}")
            raise

    def parse_position(self, input_str):
     try:
        row, col = map(int, input_str.split())
        row -= 1
        col -= 1

        if not (0 <= row <= 7 and 0 <= col <= 7):
            raise OutOfBoundsException(f"Position {input_str} esta fuera de los limites.")
        return (row, col)

     except ValueError:
        raise ValueError(f"Entrada inválida: {input_str}. Debe tener el formato 'fila columna', donde ambos valores están entre 1 y 8.")

    def get_piece_or_raise(self, pos):
        piece = self.__board__.get_piece(*pos)
        if piece is None:
            raise PieceAlreadyCapturedException(f'En la posicion {pos} no hay ninguna pieza.')
        return piece

    def validate_turn(self, piece):
        if piece.get_color().lower() != self.__turn__.lower():
            raise ColorException("No se puede mover una pieza de un color diferente.")

    def execute_move(self, from_pos, to_pos, piece):
        if not piece.chech_move(self.__board__, from_pos, to_pos):
            raise InvalidMoveException("Movimiento no válido para esta pieza.")
        
        self.__board__.set_piece(*to_pos, piece)
        self.__board__.set_piece(*from_pos, None)

    def check_victory(self):
        pieces_alive = self.__board__.pieces_on_board()
        if pieces_alive[0] > 1 and pieces_alive[1] < 2 and self.__turn__ == "BLACK":
            return "White wins"
        elif pieces_alive[1] > 1 and pieces_alive[0] < 2 and self.__turn__ == "WHITE":
            return "Black wins"
        elif pieces_alive[0] + pieces_alive[1] == 2:
            return "Draw"
        return True

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

    def print_board(self):
        self.__board__.print_board()
    
    def turn(self):
        return self.__turn__
    