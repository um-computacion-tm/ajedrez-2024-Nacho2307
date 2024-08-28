from Juego.Piezas.Piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color.lower(), 'Bishop')
    
    # El Alfil se mueve en diagonal
   
    def movimiento_correcto(self, from_row, from_col, to_row, to_col, board):
        # Verificar si el movimiento es diagonal
        if abs(to_row - from_row) == abs(to_col - from_col):
            return self.diagonal_move(board.__positions__, (from_row, from_col), (to_row, to_col))
        return False

    def diagonal_move(self, positions, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        step_row = 1 if to_row > from_row else -1
        step_col = 1 if to_col > from_col else -1
        
        current_row, current_col = from_row + step_row, from_col + step_col
        while current_row != to_row and current_col != to_col:
            if positions[current_row][current_col] is not None:
                return False
            current_row += step_row
            current_col += step_col
        return True