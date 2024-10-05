from Juego.Piezas.piece import Piece

class Rook(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, 'Rook', x, y)

    def __movimiento_correcto__(self, from_row, from_col, to_row, to_col, board):
        from_pos = (from_row, from_col)
        to_pos = (to_row, to_col)
    
        # Verificar si la posición está dentro de los límites
        if not self.__dentro_de_limites__(from_pos, to_pos):
            return False
    
        # Verificar si el movimiento es en línea recta (horizontal o vertical)
        if self.__movimiento_en_linea_recta__(from_pos, to_pos):
            # Verificar si el camino está libre y no se está capturando una pieza del mismo color
            pieza_destino = board.__get_piece__(to_row, to_col)
            if pieza_destino is None or pieza_destino.__get_color__() != self.__get_color__():
                return self.__camino_libre_y_captura__(from_pos, to_pos, board)

        return False

    def __movimiento_en_linea_recta__(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return to_row == from_row or to_col == from_col

    def __camino_libre_y_captura__(self, from_pos, to_pos, board):
        direction, start, end = self.__determinar_direccion_y_limites__(from_pos, to_pos)
        camino_libre = self.__camino_libre__(direction, start, end, board, from_pos)
        return camino_libre

    def __determinar_direccion_y_limites__(self, from_pos, to_pos):
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

    def __camino_libre__(self, direction, start, end, board, from_pos):
        from_row, from_col = from_pos
        for pos in range(start, end, 1 if end > start else -1):
            if direction == "horizontal" and board.__get_piece__(from_row, pos) is not None:
                return False
            elif direction == "vertical" and board.__get_piece__(pos, from_col) is not None:
                return False
        return True
