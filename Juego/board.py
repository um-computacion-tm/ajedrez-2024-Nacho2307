from Juego.Piezas.rook import Rook
from Juego.Piezas.knight import Knight
from Juego.Piezas.king import King
from Juego.Piezas.bishop import Bishop
from Juego.Piezas.pawn import Pawn
from Juego.Piezas.queen import Queen

class Board:
    """
    Clase que representa el tablero de ajedrez.

    Atributos:
        __positions__: Lista 2D que contiene las posiciones de las piezas en el tablero.
    """

    def __init__(self):
        """Inicializa el tablero y coloca las piezas en sus posiciones iniciales."""
        self.__positions__ = [[None] * 8 for _ in range(8)]
        self.__setup_pieces__()

    def __setup_pieces__(self):
        """Coloca todas las piezas en el tablero en sus posiciones iniciales."""
        # Piezas negras
        self.__positions__[0] = [
            Rook("Black"), Knight("Black"), Bishop("Black"), Queen("Black"),
            King("Black"), Bishop("Black"), Knight("Black"), Rook("Black")
        ]
        self.__positions__[1] = [Pawn("Black") for _ in range(8)]  # Peones negros

        # Piezas blancas
        self.__positions__[6] = [Pawn("White") for _ in range(8)]  # Peones blancos
        self.__positions__[7] = [
            Rook("White"), Knight("White"), Bishop("White"), Queen("White"),
            King("White"), Bishop("White"), Knight("White"), Rook("White")
        ]

    def __clear_board__(self):
        """Limpia el tablero, removiendo todas las piezas."""
        self.__positions__ = [[None] * 8 for _ in range(8)]

    def __place_piece__(self, piece, position):
        """Coloca una pieza en una posición específica del tablero."""
        row, col = position
        self.__positions__[row][col] = piece

    def __remove_piece__(self, row, col):
        """Remueve una pieza de una posición específica del tablero."""
        self.__check_bounds__(row, col)
        self.__positions__[row][col] = None

    def __str__(self):
        """Retorna una representación en cadena del tablero."""
        resultado = ""
        for row in self.__positions__:
            fila_texto = [str(piece) if piece else "." for piece in row]
            resultado += " ".join(fila_texto) + "\n"
        return resultado

    def __mostrar_coords__(self):
        """Imprime las coordenadas del tablero para referencia visual."""
        mostrar = "  0 1 2 3 4 5 6 7\n"
        for i, row in enumerate(self.__positions__):
            fila = f"{i} " + " ".join([piece.__str__() if piece else '.' for piece in row]) + "\n"
            mostrar += fila
        return mostrar

    def __check_bounds__(self, row, col):
        """Verifica que las coordenadas estén dentro de los límites del tablero."""
        if 0 <= row < 8 and 0 <= col < 8:
            return True
        else:
            raise IndexError("Posición fuera del tablero.")

    def __move_piece__(self, from_pos, to_pos):
        """Mueve una pieza de una posición inicial a una posición final, capturando si es necesario."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        piece_to_move = self.__get_piece__(from_row, from_col)
        captured_piece = self.__get_piece__(to_row, to_col)

        self.__set_piece__(to_row, to_col, piece_to_move)
        self.__remove_piece__(from_row, from_col)

        return captured_piece  # Devuelve la pieza capturada, si hay

    def __get_piece__(self, row, col):
        """Devuelve la pieza en la posición dada del tablero."""
        return self.__positions__[row][col]

    def __set_piece__(self, row, col, piece):
        """Coloca una pieza en una posición específica del tablero."""
        self.__check_bounds__(row, col)
        self.__positions__[row][col] = piece

    def __get_pieces__(self):
        """Devuelve todas las piezas actuales en el tablero."""
        pieces = []
        for row in self.__positions__:
            for piece in row:
                if piece:
                    pieces.append(piece)
        return pieces

    def __pieces_on_board__(self):
        """Devuelve una lista de todas las piezas en el tablero."""
        white_pieces = 0
        black_pieces = 0
        for row in self.__positions__:
            for piece in row:
                if piece:
                    if piece.__get_color__().lower() == 'white':
                        white_pieces += 1
                    elif piece.__get_color__().lower() == 'black':
                        black_pieces += 1
        return white_pieces, black_pieces

    def __is_valid_move__(self, piece, from_pos, to_pos):
        """Verifica si un movimiento de una posición inicial a una final es válido."""
        return piece.__movimiento_correcto__(from_pos[0], from_pos[1], to_pos[0], to_pos[1], self)
