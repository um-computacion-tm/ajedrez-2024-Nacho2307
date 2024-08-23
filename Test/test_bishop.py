import unittest
from Juego.Piezas.Bishop import Bishop


class TestBishop(unittest.TestCase):
    def setUp(self):
        self.__bishop_white__ = Bishop("White")
    
    def check_moves(self, expected_result, moves):
        for from_row, from_col, to_row, to_col in moves:
            with self.subTest(from_pos=(from_row, from_col), to_pos=(to_row, to_col)):
                 self.assertEqual(self.__bishop_white__.movimiento_correcto(from_row, from_col, to_row, to_col), expected_result)
    
    def get_moves(self):
        return [
            (True, 1, 1, 4, 4),
            (True, 3, 5, 5, 3),
            (False, 1, 1, 4, 3),
            (False, 3, 5, 4, 5)
        ]
    def test_moves(self):
        self.check_moves(self.get_moves())

if __name__ == "__main__":
    unittest.main()
