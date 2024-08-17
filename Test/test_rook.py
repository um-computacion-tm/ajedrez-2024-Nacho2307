import unittest
from Juego.Piezas.Rook import Rook


class TestRook(unittest.TestCase):
    def test_movimiento_valido_horizontal(self):
        rook = Rook("white")
        self.assertTrue(rook.movimiento_correcto(0, 0, 0, 3))  # movimiento horizontal

    def test_movimiento_valido_vertical(self):
        rook = Rook("white")
        self.assertTrue(rook.movimiento_correcto(0, 0, 3, 0))  # movimiento vertical

    def test_movimiento_incorrecto_diagonal(self):
        rook = Rook("white")
        self.assertFalse(rook.movimiento_correcto(0, 0, 3, 3))  # movimiento diagonal

    def test_movimiento_incorrecto_no_recto(self):
        rook = Rook("white")
        self.assertFalse(rook.movimiento_correcto(0, 0, 2, 2))  # movimiento no recto

if __name__ == "__main__":
    unittest.main()