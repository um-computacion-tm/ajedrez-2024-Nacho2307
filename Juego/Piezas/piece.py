class Piece:
    """
    Clase base para las piezas del juego de ajedrez.

    Atributos:
        SYMBOLS: Diccionario que contiene los símbolos de las piezas para cada color.
        VALUES: Diccionario que contiene los valores de cada tipo de pieza.
    """
    
    SYMBOLS = {
        'Pawn':   {'white': '♙', 'black': '♟'},
        'Rook':   {'white': '♖', 'black': '♜'},
        'Knight': {'white': '♘', 'black': '♞'},
        'Bishop': {'white': '♗', 'black': '♝'},
        'Queen':  {'white': '♕', 'black': '♛'},
        'King':   {'white': '♔', 'black': '♚'}
    }
    
    VALUES = {
        'Pawn': 1,
        'Rook': 5,
        'Knight': 3,
        'Bishop': 3,
        'Queen': 9,
        'King': 8
    }

    def __init__(self, color, nombre, x=0, y=0):
        """Inicializa una pieza con su color, nombre y posición en el tablero."""
        self.__nombre__ = nombre
        self.__color__ = color.lower()
        self.__simbolo__ = self.SYMBOLS.get(nombre, {}).get(self.__color__, ' ')
        self.__x__ = x
        self.__y__ = y
    
    def __str__(self):
        """Retorna el símbolo de la pieza."""
        return self.__simbolo__
    
    def __get_color__(self):
        """Devuelve el color de la pieza."""
        return self.__color__.capitalize()
    
    def __get_x__(self):
        """Devuelve la coordenada X de la pieza."""
        return self.__x__
    
    def __get_y__(self):
        """Devuelve la coordenada Y de la pieza."""
        return self.__y__

    def __possible_moves__(self, board):
        """Devuelve los movimientos posibles para la pieza (debe ser implementado por subclases)."""
        raise NotImplementedError("Este método debe ser implementado en las subclases.")

    def __movimiento_posible__(self, from_row, from_col, board):
        """Verifica si un movimiento es posible (debe ser implementado por subclases)."""
        raise NotImplementedError("Este método debe ser implementado por subclases.")

    def __movimiento_correcto__(self, from_row, from_col, to_row, to_col, board):
        """Verifica si el movimiento es correcto (debe ser implementado por subclases)."""
        raise NotImplementedError("Este método debe ser implementado por subclases.")

    def __get_coordinates__(self, new_position):
        """Devuelve las coordenadas actuales y nuevas de la pieza."""
        x, y = new_position
        current_x, current_y = self.__x__, self.__y__
        return x, y, current_x, current_y
    
    def __get_position__(self):
        """Devuelve la posición actual de la pieza."""
        return self.__x__, self.__y__

    @staticmethod
    def __dentro_de_limites__(from_pos, to_pos):
        """Verifica si las posiciones están dentro de los límites del tablero."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return 0 <= from_row <= 7 and 0 <= from_col <= 7 and 0 <= to_row <= 7 and 0 <= to_col <= 7

    def __check_move__(self, board, from_pos, to_pos):
        """Verifica si el movimiento es válido en el tablero."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        if not self.__dentro_de_limites__(from_pos, to_pos):
            return False  # Fuera de límites

        return self.__movimiento_correcto__(from_row, from_col, to_row, to_col, board)

    def __get_value__(self):
        """Devuelve el valor de la pieza."""
        return self.VALUES.get(self.__nombre__, 0)  # Devuelve el valor de la pieza

    def __misma_pieza_en_destino__(self, destino):
        """Verifica si la casilla de destino tiene una pieza del mismo color."""
        if destino:
            color_self = self.__get_color__()
            color_destino = destino.__get_color__()
            return color_self == color_destino
        return False
