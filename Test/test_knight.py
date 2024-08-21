import unittest
from Juego.Piezas.Knight import Knight

class TestKnight(unittest.TestCase):
    
    def setUp(self):
        self.caballo_blanco = Knight("blanco")
        self.caballo_negro = Knight("negro")
        
    def _test_movimiento(self, esperado, movimientos):
        for desde_fila, desde_columna, hasta_fila, hasta_columna in movimientos:
            with self.subTest(desde_fila=desde_fila, desde_columna=desde_columna, hasta_fila=hasta_fila, hasta_columna=hasta_columna):
                self.assertEqual(
                    self.caballo_blanco.movimiento_correcto(desde_fila, desde_columna, hasta_fila, hasta_columna), 
                    esperado
                )
                self.assertEqual(
                    self.caballo_negro.movimiento_correcto(desde_fila, desde_columna, hasta_fila, hasta_columna), 
                    esperado
                )
    
    def test_movimiento_correcto_en_L(self):
        movimientos_validos = [
            (0, 0, 2, 1), 
            (0, 0, 1, 2), 
            (4, 4, 6, 5), 
            (4, 4, 5, 6)
        ]
        self._test_movimiento(True, movimientos_validos)

    def test_movimiento_incorrecto(self):
        movimientos_invalidos = [
            (0, 0, 3, 3), 
            (0, 0, 0, 0), 
            (4, 4, 7, 4), 
            (4, 4, 4, 7)
        ]
        self._test_movimiento(False, movimientos_invalidos)

if __name__ == "__main__":
    unittest.main()
