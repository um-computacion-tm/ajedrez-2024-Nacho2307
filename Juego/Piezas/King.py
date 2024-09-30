from Juego.Piezas.Piece import Piece
from Juego.Exception import *

class King(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color.lower(), 'King', x, y)
        self.__simbolo__ = self.SYMBOLS['King'][self.__color__]

    def __movimiento_correcto__(self, desde_fila, desde_columna, hasta_fila, hasta_columna, board=None):
        fila_diff = abs(hasta_fila - desde_fila)
        columna_diff = abs(hasta_columna - desde_columna)
    
        # El rey se mueve solo una casilla en cualquier dirección
        if fila_diff <= 1 and columna_diff <= 1:
            destino = board.__get_piece__(hasta_fila, hasta_columna)
            if self.__misma_pieza_en_destino__(destino):
                return False  # No puede moverse a una casilla ocupada por una pieza del mismo color
            return True
        return False

    def __mover__(self, x, y):
        # Verifica que el movimiento esté dentro del rango permitido para el rey
        if abs(x - self.__x__) <= 1 and abs(y - self.__y__) <= 1:
            self.__x__ = x
            self.__y__ = y
        else:
            raise InvalidMoveException("Movimiento no válido para el rey.")

    def __get_position__(self):
        return (self.__x__, self.__y__)
