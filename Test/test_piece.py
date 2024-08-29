import unittest
from Juego.Piezas.Piece import Piece

class TestPiece(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, "TestPiece", x, y)
        # Establece el símbolo manualmente para la pieza de prueba
        self.__simbolo__ = 'T'

    def movimiento_posible(self, from_row, from_col, board):
        # Implementación simple para pruebas
        return True

    def movimiento_correcto(self, from_row, from_col, to_row, to_col, board):
        # Implementación simple para pruebas
        return from_row != to_row or from_col != to_col

class TestPieceMethods(unittest.TestCase):
    def setUp(self):
        self.piece = TestPiece("white", 0, 0)
    
    def test_initialization(self):
        # Verifica la inicialización de la pieza
        self.assertEqual(self.piece.get_color(), "White")
        self.assertEqual(self.piece.get_x(), 0)
        self.assertEqual(self.piece.get_y(), 0)
        self.assertEqual(str(self.piece), 'T')  # Verifica el símbolo de la pieza para TestPiece
    
    def test_dentro_de_limites(self):
        # Prueba si el método dentro_de_limites funciona correctamente
        self.assertTrue(Piece.dentro_de_limites((0, 0), (7, 7)))
        self.assertFalse(Piece.dentro_de_limites((0, 0), (8, 8)))
    
    def test_get_coordinates(self):
        # Verifica el método get_coordinates
        self.assertEqual(self.piece.get_coordinates((1, 1)), (1, 1, 0, 0))
    
    def test_movimiento_posible(self):
        # Verifica el método movimiento_posible
        self.assertTrue(self.piece.movimiento_posible(0, 0, None))
    
    def test_movimiento_correcto(self):
        # Verifica el método movimiento_correcto
        self.assertTrue(self.piece.movimiento_correcto(0, 0, 1, 1, None))
        self.assertFalse(self.piece.movimiento_correcto(0, 0, 0, 0, None))

if __name__ == '__main__':
    unittest.main()
