from .Piece import Piece


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color, "Bishop", "♗" if color == "Black" else "♝")
    
    # El Alfil se mueve en diagonal
    def movimiento_correcto(self, from_row, from_col, to_row, to_col):
        if from_row == to_row and from_col == to_col:
            return False
        # Verifica si es en diagonal el movimiento
        return abs(to_row - from_row) == abs(to_col - from_col)
    