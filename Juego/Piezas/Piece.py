class Piece:
    def __init__(self, color, nombre, simbolo):
        self.__nombre__ = nombre # Nombre de la pieza
        self.__color__ = color # Color de la pieza
        self.__simbolo__ = simbolo # simbolo para representar la pieza
    
    # Da el simbolo de la pieza como texto
    def __str__(self):
        return self.__simbolo__
    
    # Determina si un movimiento de cualquier pieza es valido
    def movimiento_correcto(self, desde_fila, desde_columna, hasta_fila, hasta_columna):
        return False
    