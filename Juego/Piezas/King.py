from Juego.Piezas.Piece import Piece
from Juego.Exception import *

class King(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color.lower(), 'King', x, y)
        self.__simbolo__ = self.SYMBOLS['King'][self.__color__]

    def movimiento_correcto(self, from_row, from_col, to_row, to_col, board):
        # El rey se puede mover una casilla en cualquier dirección
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        if row_diff <= 1 and col_diff <= 1:
            pieza_destino = board.get_piece(to_row, to_col)
            # Verifica que la casilla destino no contenga una pieza del mismo color
            if pieza_destino is None or pieza_destino.get_color() != self.get_color():
                return True
        return False

    def mover(self, x, y):
        if abs(x - self.__x__) <= 1 and abs(y - self.__y__) <= 1:
            self.__x__ = x
            self.__y__ = y
        else:
            raise InvalidMoveException("Movimiento no válido para el rey.")

    def get_position(self):
        return (self.__x__, self.__y__)
