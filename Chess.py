from board import Board


class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def move(self, from_row, from_col, to_row, to_col):
        # validate coords
       piece = self.board.get_piece(from_row, from_col)
       if piece is not None:
            self.board._positions[from_row][from_col] = None
            self.board._positions[to_row][to_col] = piece
            self.change_turn()
       else:
            print("Error: No es tu turno")
            print("Error: No hay una pieza en esa posicion")
        

    @property
    def turn(self):
        return self.__turn__

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"