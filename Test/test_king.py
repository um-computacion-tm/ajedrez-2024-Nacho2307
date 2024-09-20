import unittest
from Juego.Piezas.King import King
from Juego.board import Board
from Juego.Exception import InvalidMoveException

class TestRey(unittest.TestCase):
    def setUp(self):
        self.board = Board()  # Utiliza el tablero real
        self.__rey__ = King("white", 0, 0)
        self.board.clear_board()  # Limpia el tablero antes de cada prueba
        self.board.set_piece(0, 0, self.__rey__)  # Coloca al rey en la posición (0, 0)

    def verificar_posicion(self, x, y):
        self.assertEqual(self.__rey__.get_position(), (x, y))

    def test_incio(self):
        # Verifica el color y símbolo
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
        # Verifica un movimiento correcto
        self.assertTrue(self.__rey__.movimiento_correcto(0, 0, 1, 1, self.board))
        self.assertFalse(self.__rey__.movimiento_correcto(0, 0, 2, 2, self.board))

    def test_movimiento_casilla_ocupada(self):
        # Coloca una pieza del mismo color en la posición (1, 1) para verificar que el rey no puede moverse allí
        otra_pieza = King("white", 1, 1)
        self.board.set_piece(1, 1, otra_pieza)
        self.assertFalse(self.__rey__.movimiento_correcto(0, 0, 1, 1, self.board))  # No debe moverse a (1, 1)

if __name__ == "__main__":
    unittest.main()
