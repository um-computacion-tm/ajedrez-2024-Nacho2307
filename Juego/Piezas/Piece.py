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
        self.__simbolo__ = self.SYMBOLS.get(nombre, {}).get(self.__color__, ' ')  # Simbolo para representar la pieza
        self.__x__ = x  # Fila inicial
        self.__y__ = y  # Columna inicial
    
    # Da el simbolo de la pieza como texto
    def __str__(self):
        return self.__simbolo__
    
    def get_color(self):
        print(f"Color de la pieza: {self.__color__}")
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
        print(f"Nueva posición: {new_position}, Posición actual: ({current_x}, {current_y})")
        return x, y, current_x, current_y
    
    # Método común para todas las piezas
    @staticmethod
    def dentro_de_limites(from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return 0 <= from_row <= 7 and 0 <= from_col <= 7 and 0 <= to_row <= 7 and 0 <= to_col <= 7
    
    # Verifica los movimientos para todas las piezas
    def chech_move(self, board, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        
        # Verifica si el movimiento es dentro de los limites del board
        if not self.dentro_de_limites(from_pos, to_pos):
            return False
        return self.movimiento_correcto(from_row, from_col, to_row, to_col, board)
    