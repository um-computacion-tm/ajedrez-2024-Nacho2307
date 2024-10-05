from Juego.Piezas.piece import Piece

class Pawn(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, 'Pawn', x, y)

    def __movimiento_correcto__(self, from_row, from_col, to_row, to_col, board):
        from_pos = (from_row, from_col)
        to_pos = (to_row, to_col)
        direccion = -1 if self.__get_color__() == "White" else 1

        # Verificar si la casilla de destino tiene una pieza del mismo color
        destino = board.__get_piece__(to_row, to_col)
        if destino is not None and destino.__get_color__() == self.__get_color__():
            return False  

        # Inicializa la variable de resultado
        movimiento_valido = False

        # Chequeo de movimiento simple hacia adelante
        if self.__movimiento_simple__(from_pos, to_pos, direccion, board):
            movimiento_valido = True
        # Chequeo de movimiento doble inicial
        elif self.__movimiento_doble_inicial__(from_pos, to_pos, direccion, board):
            movimiento_valido = True
        # Chequeo de captura diagonal
        elif self.__captura_diagonal__(from_pos, to_pos, direccion, board):
            movimiento_valido = True

        # Retorna el resultado de las comprobaciones
        return movimiento_valido

    def __movimiento_simple__(self, from_pos, to_pos, direccion, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        pieza_destino = board.__get_piece__(to_row, to_col)
        return (from_col == to_col and 
                to_row == from_row + direccion and 
                pieza_destino is None)

    def __movimiento_doble_inicial__(self, from_pos, to_pos, direccion, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        pieza_destino = board.__get_piece__(to_row, to_col)
        es_movimiento_valido = (
            (self.__get_color__() == "White" and from_row == 6) or 
            (self.__get_color__() == "Black" and from_row == 1)
        )
        return (es_movimiento_valido and 
                to_row == from_row + 2 * direccion and 
                pieza_destino is None and 
                board.__get_piece__(from_row + direccion, from_col) is None)

    def __captura_diagonal__(self, from_pos, to_pos, direccion, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        pieza_destino = board.__get_piece__(to_row, to_col)
        return (abs(from_col - to_col) == 1 and 
                to_row == from_row + direccion and 
                pieza_destino is not None and 
                pieza_destino.__get_color__() != self.__get_color__())