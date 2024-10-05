import unittest
from Juego.Piezas.piece import Piece

# Función auxiliar para probar los límites
def test_dentro_de_limites(self, piece_class):
    casos = [
        ((0, 0), (7, 7), True),  # Caso válido
        ((0, 0), (8, 8), False),  # Fuera de límites
        ((-1, 0), (7, 7), False),  # Fuera de límites
        ((0, -1), (7, 7), False),  # Fuera de límites
        ((0, 0), (7, 8), False),  # Fuera de límites
        ((0, 0), (8, 7), False)   # Fuera de límites
    ]
    
    for from_pos, to_pos, expected in casos:
        with self.subTest(from_pos=from_pos, to_pos=to_pos):
            resultado = piece_class.__dentro_de_limites__(from_pos, to_pos)
            self.assertEqual(resultado, expected)

# Función auxiliar para probar el movimiento correcto
def test_movimiento_correcto(self, piece, movimientos):
    for from_row, from_col, to_row, to_col, expected in movimientos:
        with self.subTest(from_row=from_row, to_col=to_col):
            self.assertEqual(piece.__movimiento_correcto__(from_row, from_col, to_row, to_col, None), expected)

# Clase de prueba personalizada para la pieza de prueba
class TestPiece(Piece):
    def __init__(self, color, x=0, y=0):
        super().__init__(color, "TestPiece", x, y)
        self.__simbolo__ = 'T'

    def __movimiento_posible__(self, from_row, from_col, board):
        return True

    def __movimiento_correcto__(self, from_row, from_col, to_row, to_col, board):
        return from_row != to_row or from_col != to_col

# Clase de pruebas para los métodos de TestPiece
class TestPieceMethods(unittest.TestCase):
    def setUp(self):
        self.piece = TestPiece("white", 0, 0)

    def test_initialization(self):
        self.assertEqual(self.piece.__get_color__(), "White")
        self.assertEqual(self.piece.__get_x__(), 0)
        self.assertEqual(self.piece.__get_y__(), 0)
        self.assertEqual(str(self.piece), 'T')

    def test_dentro_de_limites(self):
        # Usamos la función auxiliar para evitar duplicación
        test_dentro_de_limites(self, Piece)

    def test_check_move(self):
        movimientos = [
            ((0, 0), (1, 1), True),
            ((0, 0), (8, 8), False),  # Fuera de límites
            ((-1, 0), (0, 0), False),  # Fuera de límites
            ((0, 0), (7, 8), False)    # Fuera de límites
        ]
        for from_pos, to_pos, expected in movimientos:
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self.assertEqual(self.piece.__check_move__(None, from_pos, to_pos), expected)

    def test_get_coordinates(self):
        self.assertEqual(self.piece.__get_coordinates__((1, 1)), (1, 1, 0, 0))

    def test_movimiento_posible(self):
        self.assertTrue(self.piece.__movimiento_posible__(0, 0, None))

    def test_movimiento_correcto(self):
        # Usamos la función auxiliar para probar múltiples casos de movimiento correcto
        movimientos = [
            (0, 0, 1, 1, True),
            (0, 0, 0, 0, False)
        ]
        test_movimiento_correcto(self, self.piece, movimientos)

    def test_possible_moves_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.piece.__possible_moves__(None)

    def test_movimiento_posible_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            super(TestPiece, self.piece).__movimiento_posible__(0, 0, None)

    def test_movimiento_correcto_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            super(TestPiece, self.piece).__movimiento_correcto__(0, 0, 1, 1, None)

    def test_get_position(self):
        self.assertEqual(self.piece.__get_position__(), (0, 0))

if __name__ == '__main__':
    unittest.main()
