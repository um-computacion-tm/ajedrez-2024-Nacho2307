import unittest
from Juego.Piezas.Knight import Knight

class TestKnight(unittest.TestCase):
    
    def setUp(self):
        # Configuración común para todas las pruebas
        self.caballo_blanco = Knight("blanco")
        self.caballo_negro = Knight("negro")
    
    def test_movimiento_correcto_en_L(self):
        # Movimientos válidos en "L"
        self.assertTrue(self.caballo_blanco.movimiento_correcto(0, 0, 2, 1))
        self.assertTrue(self.caballo_blanco.movimiento_correcto(0, 0, 1, 2))
        self.assertTrue(self.caballo_negro.movimiento_correcto(4, 4, 6, 5))
        self.assertTrue(self.caballo_negro.movimiento_correcto(4, 4, 5, 6))
    
    def test_movimiento_incorrecto(self):
        # Movimientos inválidos
        self.assertFalse(self.caballo_blanco.movimiento_correcto(0, 0, 3, 3))
        self.assertFalse(self.caballo_blanco.movimiento_correcto(0, 0, 0, 0))
        self.assertFalse(self.caballo_negro.movimiento_correcto(4, 4, 7, 4))
        self.assertFalse(self.caballo_negro.movimiento_correcto(4, 4, 4, 7))

if __name__ == "__main__":
    unittest.main()
