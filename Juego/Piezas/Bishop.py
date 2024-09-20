from Juego.Piezas.Piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color.lower(), 'Bishop')

    def movimiento_correcto(self, from_row, from_col, to_row, to_col, board):
        if not self.es_movimiento_diagonal(from_row, from_col, to_row, to_col):
            return False
        # Verificar si la casilla de destino tiene una pieza del mismo color
        destino = board.__positions__[to_row][to_col]
        if destino is not None and destino.get_color() == self.get_color():
            return False
        return self.es_camino_despejado(board.__positions__, (from_row, from_col), (to_row, to_col))

    def es_movimiento_diagonal(self, from_row, from_col, to_row, to_col):
        # Verifica si la diferencia de filas es igual a la diferencia de columnas
        return abs(to_row - from_row) == abs(to_col - from_col)

    def es_camino_despejado(self, positions, from_pos, to_pos):
        step_row, step_col = self.direccion_movimiento(from_pos, to_pos)
        return self.chequear_camino_libre(positions, from_pos, to_pos, step_row, step_col)

    def direccion_movimiento(self, from_pos, to_pos):
        step_row = 1 if to_pos[0] > from_pos[0] else -1
        step_col = 1 if to_pos[1] > from_pos[1] else -1
        return step_row, step_col

    def chequear_camino_libre(self, positions, from_pos, to_pos, step_row, step_col):
        current_row, current_col = from_pos[0] + step_row, from_pos[1] + step_col
        while current_row != to_pos[0] or current_col != to_pos[1]:  # Recorre el camino hasta antes de la posición destino
            if positions[current_row][current_col] is not None:  # Si hay una pieza en el camino
                return False
            current_row += step_row
            current_col += step_col
        return True  # El camino está despejado

