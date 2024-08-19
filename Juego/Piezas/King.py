from Piezas.Piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color, "King", "K")
        
    def mover(self, x, y):
        # Solo se puede moverse una casilla en cualquier direccion
        if abs(x - self.x) <= 1 and abs(y - self.y) <= 1:
            self.x = x
            self.y = y
        else:
            print("Movimiento incorrecto")
