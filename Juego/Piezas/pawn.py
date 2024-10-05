from Juego.Piezas.piece import Piece

class Pawn(Piece):
    """
    Clase que representa un peón en el juego de ajedrez.

    Atributos:
        color: Color de la pieza ('white' o 'black').
        x: Coordenada en el eje X (fila).
        y: Coordenada en el eje Y (columna).
    """

    def __init__(self, color, x=0, y=0):
        """Inicializa el peón con su color y posición en el tablero."""
        super().__init__(color, 'Pawn', x, y)

    def __movimiento_correcto__(self, from_row, from_col, to_row, to_col, board):
        """Verifica si el movimiento del peón es válido."""
        direccion = -1 if self.__get_color__() == "White" else 1
        destino = board.__get_piece__(to_row, to_col)

        # Verifica si hay una pieza del mismo color en el destino
        if self.__pieza_misma_color__(destino):
            return False  # Movimiento no permitido

        return (self.__movimiento_simple__(from_row, from_col, to_row, to_col, direccion, board) or
                self.__movimiento_doble_inicial__(from_row, from_col, to_row, to_col, direccion, board) or
                self.__captura_diagonal__(from_row, from_col, to_row, to_col, direccion, board))

    def __pieza_misma_color__(self, pieza_destino):
        """Verifica si la pieza en la posición de destino es del mismo color que el peón."""
        return pieza_destino is not None and pieza_destino.__get_color__() == self.__get_color__()

    def __movimiento_simple__(self, from_row, from_col, to_row, to_col, direccion, board):
        """Verifica un movimiento simple hacia adelante del peón."""
        return (from_col == to_col and 
                to_row == from_row + direccion and 
                board.__get_piece__(to_row, to_col) is None)

    def __movimiento_doble_inicial__(self, from_row, from_col, to_row, to_col, direccion, board):
        """Verifica si el peón puede realizar un movimiento doble inicial."""
        es_movimiento_valido = (
            (self.__get_color__() == "White" and from_row == 6) or 
            (self.__get_color__() == "Black" and from_row == 1)
        )
        return (es_movimiento_valido and 
                to_row == from_row + 2 * direccion and 
                board.__get_piece__(to_row, to_col) is None and 
                board.__get_piece__(from_row + direccion, from_col) is None)

    def __captura_diagonal__(self, from_row, from_col, to_row, to_col, direccion, board):
        """Verifica si el peón puede realizar una captura diagonal."""
        pieza_destino = board.__get_piece__(to_row, to_col)
        return (abs(from_col - to_col) == 1 and 
                to_row == from_row + direccion and 
                pieza_destino is not None and 
                pieza_destino.__get_color__() != self.__get_color__())
