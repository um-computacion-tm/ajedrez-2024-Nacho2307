import copy
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
        self.__positions__ = [[None] * 8 for _ in range(8)]

    def place_piece(self, piece, position):
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
        return mostrar

    def _check_bounds(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return True
        else:
            raise IndexError("Posición fuera del tablero.")

    def get_piece(self, row, col):
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        self._check_bounds(row, col)
        self.__positions__[row][col] = piece

    def get_pieces(self):
        pieces = []
        for row in self.__positions__:
            for piece in row:
                if piece:
                    pieces.append(piece)
        return pieces

    def pieces_on_board(self):
        white_pieces = 0
        black_pieces = 0
        for row in self.__positions__:
            for piece in row:
                if piece:
                    if piece.get_color().lower() == 'white':
                        white_pieces += 1
                    elif piece.get_color().lower() == 'black':
                        black_pieces += 1
        return white_pieces, black_pieces

    def is_valid_move(self, piece, from_pos, to_pos):
        return piece.movimiento_correcto(from_pos[0], from_pos[1], to_pos[0], to_pos[1], self)
