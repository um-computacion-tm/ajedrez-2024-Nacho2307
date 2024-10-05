from Juego.Piezas.piece import Piece
from Juego.Piezas.bishop import Bishop
from Juego.Piezas.rook import Rook

class Queen(Piece):
    """
    Clase que representa una reina en el juego de ajedrez.

    Atributos:
        color: Color de la pieza ('white' o 'black').
        __bishop_moves__: Instancia de Bishop para validar movimientos diagonales.
        __rook_moves__: Instancia de Rook para validar movimientos rectos.
    """
    
    def __init__(self, color, x=0, y=0):
        """Inicializa la reina con su color y posición en el tablero."""
        super().__init__(color, 'Queen', x, y)
        self.__bishop_moves__ = Bishop(color)  # Movimiento como un alfil
        self.__rook_moves__ = Rook(color)      # Movimiento como una torre

    def __movimiento_correcto__(self, from_row, from_col, to_row, to_col, board=None):
        """Verifica si el movimiento de la reina es válido."""
        destino = board.__positions__[to_row][to_col]
        
        if self.__misma_pieza_en_destino__(destino):
            return False  # No puede moverse a una casilla ocupada por una pieza del mismo color
        
        # Validar movimientos de torre y alfil
        movimiento_rook = self.__rook_moves__.__movimiento_correcto__(from_row, from_col, to_row, to_col, board)
        movimiento_bishop = self.__bishop_moves__.__movimiento_correcto__(from_row, from_col, to_row, to_col, board)
        
        # La reina puede moverse como torre o alfil
        return movimiento_rook or movimiento_bishop
