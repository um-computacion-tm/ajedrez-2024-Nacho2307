from board import Board
from Chess import Chess

def main():
    chess = Chess()
    while True:
        play(chess)
        
def play(chess):
    try: 
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To row: "))
        to_col = int(input("To col: "))
    except Exception as e:
     print("Error")
     return

        
    chess.move(
        from_row, 
        from_col, 
        to_row, 
        to_col,
    )
    # validate coords
def move(self, from_row, from_col, to_row, to_col):
 piece = self.board.get_piece(from_row, from_col)
 if piece is not None:
        if piece.color == self.__turn__:
            self.board._positions[from_row][from_col] = None
            self.board._positions[to_row][to_col] = piece
            self.change_turn()
        else:
            print("Error: It's not your turn")
 else:
        print("Error: No piece at that position")
    
def change_turn(self):
     if self.__turn__ == "WHITE":
        self.__turn__ = "BLACK"
     else:
        self.__turn__ = "WHITE"
        
        
   
    
if __name__ == '__main__':
    main()