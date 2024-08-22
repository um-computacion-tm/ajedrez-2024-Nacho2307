from Piezas.Rook import Rook
from Piezas.Knight import Knight
from Piezas.King import King    
from Piezas.Bishop import Bishop
from Piezas.Pawn import Pawn
from Piezas.Queen import Queen

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
            Knight("Black"),  # Caballo negro izquierdo
            Bishop("Black"),  # Alfil negro izquierdoS
            Queen("Black"),  # Reina negra
            King("Black"),  # Rey negro
            Bishop("Black"),  # Alfil negro derecho
            Knight("Black"),  # Caballo negro derecho
            Rook("Black")  # Torre Negra derecho 
        ]
# Se ponen los peones negros en la fila 1
        self.__positions__[1] = [Pawn("Black")]*8

# Se ponen los peones blancos en la fila 6
        self.__positions__[6] = [Pawn("White")]*8
      
        # Establece las piezas en la fila 7 (blancas)
        self.__positions__[7] = [
            Rook("White"),  # Torre blanca izquierda
            Knight("White"),  # Caballo blanco izquierdo
            Bishop("White"),  # Alfil blanco izquierdo
            Queen("White"),  # Reina blanca
            King("White"),  # Rey blanco
            Bishop("White"),  # Alfil blanco derecho
            Knight("White"),  # Caballo blanco derecho
            Rook("White")  # Torre blanca derecha
        ]
 
# Devuelve una representacion en texto del tablero       
    def __str__(self):
      resultado = ""
      for row in self.__positions__:
        fila_texto = []
        for piece in row:
            if piece:
                fila_texto.append(str(piece))
            else:
                fila_texto.append(".")
        resultado += "".join(fila_texto) + "\n"
      return resultado
        
# Devuelve la pieza en la posicion (row, col)
    def get_piece(self, row, col):
     return self.__positions__[row] [col]

if __name__ == "__main__":
    board = Board()
    print(board)
...