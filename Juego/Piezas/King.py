from .Piece import Piece


class King(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, "King", "K")
        self.__x__ = x
        self.__y__ = y
        
        
    def mover(self, x, y):
        # Solo se puede moverse una casilla en cualquier direccion
        if abs(x - self.__x__) <= 1 and abs(y - self.__y__) <= 1:
            self.__x__ = x
            self.__y__ = y
        else:
            print("Movimiento incorrecto")
