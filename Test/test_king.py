import unittest
from Juego.Piezas.King import King


class TestRey(unittest.TestCase):
    def setUp(self):
        self.__rey__ = King("white")
    
    def verificar_posicion(self, x, y):
        self.assertEqual(self.__rey__.get_x(), x)
        self.assertEqual(self.__rey__.get_y(), y)
    
    def test_incio(self):
        # Verifica el color y simbolo
     self.assertEqual(self.__rey__.get_color(), "White")
     self.assertEqual(str(self.__rey__), '♔')
    
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
