import unittest
from Juego.Piezas.king import King
from Juego.board import Board
from Juego.exception import InvalidMoveException

class TestRey(unittest.TestCase):
    """
    Clase de pruebas para la pieza Rey en el juego de ajedrez.
    Verifica que los movimientos del rey se comporten según las reglas del juego.
    """

    def setUp(self):
        """Inicializa el tablero y coloca el rey en la posición (0, 0)."""
        self.board = Board()
        self.__rey__ = King("white", 0, 0)
        self.board.__clear_board__()
        self.board.__set_piece__(0, 0, self.__rey__)

    @staticmethod
    def validar_movimiento_correcto(pieza, inicio, destino, board, esperado):
        """Valida si el movimiento del rey es correcto según las expectativas."""
        resultado = pieza.__movimiento_correcto__(inicio[0], inicio[1], destino[0], destino[1], board)
        assert resultado == esperado, (
            f"Error: {pieza.__class__.__name__} debería retornar {esperado} "
            f"para movimiento de {inicio} a {destino}, pero retornó {resultado}."
        )

    def test_incio(self):
        """Verifica el color y símbolo del rey."""
        self.assertEqual(self.__rey__.__get_color__(), "White")
        self.assertEqual(str(self.__rey__), '♔')

    def test_mover_valido(self):
        """Verifica que el rey se mueva a una posición válida."""
        self.__rey__.__mover__(1, 1)
        self.assertEqual(self.__rey__.__get_position__(), (1, 1))

    def test_mover_invalido(self):
        """Verifica que intentar mover el rey a una posición inválida lance una excepción."""
        with self.assertRaises(InvalidMoveException):
            self.__rey__.__mover__(3, 3)
        self.assertEqual(self.__rey__.__get_position__(), (0, 0))

    def test_mismo_lugar(self):
        """Verifica que el rey permanezca en la misma posición si se mueve a su lugar actual."""
        self.__rey__.__mover__(0, 0)
        self.assertEqual(self.__rey__.__get_position__(), (0, 0))

    def test_movimiento_correcto(self):
        """Verifica que el rey realice movimientos correctos según las reglas."""
        movimientos = {
            (0, 0): [((1, 1), True), ((2, 2), False)]  # Lista de tuplas (destino, esperado)
        }
        for inicio, destinos in movimientos.items():
            for destino, esperado in destinos:
                self.validar_movimiento_correcto(self.__rey__, inicio, destino, self.board, esperado)

    def test_movimiento_casilla_ocupada(self):
        """Verifica que el rey no pueda moverse a una casilla ocupada por su propia pieza."""
        otra_pieza = King("white", 1, 1)
        self.board.__set_piece__(1, 1, otra_pieza)
        self.assertFalse(self.__rey__.__movimiento_correcto__(0, 0, 1, 1, self.board))

if __name__ == "__main__":
    unittest.main()
