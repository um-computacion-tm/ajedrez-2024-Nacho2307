import unittest
from Juego.Piezas.Bishop import Bishop

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.__bishop_white__ = Bishop("White")
    
    def test_move_diagonal_valido(self):
        self.assertTrue(self.__bishop_white__.movimiento_correcto(1, 1, 4, 4))
        self.assertTrue(self.__bishop_white__.movimiento_correcto(3, 5, 5, 3))
    
    def test_move_diagonal_invalido(self):
        self.assertFalse(self.__bishop_white__.movimiento_correcto(1, 1, 4, 3))
        self.assertFalse(self.__bishop_white__.movimiento_correcto(3, 5, 4, 5))
    
    def test_move_nulo(self):
        self.assertFalse(self.__bishop_white__.movimiento_correcto(4, 4, 4, 4))

if __name__ == "__main__":
    unittest.main()    
        