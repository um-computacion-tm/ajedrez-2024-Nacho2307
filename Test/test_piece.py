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
        self.assertEqual(self.piece.get_color(), "White")
        self.assertEqual(self.piece.get_x(), 0)
        self.assertEqual(self.piece.get_y(), 0)
        self.assertEqual(str(self.piece), 'T')

    def test_dentro_de_limites(self):
        # Lista de casos de prueba para dentro_de_limites
        casos = [
            ((0, 0), (7, 7), True),  # Dentro de los límites
            ((0, 0), (8, 8), False), # Fuera de los límites
            ((-1, 0), (7, 7), False),# Fila negativa
            ((0, -1), (7, 7), False),# Columna negativa
            ((0, 0), (7, 8), False), # Columna fuera de rango
            ((0, 0), (8, 7), False)  # Fila fuera de rango
        ]
        
        for from_pos, to_pos, expected in casos:
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self.assertEqual(Piece.dentro_de_limites(from_pos, to_pos), expected)

    def test_check_move(self):
        # Prueba movimientos dentro y fuera de los límites para check_move
        board = None 
        # Caso dentro de los límites
        self.assertTrue(self.piece.check_move(board, (0, 0), (1, 1)))
        
        # Caso fuera de los límites
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

if __name__ == '__main__':
    unittest.main()
