from Juego.Piezas.Piece import Piece

class Pawn(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, 'Pawn', x, y)

    def movimiento_correcto(self, from_row, from_col, to_row, to_col, board):
        direccion = -1 if self.get_color() == "White" else 1
        
        if not self._dentro_de_limites(from_row, from_col, to_row, to_col):
            return False
        
        if self._movimiento_simple(from_row, from_col, to_row, to_col, direccion, board):
            return True

        if self._movimiento_doble_inicial(from_row, from_col, to_row, to_col, direccion, board):
            return True

        if self._captura_diagonal(from_row, from_col, to_row, to_col, direccion, board):
            return True

        return False

    def _dentro_de_limites(self, from_row, from_col, to_row, to_col):
        return 0 <= from_row <= 7 and 0 <= from_col <= 7 and 0 <= to_row <= 7 and 0 <= to_col <= 7

    def _movimiento_simple(self, from_row, from_col, to_row, to_col, direccion, board):
        return (from_col == to_col and 
                to_row == from_row + direccion and 
                board.get_piece(to_row, to_col) is None)

    def _movimiento_doble_inicial(self, from_row, from_col, to_row, to_col, direccion, board):
        if ((self.get_color() == "Black" and from_row == 6) or 
            (self.get_color() == "White" and from_row == 1)):
            return (to_row == from_row + 2 * direccion and 
                    board.get_piece(to_row, to_col) is None and 
                    board.get_piece(from_row + direccion, from_col) is None)
        return False

    def _captura_diagonal(self, from_row, from_col, to_row, to_col, direccion, board):
        return (abs(from_col - to_col) == 1 and 
                to_row == from_row + direccion and 
                board.get_piece(to_row, to_col) is not None and 
                board.get_piece(to_row, to_col).get_color() != self.get_color())
