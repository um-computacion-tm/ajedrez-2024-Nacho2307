from Juego.Piezas.Piece import Piece

class Rook(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, 'Rook', x, y)

    def movimiento_correcto(self, from_pos, to_pos, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        if not self.dentro_de_limites(from_pos, to_pos):
            return False
        
        if self._movimiento_en_linea_recta(from_pos, to_pos):
            return self._camino_libre_y_captura(from_row, from_col, to_row, to_col, from_pos, to_pos, board)

        return False

    def _movimiento_en_linea_recta(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return to_row == from_row or to_col == from_col

    def _camino_libre_y_captura(self, from_pos, to_pos, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        if from_row == to_row:
            return self._camino_libre(from_row, from_col, to_col, 1 if to_col > from_col else -1, board, horizontal=True)
        elif from_col == to_col:
            return self._camino_libre(from_row, from_col, to_row, 1 if to_row > from_row else -1, board, horizontal=False)

        return False

    def _camino_libre(self, start, end, paso, board, horizontal):
        if horizontal:
            for col in range(start + paso, end, paso):
                if board.get_piece(start, col) is not None:
                    return False
        else:
            for row in range(start + paso, end, paso):
                if board.get_piece(row, start) is not None:
                    return False
        return True
 