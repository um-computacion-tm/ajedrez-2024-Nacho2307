import unittest
from main import suma, resta

class TestFunciones(unittest.TestCase):
    def funcion_verificar(self, funcion, casos):
        for a, b, resultado in casos:
            with self.subTest(a=a, b=b, resultado=resultado):
                self.assertEqual(funcion(a, b), resultado)
    def test_suma(self):
        casos_suma = [
            (5, 4, 9),
            (-1, 1, 0)
        ]
        self.funcion_verificar(suma, casos_suma)
    def test_resta(self):
        casos_resta = [
            (5, 4, 1),
            (-1, 1, -2)
        ]
        self.funcion_verificar(resta, casos_resta)

if __name__ == "__main__":
    unittest.main()
    