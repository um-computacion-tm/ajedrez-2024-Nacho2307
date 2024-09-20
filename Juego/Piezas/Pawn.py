from Juego.Piezas.Piece import Piece

class Pawn(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, 'Pawn', x, y)

    def movimiento_correcto(self, from_row, from_col, to_row, to_col, board):
        from_pos = (from_row, from_col)
        to_pos = (to_row, to_col)
        direccion = -1 if self.get_color() == "White" else 1

        # Verificar si la casilla de destino tiene una pieza del mismo color
        destino = board.get_piece(to_row, to_col)
        if destino is not None and destino.get_color() == self.get_color():
            return False  # Puedes dejar este return ya que es importante

        # Inicializa la variable de resultado
        movimiento_valido = False

        # Chequeo de movimiento simple hacia adelante
        if self._movimiento_simple(from_pos, to_pos, direccion, board):
            movimiento_valido = True
        # Chequeo de movimiento doble inicial
        elif self._movimiento_doble_inicial(from_pos, to_pos, direccion, board):
            movimiento_valido = True
        # Chequeo de captura diagonal
        elif self._captura_diagonal(from_pos, to_pos, direccion, board):
            movimiento_valido = True

        # Retorna el resultado de las comprobaciones
        return movimiento_valido

    def _movimiento_simple(self, from_pos, to_pos, direccion, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        pieza_destino = board.get_piece(to_row, to_col)
        return (from_col == to_col and 
                to_row == from_row + direccion and 
                pieza_destino is None)

    def _movimiento_doble_inicial(self, from_pos, to_pos, direccion, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        pieza_destino = board.get_piece(to_row, to_col)
        es_movimiento_valido = (
            (self.get_color() == "White" and from_row == 6) or 
            (self.get_color() == "Black" and from_row == 1)
        )
        return (es_movimiento_valido and 
                to_row == from_row + 2 * direccion and 
                pieza_destino is None and 
                board.get_piece(from_row + direccion, from_col) is None)

    def _captura_diagonal(self, from_pos, to_pos, direccion, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        pieza_destino = board.get_piece(to_row, to_col)
        return (abs(from_col - to_col) == 1 and 
                to_row == from_row + direccion and 
                pieza_destino is not None and 
                pieza_destino.get_color() != self.get_color())