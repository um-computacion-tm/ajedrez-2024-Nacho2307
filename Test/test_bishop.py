import unittest
from Juego.Piezas.Bishop import Bishop

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.__bishop_white__ = Bishop("White")
    
    def test_move_diagonal_valido(self):
        for from_row, from_col, to_row, to_col in [(1, 1, 4, 4), (3, 5, 5, 3)]:
            self.assertTrue(self.__bishop_white__.movimiento_correcto(from_row, from_col, to_row, to_col))
    
    def test_move_diagonal_invalido(self):
        for from_row, from_col, to_row, to_col in [(1, 1, 4, 3), (3, 5, 4, 5)]:
            self.assertFalse(self.__bishop_white__.movimiento_correcto(from_row, from_col, to_row, to_col))
    
    def test_move_nulo(self):
        self.assertFalse(self.__bishop_white__.movimiento_correcto(4, 4, 4, 4))

if __name__ == "__main__":
    unittest.main()
