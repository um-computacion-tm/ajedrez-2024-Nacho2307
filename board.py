from Piezas import Rook, knight, Bishop, Pawn, Queen, King

class Board:
    def __init__(self):
        self.__positions__ = []
        # Inicializo el tablero con 8x8 posiciones que esten vacias 
        for  _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)            
            self.__positions__.append(col) 
# Posiciones de las piezas del ajedrez de color negro
# Las piezas son puesta en la fila 0
        self.__positions__[0] = [
            Rook("Black"),  # Torre Negra izquierda 
            knight("Black"),  # Caballo negro izquierdo
            Bishop("Black"),  # Alfil negro izquierdo
            Queen("Black"),  # Reina negra
            King("Black"),  # Rey negro
            Bishop("Black"),  # Alfil negro derecho
            knight("Black"),  # Caballo negro derecho
            Rook("Black")  # Torre Negra derecho 
        ]
# Se ponen los peones negros en la fila 1
        self.__positions__[1] = [Pawn("Black")]*8

        

        
# Devuelve la pieza en la posicion (row, col)
def get_piece(self, row, col):
    return self.board.__positions__[row] [col]
...