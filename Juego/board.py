from Juego.Piezas.Rook import Rook
from Juego.Piezas.Knight import Knight
from Juego.Piezas.King import King
from Juego.Piezas.Bishop import Bishop
from Juego.Piezas.Pawn import Pawn
from Juego.Piezas.Queen import Queen

class Board:
    #Inicializa el tablero de ajedrez y coloca las piezas en sus posiciones iniciales.
    def __init__(self):
        self.__positions__ = [[None] * 8 for _ in range(8)]
        self.__setup_pieces__()

    #Coloca todas las piezas en el tablero en sus posiciones iniciales.
    def __setup_pieces__(self):
        # Piezas negras
        self.__positions__[0] = [
            Rook("Black"), Knight("Black"), Bishop("Black"), Queen("Black"),
            King("Black"), Bishop("Black"), Knight("Black"), Rook("Black")
        ]
        # Crear 8 peones negros únicos
        self.__positions__[1] = [Pawn("Black") for _ in range(8)]

        # Crear 8 peones blancos únicos
        self.__positions__[6] = [Pawn("White") for _ in range(8)]

        # Piezas blancas
        self.__positions__[7] = [
            Rook("White"), Knight("White"), Bishop("White"), Queen("White"),
            King("White"), Bishop("White"), Knight("White"), Rook("White")
        ]

    # Limpia el tablero, removiendo todas las piezas.
    def __clear_board__(self):
        self.__positions__ = [[None] * 8 for _ in range(8)]

    #Coloca una pieza en una posición específica del tablero.
    def __place_piece__(self, piece, position):
        row, col = position
        self.__positions__[row][col] = piece

    # Remueve una pieza de una posición específica del tablero.
    def __remove_piece__(self, row, col):
        self.__check_bounds__(row, col)
        self.__positions__[row][col] = None

    # Retorna una representación en cadena del tablero.
    def __str__(self):
        resultado = ""
        for row in self.__positions__:
            fila_texto = [str(piece) if piece else "." for piece in row]
            resultado += " ".join(fila_texto) + "\n"
        return resultado

    # Imprime las coordenadas del tablero para referencia visual.
    def __mostrar_coords__(self):
        mostrar = "  0 1 2 3 4 5 6 7\n"
        for i, row in enumerate(self.__positions__):
            fila = f"{i} " + " ".join([piece.__str__() if piece else '.' for piece in row]) + "\n"
            mostrar += fila
        return mostrar

    # Mueve una pieza de una posición inicial a una posición final.
    def __check_bounds__(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return True
        else:
            raise IndexError("Posición fuera del tablero.")

    # Método para mover una pieza y capturar si es necesario
    def __move_piece__(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        piece_to_move = self.__get_piece__(from_row, from_col)
        captured_piece = self.__get_piece__(to_row, to_col)

        # Mover la pieza a la nueva posición
        self.__set_piece__(to_row, to_col, piece_to_move)
        self.__remove_piece__(from_row, from_col)

        # Devolver la pieza capturada, si es que la hay
        return captured_piece

    # Devuelve la pieza en la posición dada del tablero.
    def __get_piece__(self, row, col):
        return self.__positions__[row][col]

    # Coloca una pieza en una posición específica del tablero.
    def __set_piece__(self, row, col, piece):
        self.__check_bounds__(row, col)
        self.__positions__[row][col] = piece

    #  Devuelve todas las piezas actuales en el tablero.
    def __get_pieces__(self):
        pieces = []
        for row in self.__positions__:
            for piece in row:
                if piece:
                    pieces.append(piece)
        return pieces

    # Devuelve una lista de todas las piezas en el tablero.
    def __pieces_on_board__(self):
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

    # Verifica si un movimiento de una posición inicial a una final es válido.
    def __is_valid_move__(self, piece, from_pos, to_pos):
        return piece.__movimiento_correcto__(from_pos[0], from_pos[1], to_pos[0], to_pos[1], self)
