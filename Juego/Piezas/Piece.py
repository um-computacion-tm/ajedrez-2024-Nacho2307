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
        self.__nombre__ = nombre
        self.__color__ = color.lower()
        self.__simbolo__ = self.SYMBOLS.get(nombre, {}).get(self.__color__, ' ')
        self.__x__ = x
        self.__y__ = y
    
    def __str__(self):
        return self.__simbolo__
    
    def get_color(self):
        return self.__color__.capitalize()
    
    def get_x(self):
        return self.__x__
    
    def get_y(self):
        return self.__y__

    def possible_moves(self, board):
        raise NotImplementedError("Este método debe ser implementado en las subclases.")

    def movimiento_posible(self, from_row, from_col, board):
        raise NotImplementedError("Este método debe ser implementado por subclases.")

    def movimiento_correcto(self, from_row, from_col, to_row, to_col, board):
        raise NotImplementedError("Este método debe ser implementado por subclases.")

    def get_coordinates(self, new_position):
        x, y = new_position
        current_x, current_y = self.__x__, self.__y__
        return x, y, current_x, current_y
    
    def get_position(self):
        # Devuelve las coordenadas actuales de la pieza
        return self.__x__, self.__y__
    
    @staticmethod
    def dentro_de_limites(from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return 0 <= from_row <= 7 and 0 <= from_col <= 7 and 0 <= to_row <= 7 and 0 <= to_col <= 7
    
    def check_move(self, board, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        
        if not self.dentro_de_limites(from_pos, to_pos):
            return False
        
        return self.movimiento_correcto(from_row, from_col, to_row, to_col, board)
