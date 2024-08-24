import unittest
from Juego.Piezas.Piece import Piece

class TestPiece(unittest.TestCase):
    def setUp(self):
        self.__piece_dato__ =  [
            ('White', 'Pawn', '♙'),
            ('Black', 'Pawn', '♟'),
            ('White', 'Rook', '♖'),
            ('Black', 'Rook', '♜'),
            ('White', 'Knight', '♘'),
            ('Black', 'Knight', '♞'),
            ('White', 'Bishop', '♗'),
            ('Black', 'Bishop', '♝'),
            ('White', 'Queen', '♕'),
            ('Black', 'Queen', '♛'),
            ('White', 'King', '♔'),
            ('Black', 'King', '♚')
        ]
        
    def test_piece_creacion_de_symbol(self):
        for color, nombre, simbolo_esperado in self.__piece_dato__:
            with self.subTest(color = color, nombre = nombre):
                piece = Piece(color, nombre)
                self.assertEqual(str(piece), simbolo_esperado)
    
    def test_move_invalido(self):
        piece = Piece("White", "Pawn")
        self.assertFalse(piece.movimiento_correcto(0, 0, 7, 7))

if __name__ == '__main__':
    unittest.main()
    
    