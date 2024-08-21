import unittest
from Juego.Piezas.Knight import Knight

class TestKnight(unittest.TestCase):
    
    def setUp(self):
        self.caballo_blanco = Knight("blanco")
        self.caballo_negro = Knight("negro")
        
    def _test_movimientos(self, pieza, movimientos_correctos, movimientos_incorrectos):
        # Pruebas de movimientos correctos
        for desde_fila, desde_columna, hasta_fila, hasta_columna in movimientos_correctos:
            with self.subTest(tipo="correcto", desde_fila=desde_fila, desde_columna=desde_columna, hasta_fila=hasta_fila, hasta_columna=hasta_columna):
                self.assertTrue(pieza.movimiento_correcto(desde_fila, desde_columna, hasta_fila, hasta_columna))

        # Pruebas de movimientos incorrectos
        for desde_fila, desde_columna, hasta_fila, hasta_columna in movimientos_incorrectos:
            with self.subTest(tipo="incorrecto", desde_fila=desde_fila, desde_columna=desde_columna, hasta_fila=hasta_fila, hasta_columna=hasta_columna):
                self.assertFalse(pieza.movimiento_correcto(desde_fila, desde_columna, hasta_fila, hasta_columna))
    
    def test_movimientos_caballo(self):
        movimientos_correctos = [
            (0, 0, 2, 1), 
            (0, 0, 1, 2), 
            (4, 4, 6, 5), 
            (4, 4, 5, 6)
        ]

        movimientos_incorrectos = [
            (0, 0, 3, 3), 
            (0, 0, 0, 0), 
            (4, 4, 7, 4), 
            (4, 4, 4, 7)
        ]

        self._test_movimientos(self.caballo_blanco, movimientos_correctos, movimientos_incorrectos)
        self._test_movimientos(self.caballo_negro, movimientos_correctos, movimientos_incorrectos)

if __name__ == "__main__":
    unittest.main()