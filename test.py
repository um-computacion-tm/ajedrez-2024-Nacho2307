import unittest
from main import suma, resta
from util_pruebas import verificar_funcion

class TestFunciones(unittest.TestCase):
    def test_suma(self):
        casos_suma = [
            (5, 4, 9),
            (-1, 1, 0)
        ]
        verificar_funcion(self, suma, casos_suma)
    
    def test_resta(self):
        casos_resta = [
            (5, 4, 1),
            (-1, 1, -2)
        ]
        verificar_funcion(self, resta, casos_resta)

if __name__ == "__main__":
    unittest.main()
