import unittest
from Juego.Piezas.Piece import Piece

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.__piece_dato__ =  [
            ('white', 'Pawn', '♙'),
            ('black', 'Pawn', '♟'),
            ('white', 'Rook', '♖'),
            ('black', 'Rook', '♜'),
            ('white', 'Knight', '♘'),
            ('black', 'Knight', '♞'),
            ('white', 'Bishop', '♗'),
            ('black', 'Bishop', '♝'),
            ('white', 'Queen', '♕'),
            ('black', 'Queen', '♛'),
            ('white', 'King', '♔'),
            ('black', 'King', '♚')
        ]
        
    def test_piece_creacion_de_symbol(self):
        for color, nombre, simbolo_esperado in self.__piece_dato__:
            with self.subTest(color = color, nombre = nombre):
                piece = Piece(color, nombre)
                self.assertEqual(str(piece), simbolo_esperado)
    
    def test_move_invalido(self):
        piece = Piece("white", "Pawn")
        self.assertFalse(piece.movimiento_correcto(0, 0, 7, 7))

if __name__ == '__main__':
    unittest.main()
    
    