from Juego.Piezas.Piece import Piece
from Juego.Piezas.Bishop import Bishop
from Juego.Piezas.Rook import Rook

class Queen(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, 'Queen', x, y)
        self.__bishop_moves__ = Bishop(color)
        self.__rook_moves__ = Rook(color)

    def __movimiento_correcto__(self, from_row, from_col, to_row, to_col, board=None):
        destino = board.__positions__[to_row][to_col]
        
        if self.__misma_pieza_en_destino__(destino):
            return False
        
        # Validar movimientos de torre y alfil
        movimiento_rook = self.__rook_moves__.__movimiento_correcto__(from_row, from_col, to_row, to_col, board)
        movimiento_bishop = self.__bishop_moves__.__movimiento_correcto__(from_row, from_col, to_row, to_col, board)
        
        # La reina puede moverse como torre o alfil
        return movimiento_rook or movimiento_bishop
