from Juego.Piezas.Piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color.lower(), 'Bishop')

    def __movimiento_correcto__(self, from_row, from_col, to_row, to_col, board):
        if not self.__es_movimiento_diagonal__(from_row, from_col, to_row, to_col):
            return False
        # Verificar si la casilla de destino tiene una pieza del mismo color
        destino = board.__positions__[to_row][to_col]
        if destino is not None:
            if destino.__get_color__() == self.__get_color__():
                return False  # No puede moverse a una casilla ocupada por una pieza del mismo color
            # Si es una pieza de color contrario, es una captura, así que permitimos el movimiento
        return self.__es_camino_despejado__(board.__positions__, (from_row, from_col), (to_row, to_col))

    def __es_movimiento_diagonal__(self, from_row, from_col, to_row, to_col):
        # Verifica si la diferencia de filas es igual a la diferencia de columnas
        return abs(to_row - from_row) == abs(to_col - from_col)

    def __es_camino_despejado__(self, positions, from_pos, to_pos):
        step_row, step_col = self.__direccion_movimiento__(from_pos, to_pos)
        return self.__chequear_camino_libre__(positions, from_pos, to_pos, step_row, step_col)

    def __direccion_movimiento__(self, from_pos, to_pos):
        step_row = 1 if to_pos[0] > from_pos[0] else -1
        step_col = 1 if to_pos[1] > from_pos[1] else -1
        return step_row, step_col

    def __chequear_camino_libre__(self, positions, from_pos, to_pos, step_row, step_col):
        current_row, current_col = from_pos[0] + step_row, from_pos[1] + step_col
        while current_row != to_pos[0] or current_col != to_pos[1]:  # Recorre el camino hasta antes de la posición destino
            if positions[current_row][current_col] is not None:  # Si hay una pieza en el camino
                return False
            current_row += step_row
            current_col += step_col
        return True  # El camino está despejado

