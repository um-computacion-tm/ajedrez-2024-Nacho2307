from Juego.Piezas.Piece import Piece

class Rook(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, 'Rook', x, y)
        
    def movimiento_correcto(self, from_row, from_col, to_row, to_col, board):
        from_pos = (from_row, from_col)
        to_pos = (to_row, to_col)
        
        if not self.dentro_de_limites(from_pos, to_pos):
            return False
        
        if self._movimiento_en_linea_recta(from_pos, to_pos):
            return self._camino_libre_y_captura(from_pos, to_pos, board)

        return False

    
    def _movimiento_en_linea_recta(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return to_row == from_row or to_col == from_col

    def _camino_libre_y_captura(self, from_pos, to_pos, board):
        direction, start, end = self._determinar_direccion_y_límites(from_pos, to_pos)
        camino_libre = self._camino_libre(direction, start, end, board, from_pos)
        return camino_libre

    def _determinar_direccion_y_límites(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        if from_row == to_row:  # Movimiento horizontal
            direction = "horizontal"
            start, end = from_col, to_col
        else:  # Movimiento vertical
            direction = "vertical"
            start, end = from_row, to_row

        paso = 1 if end > start else -1
        return direction, start + paso, end

    def _camino_libre(self, direction, start, end, board, from_pos):
        from_row, from_col = from_pos
        for pos in range(start, end, 1 if end > start else -1):
            if direction == "horizontal" and board.get_piece(from_row, pos) is not None:
                return False
            elif direction == "vertical" and board.get_piece(pos, from_col) is not None:
                return False
        return True