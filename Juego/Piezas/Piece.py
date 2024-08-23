class Piece:
     SYMBOLS = {
        'Pawn':   {'White': '♙', 'Black': '♟'},
        'Rook':   {'White': '♖', 'Black': '♜'},
        'Knight': {'White': '♘', 'Black': '♞'},
        'Bishop': {'White': '♗', 'Black': '♝'},
        'Queen':  {'White': '♕', 'Black': '♛'},
        'King':   {'White': '♔', 'Black': '♚'}
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
     def movimiento_correcto(self, desde_fila, desde_columna, hasta_fila, hasta_columna):
        return False
    