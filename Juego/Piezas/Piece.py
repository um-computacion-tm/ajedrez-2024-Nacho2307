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
        self.__nombre__ = nombre # Nombre de la pieza
        self.__color__ = color # Color de la pieza
        self.__simbolo__ = self.SYMBOLS[nombre][color] # simbolo para representar la pieza
        self.__x__ = x # Fila inical
        self.__y__ = y # Columna inicial
    
    # Da el simbolo de la pieza como texto
   def __str__(self):
        return self.__simbolo__
    
    # Determina si un movimiento de cualquier pieza es valido
   def movimiento_correcto(self, from_row, from_col, to_row, to_col):
        return False
    