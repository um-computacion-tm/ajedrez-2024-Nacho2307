import unittest
from Juego.Piezas.Piece import Piece

class TestPiece(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, "TestPiece", x, y)
        self.__simbolo__ = 'T'

    def movimiento_posible(self, from_row, from_col, board):
        return True

    def movimiento_correcto(self, from_row, from_col, to_row, to_col, board):
        return from_row != to_row or from_col != to_col

class TestPieceMethods(unittest.TestCase):
    def setUp(self):
        self.piece = TestPiece("white", 0, 0)

    def test_initialization(self):
        self.assertEqual(self.piece.get_color(), "White")
        self.assertEqual(self.piece.get_x(), 0)
        self.assertEqual(self.piece.get_y(), 0)
        self.assertEqual(str(self.piece), 'T')

    def test_dentro_de_limites(self):
        casos = [
            ((0, 0), (7, 7), True),
            ((0, 0), (8, 8), False),
            ((-1, 0), (7, 7), False),
            ((0, -1), (7, 7), False),
            ((0, 0), (7, 8), False),
            ((0, 0), (8, 7), False)
        ]
        
        for from_pos, to_pos, expected in casos:
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self.assertEqual(Piece.dentro_de_limites(from_pos, to_pos), expected)

    def test_check_move(self):
        board = None
        self.assertTrue(self.piece.check_move(board, (0, 0), (1, 1)))
        self.assertFalse(self.piece.check_move(board, (0, 0), (8, 8)))
        self.assertFalse(self.piece.check_move(board, (-1, 0), (0, 0)))
        self.assertFalse(self.piece.check_move(board, (0, 0), (7, 8)))

    def test_get_coordinates(self):
        self.assertEqual(self.piece.get_coordinates((1, 1)), (1, 1, 0, 0))
    
    def test_movimiento_posible(self):
        self.assertTrue(self.piece.movimiento_posible(0, 0, None))
    
    def test_movimiento_correcto(self):
        self.assertTrue(self.piece.movimiento_correcto(0, 0, 1, 1, None))
        self.assertFalse(self.piece.movimiento_correcto(0, 0, 0, 0, None))
    
    def test_possible_moves_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.piece.possible_moves(None)

    def test_movimiento_posible_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            super(TestPiece, self.piece).movimiento_posible(0, 0, None)

    def test_movimiento_correcto_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            super(TestPiece, self.piece).movimiento_correcto(0, 0, 1, 1, None)

    def test_get_position(self):
        self.assertEqual(self.piece.get_position(), (0, 0))

if __name__ == '__main__':
    unittest.main()
