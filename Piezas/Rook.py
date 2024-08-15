from piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color, "Rook", "R")
    
# La torre puede moverse en horizontal o verticalmente
    def movimiento_correcto(self, from_row, from_col, to_row, to_col):
        if to_row == from_row or to_col == from_col:
            return True
        return False