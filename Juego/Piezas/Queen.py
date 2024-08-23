from Piezas.Piece import Piece
from Piezas.Bishop import Bishop
from Piezas.Rook import Rook

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color, "Queen", "♕" if color == "Black" else "♛")
        self.__bishop_moves__ = Bishop(color)
        self.___rook_moves__ = Rook(color)
    
    def movimiento_correcto(self, from_row, from_col, to_row, to_col):
        # La reina puede moverse como un alfil o como una torre
        return (self.__bishop_moves.movimiento_correcto(from_row, from_col, to_row, to_col) or
                self.__rook_moves.movimiento_correcto(from_row, from_col, to_row, to_col))