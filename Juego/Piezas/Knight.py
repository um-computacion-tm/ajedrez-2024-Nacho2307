from Juego.Piezas.Piece import Piece

class Knight(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, 'Knight', x, y)

    def movimiento_correcto(self, desde_fila, desde_columna, hasta_fila, hasta_columna, board=None):
        fila_diff = abs(hasta_fila - desde_fila)
        columna_diff = abs(hasta_columna - desde_columna)

        print(f"Comprobando movimiento desde ({desde_fila}, {desde_columna}) a ({hasta_fila}, {hasta_columna})")

        if (fila_diff == 2 and columna_diff == 1) or (fila_diff == 1 and columna_diff == 2):
            if board:
                destino = board.__positions__[hasta_fila][hasta_columna]
                print(f"Destino: {destino}")
                if destino is not None:
                    print(f"Color de destino: {destino.get_color()}, Color del caballo: {self.get_color()}")
                    if destino.get_color() == self.get_color():
                        return False  # Movimiento bloqueado por pieza del mismo color
                    return True  # Movimiento válido (captura)
                return True  # Movimiento válido si el destino está vacío
        return False  # Movimiento inválido
