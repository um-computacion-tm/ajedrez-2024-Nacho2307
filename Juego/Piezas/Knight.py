from .Piece import Piece


class Knight(Piece):
    def __init__(self, color):
         super().__init__(color, "Caballo", "♞" if color == "negro" else "♘")
         
    def movimiento_correcto(self, desde_fila, desde_columna, hasta_fila, hasta_columna):
         fila_diff = abs(hasta_fila - desde_columna)
         columna_diff = abs(hasta_columna - desde_columna)
         return (fila_diff == 2 and columna_diff == 1) or (fila_diff == 1 and columna_diff == 2)
     