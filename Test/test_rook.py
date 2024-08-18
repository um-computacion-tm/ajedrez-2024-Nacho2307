import unittest
from Juego.Piezas.Rook import Rook

class TestRook(unittest.TestCase):
    # Método de ayuda para probar el movimiento de Rook
    def _test_rook_movimiento(self, x1, y1, x2, y2, resultado_esperado):
        # Crea un objeto rook con color "white"
        rook = Rook("white")
        resultado = rook.movimiento_correcto(x1, y1, x2, y2)
        # Comprueba si el resultado es verdadero o falso
        if resultado_esperado:
            self.assertTrue(resultado)
        else:
            self.assertFalse(resultado)
    
    def test_movimiento_valido_horizontal(self):
        self._test_rook_movimiento(0, 0, 0, 3, True) # Movimiento Horizontal
    
    def test_movimiento_valido_vertical(self):
        self._test_rook_movimiento(0, 0, 3, 0, True) # Movimiento Vertical

    def test_movimiento_incorrecto_diagonal(self):
        self._test_rook_movimiento(0, 0, 3, 3, False) # Movimiento Diagonal
    
    def test_movimiento_incorrecto_no_recto(self):
        self._test_rook_movimiento(0, 0, 2, 2, False) # Movimiento no recto

if __name__ == "__main__":
    unittest.main()
