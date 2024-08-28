from Juego.Piezas.Rook import Rook
from Juego.Piezas.Knight import Knight
from Juego.Piezas.King import King
from Juego.Piezas.Bishop import Bishop
from Juego.Piezas.Pawn import Pawn
from Juego.Piezas.Queen import Queen

class Board:
    def __init__(self):
        self.__positions__ = []
        # Inicializa un tablero de ajedrez vacío de 8x8
        for _ in range(8):
            col = [None] * 8
            self.__positions__.append(col)

        # Configura las piezas en sus posiciones iniciales
        self.__positions__[0] = [
            Rook("Black"), Knight("Black"), Bishop("Black"), Queen("Black"),
            King("Black"), Bishop("Black"), Knight("Black"), Rook("Black")
        ]
        self.__positions__[1] = [Pawn("Black")] * 8
        self.__positions__[6] = [Pawn("White")] * 8
        self.__positions__[7] = [
            Rook("White"), Knight("White"), Bishop("White"), Queen("White"),
            King("White"), Bishop("White"), Knight("White"), Rook("White")
        ]

    def __str__(self):
        # Retorna una representación en texto del tablero
        resultado = ""
        for row in self.__positions__:
            fila_texto = [str(piece) if piece else "." for piece in row]
            resultado += " ".join(fila_texto) + "\n"
        return resultado

    def mostrar_coords(self):
        # Muestra el tablero con coordenadas para referencia
        mostrar = "  0 1 2 3 4 5 6 7\n"
        for i, row in enumerate(self.__positions__):
            fila = f"{i} " + " ".join([piece.__str__() if piece else '.' for piece in row]) + "\n"
            mostrar += fila
        return mostrar

    def _check_bounds(self, row, col):
        # Verifica si las coordenadas están dentro del rango válido del tablero
        if 0 <= row < 8 and 0 <= col < 8:
            return True
        else:
            raise IndexError("Posición fuera del tablero.")

    def get_piece(self, row, col):
        # Devuelve la pieza en la posición (row, col) si está dentro del tablero
        self._check_bounds(row, col)
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        # Coloca una pieza en la posición (row, col) si está dentro del tablero
        self._check_bounds(row, col)
        self.__positions__[row][col] = piece

if __name__ == "__main__":
    board = Board()
    print(board.mostrar_coords())
