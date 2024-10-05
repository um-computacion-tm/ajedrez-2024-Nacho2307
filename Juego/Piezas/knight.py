from Juego.Piezas.piece import Piece

class Knight(Piece):
    """
    Clase que representa un caballo en el juego de ajedrez.

    Atributos:
        color: Color de la pieza ('white' o 'black').
        x: Coordenada en el eje X (fila).
        y: Coordenada en el eje Y (columna).
    """

    def __init__(self, color, x=0, y=0):
        """Inicializa el caballo con su color y posición en el tablero."""
        super().__init__(color, 'Knight', x, y)

    def __movimiento_correcto__(self, desde_fila, desde_columna, hasta_fila, hasta_columna, board=None):
        """Verifica si el movimiento del caballo es válido."""
        fila_diff = abs(hasta_fila - desde_fila)
        columna_diff = abs(hasta_columna - desde_columna)

        # Comprobar las diferencias en filas y columnas para el movimiento en forma de L
        if (fila_diff == 2 and columna_diff == 1) or (fila_diff == 1 and columna_diff == 2):
            if board:
                destino = board.__positions__[hasta_fila][hasta_columna]
                if destino is not None:
                    # Verificar si el destino tiene una pieza del mismo color
                    if destino.__get_color__() == self.__get_color__():
                        return False  # Movimiento bloqueado por pieza del mismo color
                    return True  # Movimiento válido (captura)
                return True  # Movimiento válido si el destino está vacío
        return False  # Movimiento inválido
