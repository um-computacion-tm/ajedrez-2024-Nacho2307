from Juego.Piezas.Piece import Piece

class Knight(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, 'Knight', x, y)

    def movimiento_correcto(self, desde_fila, desde_columna, hasta_fila, hasta_columna, board=None):
            fila_diff = abs(hasta_fila - desde_fila)
            columna_diff = abs(hasta_columna - desde_columna)
            return (fila_diff == 2 and columna_diff == 1) or (fila_diff == 1 and columna_diff == 2)
