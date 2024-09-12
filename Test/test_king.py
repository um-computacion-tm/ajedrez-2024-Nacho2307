import unittest
from Juego.Piezas.King import King
from Juego.Exception import InvalidMoveException

class TestRey(unittest.TestCase):
    def setUp(self):
        self.__rey__ = King("white")
    
    def verificar_posicion(self, x, y):
        self.assertEqual(self.__rey__.get_position(), (x, y))
    
    def test_incio(self):
        # Verifica el color y simbolo
        self.assertEqual(self.__rey__.get_color(), "White")
        self.assertEqual(str(self.__rey__), '♔')
    
    def test_mover_valido(self):
        self.__rey__.mover(1, 1)
        self.verificar_posicion(1, 1)

    def test_mover_invalido(self):
        with self.assertRaises(InvalidMoveException):
            self.__rey__.mover(3, 3)
        self.verificar_posicion(0, 0)

    def test_mismo_lugar(self):
        self.__rey__.mover(0, 0)
        self.verificar_posicion(0, 0)
    
    def test_movimiento_correcto(self):
        # Simular un tablero (utiliza un mock o crea un tablero ficticio para esta prueba)
        board = MockBoard()  
        self.assertTrue(self.__rey__.movimiento_correcto(0, 0, 1, 1, board))
        self.assertFalse(self.__rey__.movimiento_correcto(0, 0, 2, 2, board))

class MockBoard:
    def get_piece(self, row, col):
        # Simular que la casilla está vacía
        return None

if __name__ == "__main__":
    unittest.main()