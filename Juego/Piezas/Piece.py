class Piece:
    SYMBOLS = {
        'Pawn':   {'white': '♙', 'black': '♟'},
        'Rook':   {'white': '♖', 'black': '♜'},
        'Knight': {'white': '♘', 'black': '♞'},
        'Bishop': {'white': '♗', 'black': '♝'},
        'Queen':  {'white': '♕', 'black': '♛'},
        'King':   {'white': '♔', 'black': '♚'}
    }

    def __init__(self, color, nombre, x=0, y=0):
        self.__nombre__ = nombre  # Nombre de la pieza
        self.__color__ = color.lower()  # Color de la pieza
        self.__simbolo__ = self.SYMBOLS[nombre][self.__color__]  # Simbolo para representar la pieza
        self.__x__ = x  # Fila inicial
        self.__y__ = y  # Columna inicial
    
    # Da el simbolo de la pieza como texto
    def __str__(self):
        return self.__simbolo__
    
    def get_color(self):
        return self.__color__.capitalize()
    
    def get_x(self):
        return self.__x__
    
    def get_y(self):
        return self.__y__
    
    # Determina si un movimiento de cualquier pieza es valido
    def movimiento_posible(self, from_row, from_col, board):
        raise NotImplementedError("Este método debe ser implementado por subclases.")

    def movimiento_correcto(self, from_row, from_col, to_row, to_col, board):
        raise NotImplementedError("Este método debe ser implementado por subclases.")

    def get_coordinates(self, new_position):
        x, y = new_position
        current_x, current_y = self.__x__, self.__y__
        return x, y, current_x, current_y