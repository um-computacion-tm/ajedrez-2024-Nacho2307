from Juego.Piezas.Piece import Piece

class Pawn(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, 'Pawn', x, y)

    def movimiento_correcto(self, from_pos, to_pos, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        direccion = -1 if self.get_color() == "White" else 1
        
        if not self._dentro_de_limites(from_pos, to_pos):
            return False
        
        if self._movimiento_simple(from_pos, to_pos, direccion, board):
            return True

        if self._movimiento_doble_inicial(from_pos, to_pos, direccion, board):
            return True

        if self._captura_diagonal(from_pos, to_pos, direccion, board):
            return True

        return False

    def _dentro_de_limites(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return 0 <= from_row <= 7 and 0 <= from_col <= 7 and 0 <= to_row <= 7 and 0 <= to_col <= 7

    def _movimiento_simple(self, from_pos, to_pos, direccion, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return (from_col == to_col and 
                to_row == from_row + direccion and 
                board.get_piece(to_row, to_col) is None)

    def _movimiento_doble_inicial(self, from_pos, to_pos, direccion, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        if ((self.get_color() == "Black" and from_row == 6) or 
            (self.get_color() == "White" and from_row == 1)):
            return (to_row == from_row + 2 * direccion and 
                    board.get_piece(to_row, to_col) is None and 
                    board.get_piece(from_row + direccion, from_col) is None)
        return False

    def _captura_diagonal(self, from_pos, to_pos, direccion, board):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return (abs(from_col - to_col) == 1 and 
                to_row == from_row + direccion and 
                board.get_piece(to_row, to_col) is not None and 
                board.get_piece(to_row, to_col).get_color() != self.get_color())
