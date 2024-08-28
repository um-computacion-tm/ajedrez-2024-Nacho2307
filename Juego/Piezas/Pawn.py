from Juego.Piezas.Piece import Piece

class Pawn(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, 'Pawn', x, y)

    def movimiento_correcto(self, from_row, from_col, to_row, to_col, board):
        direccion = -1 if self.get_color() == "white" else 1
        
        # Movimiento simple
        if from_col == to_col:
            # Casilla de a una
            if to_row == from_row + direccion and board.get_piece(to_row, to_col) is None:
                return True
            
            # Movimiento de dos casillas desde la fila inicial
            if ((self.get_color() == "black" and from_row == 6) or 
                (self.get_color() == "white" and from_row == 1)) and \
                to_row == from_row + 2 * direccion and board.get_piece(to_row, to_col) is None:
                # Ve si la casilla intermedia esta vacia
                intermediate_row = from_row + direccion
                if board.get_piece(intermediate_row, from_col) is None:
                    return True
        
        # Captura Diagonal
        if abs(from_col - to_col) == 1 and to_row == from_row + direccion:
            objetivo_piece = board.get_piece(to_row, to_col)
            if objetivo_piece is not None and objetivo_piece.get_color() != self.get_color():
               return True
        
        return False
