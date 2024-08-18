import unittest
from Juego.Piezas.Bishop import Bishop

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.__bishop_white__ = Bishop("White")
    
    def _test_move_diagonal(self, from_row, from_col, to_row, to_col, resultado_esperado):
     self.assertEqual(self.__bishop_white__.movimiento_correcto(from_row, from_col, to_row, to_col), expected_result)
    
    def test_move_diagonal_valido(self):
     self._test_move_diagonal(1, 1, 4, 4, True)
     self._test_move_diagonal(3, 5, 5, 3, True)
    
    def test_move_diagonal_invalido(self):
     self._test_move_diagonal(1, 1, 4, 3, False)
     self._test_move_diagonal(3, 5, 4, 5, False)
    
    def test_move_nulo(self):
        self.assertFalse(self.__bishop_white__.movimiento_correcto(4, 4, 4, 4))

if __name__ == "__main__":
    unittest.main()    
        