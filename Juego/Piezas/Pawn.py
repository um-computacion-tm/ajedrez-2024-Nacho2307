from Piezas.Piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, "Pawn", "♙" if color == "Black" else "♟")

    def movimiento_correcto(self, from_row, from_col, to_row, to_col):
        direccion = -1 if self.color == "Black" else 1
        
        # Movimiento simple
        if from_col == to_col:
            if to_row == from_row + direccion:
               return True
           
           # Movimiento de dos casillas inicial
            if (self.__color__ == "Black" and from_row == 6 or self.__color__ == "White" and from_row == 1) and to_row + 2 * direccion:
               return True
        
        # Captura Diagonal
        if abs(from_col - to_col) == 1 and to_row == from_row + direccion:
            return True
        return False