import unittest
from Juego.Piezas.Knight import Knight

class TestKnight(unittest.TestCase):
    
    def setUp(self):
        self.caballo_blanco = Knight("white")
        self.caballo_negro = Knight("black")
        
    
    def _test_movimientos(self, pieza, movimientos, resultado_esperado):
        for desde_fila, desde_columna, hasta_fila, hasta_columna in movimientos:
            with self.subTest(desde_fila=desde_fila, desde_columna=desde_columna, hasta_fila=hasta_fila, hasta_columna=hasta_columna):
                self.assertEqual(pieza.movimiento_correcto(desde_fila, desde_columna, hasta_fila, hasta_columna), resultado_esperado)
    
    def _test_todos_los_movimientos(self, movimientos_correctos, movimientos_incorrectos):
        piezas = [self.caballo_blanco, self.caballo_negro]  # Lista de piezas definida aquí
        for pieza in piezas:  # Iterar sobre las piezas definidas
            self._test_movimientos(pieza, movimientos_correctos, True)
            self._test_movimientos(pieza, movimientos_incorrectos, False)
    
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

        self._test_todos_los_movimientos(movimientos_correctos, movimientos_incorrectos)

if __name__ == "__main__":
    unittest.main()