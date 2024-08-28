from Juego.Piezas.Piece import Piece

class Rook(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color.lower(), 'Rook', x, y)
    
    def movimiento_correcto(self, from_pos, to_pos, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        if not self._dentro_de_limites(from_pos, to_pos):
            return False
        
        if self._movimiento_en_linea_recta(from_pos, to_pos):
            return self._camino_libre_y_captura(from_pos, to_pos, board)

        return False

    def _dentro_de_limites(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return 0 <= from_row <= 7 and 0 <= from_col <= 7 and 0 <= to_row <= 7 and 0 <= to_col <= 7

    def _movimiento_en_linea_recta(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return to_row == from_row or to_col == from_col

    def _camino_libre_y_captura(self, from_pos, to_pos, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        if from_row == to_row:
            paso = 1 if to_col > from_col else -1
            for col in range(from_col + paso, to_col, paso):
                if board.get_piece(from_row, col) is not None:
                    return False
        else:
            paso = 1 if to_row > from_row else -1
            for row in range(from_row + paso, to_row, paso):
                if board.get_piece(row, from_col) is not None:
                    return False
        
        final_piece = board.get_piece(to_row, to_col)
        return final_piece is None or final_piece.get_color() != self.get_color()
