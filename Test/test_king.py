import unittest
from Juego.Piezas.King import King


class TestRey(unittest.TestCase):
    def setUp(self):
        self.__rey__ = King("White")
    
    def verificar_posicion(self, x, y):
        self.assertEqual(self.__rey__.__x__, x)
        self.assertEqual(self.__rey__.__y__, y)
    
    def test_incio(self):
     self.assertEqual(self.__rey__.__color__, "White")
     self.assertEqual(self.__rey__.__simbolo__, "♚")
    
    def test_mover_valido(self):
        self.__rey__.mover(1, 1)
        self.verificar_posicion(1, 1)
        
    def test_mover_invalido(self):
        self.__rey__.mover(3, 3)
        self.verificar_posicion(0, 0)
        
    def test_mismo_lugar(self):
        self.__rey__.mover(0 ,0)
        self.verificar_posicion(0, 0)
        
if __name__ == "__main__":
    unittest.main()
