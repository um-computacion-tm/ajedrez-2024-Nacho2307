from Juego.Piezas.Piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color.lower(), 'Bishop')

    def movimiento_correcto(self, from_row, from_col, to_row, to_col, board):
        if not self.es_movimiento_diagonal(from_row, from_col, to_row, to_col):
            return False
        return self.es_camino_despejado(board.__positions__, from_row, from_col, to_row, to_col)

    def es_movimiento_diagonal(self, from_row, from_col, to_row, to_col):
        return abs(to_row - from_row) == abs(to_col - from_col)

    def es_camino_despejado(self, positions, from_row, from_col, to_row, to_col):
        step_row, step_col = self.direccion_movimiento(from_row, to_row, from_col, to_col)
        return self.chequear_camino_libre(positions, from_row, from_col, to_row, to_col, step_row, step_col)

    def direccion_movimiento(self, from_row, to_row, from_col, to_col):
        step_row = 1 if to_row > from_row else -1
        step_col = 1 if to_col > from_col else -1
        return step_row, step_col

    def chequear_camino_libre(self, positions, from_row, from_col, to_row, to_col, step_row, step_col):
        current_row, current_col = from_row + step_row, from_col + step_col
        while current_row != to_row and current_col != to_col:
            if positions[current_row][current_col] is not None:
                return False
            current_row += step_row
            current_col += step_col
        return True
