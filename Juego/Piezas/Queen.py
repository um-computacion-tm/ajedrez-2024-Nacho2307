from Juego.Piezas.Piece import Piece
from Juego.Piezas.Bishop import Bishop
from Juego.Piezas.Rook import Rook

class Queen(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, 'Queen', x, y)
        self.__bishop_moves__ = Bishop(color)
        self.__rook_moves__ = Rook(color)
    
    def movimiento_correcto(self, from_row, from_col, to_row, to_col, board=None):
    # La reina puede moverse como un alfil o como una torre
     bishop_correct = self.__bishop_moves__.movimiento_correcto(from_row, from_col, to_row, to_col, board)
     rook_correct = self.__rook_moves__.movimiento_correcto((from_row, from_col), (to_row, to_col), board)
     return bishop_correct or rook_correct
