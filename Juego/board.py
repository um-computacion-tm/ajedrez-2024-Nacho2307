from Juego.Piezas.Rook import Rook
from Juego.Piezas.Knight import Knight
from Juego.Piezas.King import King
from Juego.Piezas.Bishop import Bishop
from Juego.Piezas.Pawn import Pawn
from Juego.Piezas.Queen import Queen

class Board:
    def __init__(self):
        self.__positions__ = [[None] * 8 for _ in range(8)]
        self.setup_pieces()
        
    def setup_pieces(self):
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

    def clear_board(self):
    # Limpias el tablero con las piezas
     self.__positions__ = [[None] * 8 for _ in range(8)]
     
    def place_piece(self, piece, position):
        #Coloca una pieza en una posicion especifica en el tablero
        row, col = position
        self.__positions__[row][col] = piece
        
    def remove_piece(self, row, col):
        self._check_bounds(row, col)
        self.__positions__[row][col] = None
    
    def __str__(self):
        resultado = ""
        for row in self.__positions__:
            fila_texto = [str(piece) if piece else "." for piece in row]
            resultado += " ".join(fila_texto) + "\n"
        return resultado

    def mostrar_coords(self):
        mostrar = "  0 1 2 3 4 5 6 7\n"
        for i, row in enumerate(self.__positions__):
            fila = f"{i} " + " ".join([piece.__str__() if piece else '.' for piece in row]) + "\n"
            mostrar += fila
        print(mostrar)
        return mostrar

    def _check_bounds(self, row, col):
        # Verifica si las coordenadas están dentro del rango válido del tablero
        if 0 <= row < 8 and 0 <= col < 8:
            return True
        else:
            raise IndexError("Posición fuera del tablero.")

    def get_piece(self, row, col):
        pieza = self.__positions__[row][col]
        print(f"Obteniendo pieza en ({row}, {col}): {pieza}")
        return pieza

    def set_piece(self, row, col, piece):
        self._check_bounds(row, col)
        self.__positions__[row][col] = piece
        print(f"Pieza colocada en ({row}, {col}): {piece}")

if __name__ == "__main__":
    board = Board()
    print(board.mostrar_coords())
