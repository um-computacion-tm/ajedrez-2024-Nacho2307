import unittest
from Juego.Piezas.Bishop import Bishop

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.__bishop_white__ = Bishop("White")
    
    def _test_move_diagonal(self, expected_result, moves):
        for from_row, from_col, to_row, to_col in moves:
            with self.subTest(from_pos=(from_row, from_col), to_pos=(to_row, to_col)):
                 self.assertEqual(self.__bishop_white__.movimiento_correcto(from_row, from_col, to_row, to_col), expected_result)
    
    def test_move_diagonal_valido(self):
        valido_move = [(1, 1, 4, 4), (3, 5, 5, 3)]
        self._test_move_diagonal(True, valido_move)
    
    def test_move_diagonal_invalido(self):
        invalido_move = [(1, 1, 4, 3), (3, 5, 4, 5)]
        self._test_move_diagonal(False, invalido_move)

if __name__ == "__main__":
    unittest.main()
