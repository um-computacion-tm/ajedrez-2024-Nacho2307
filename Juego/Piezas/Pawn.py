from Piezas.Piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, "Pawn", "♙" if color == "Black" else "♟")
