from Juego.Piezas.Piece import Piece

class Rook(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color.lower(), 'Rook', x, y)
    
    def movimiento_correcto(self, from_row, from_col, to_row, to_col, board):
        # Verifica si las posiciones están dentro de los límites del tablero
        if not (0 <= from_row <= 7 and 0 <= from_col <= 7 and 0 <= to_row <= 7 and 0 <= to_col <= 7):
            return False
        
        # La torre se mueve en línea recta: o bien en la misma fila o en la misma columna
        if to_row == from_row or to_col == from_col:
            if to_row == from_row:
                # Movimiento horizontal
                paso = 1 if to_col > from_col else -1
                for col in range(from_col + paso, to_col, paso):
                    if board.get_piece(from_row, col) is not None:
                        return False
            else:
                # Movimiento vertical
                paso = 1 if to_row > from_row else -1
                for row in range(from_row + paso, to_row, paso):
                    if board.get_piece(row, from_col) is not None:
                        return False
            
            final_piece = board.get_piece(to_row, to_col)
            if final_piece is None or final_piece.get_color() != self.get_color():
                return True
        
        return False

