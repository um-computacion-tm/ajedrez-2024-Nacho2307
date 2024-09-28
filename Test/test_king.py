import unittest
from Juego.Piezas.King import King
from Juego.board import Board
from Juego.Exception import InvalidMoveException

class TestRey(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.__rey__ = King("white", 0, 0)
        self.board.__clear_board__()
        self.board.__set_piece__(0, 0, self.__rey__)

    def verificar_posicion(self, x, y):
        self.assertEqual(self.__rey__.__get_position__(), (x, y))

    def test_incio(self):
        self.assertEqual(self.__rey__.__get_color__(), "White")
        self.assertEqual(str(self.__rey__), '♔')

    def test_mover_valido(self):
        self.__rey__.__mover__(1, 1)
        self.verificar_posicion(1, 1)

    def test_mover_invalido(self):
        with self.assertRaises(InvalidMoveException):
            self.__rey__.__mover__(3, 3)
        self.verificar_posicion(0, 0)

    def test_mismo_lugar(self):
        self.__rey__.__mover__(0, 0)
        self.verificar_posicion(0, 0)

    def test_movimiento_correcto(self):
        self.validar_movimiento_correcto(self.__rey__, (0, 0), (1, 1), True)
        self.validar_movimiento_correcto(self.__rey__, (0, 0), (2, 2), False)

    def validar_movimiento_correcto(self, pieza, inicio, destino, esperado):
        self.assertEqual(pieza.__movimiento_correcto__(inicio[0], inicio[1], destino[0], destino[1], self.board), esperado)

    def test_movimiento_casilla_ocupada(self):
        otra_pieza = King("white", 1, 1)
        self.board.__set_piece__(1, 1, otra_pieza)
        self.assertFalse(self.__rey__.__movimiento_correcto__(0, 0, 1, 1, self.board))

if __name__ == "__main__":
    unittest.main()
