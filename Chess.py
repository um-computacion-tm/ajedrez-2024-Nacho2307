from board import Board


class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    #Mueve una pieza del tablero si pertenece al jugador actual y el movimiento es válido.
    def move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece is not None and piece.color == self.__turn__:
            self.__move_piece__(from_row, from_col, to_row, to_col)
            self.change_turn()
        else:
            print("Error: Movimiento Invalido")
            
    #Mueve una pieza de una posición a otra en el tablero.
    def __move_piece__(self, piece, from_row, from_col, to_row, to_col):
        self.__board__.__positions__[from_row][from_col] = None
        self.__board__.__positions__[to_row][to_col] = piece  
                 
     # Si el turno actual es "WHITE", cambia a "BLACK"; de lo contrario, cambia a "WHITE"
    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
                    
@property
def turn(self):
        return self.__turn__





    
      
    
        
       

   

   

    