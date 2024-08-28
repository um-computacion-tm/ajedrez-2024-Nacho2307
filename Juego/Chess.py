from Juego.board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece is not None and piece.get_color() == self.__turn__:
            if piece.movimiento_correcto(from_row, from_col, to_row, to_col, self.__board__):
                self.__move_piece__(from_row, from_col, to_row, to_col, piece)
                self.change_turn()
            else:
                print("Error: Movimiento Invalido")
        else:
            print("Error: Movimiento Invalido o la pieza no pertenece al turno actual")

    def __move_piece__(self, from_row, from_col, to_row, to_col, piece):
        self.__board__.set_piece(to_row, to_col, piece)
        self.__board__.set_piece(from_row, from_col, None)

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

    @property
    def turn(self):
        return self.__turn__

    def get_piece(self, row, col):
        return self.__board__.get_piece(row, col)

    def print_board(self):
        print(self.__board__)




    
      
    
        
       

   

   

    