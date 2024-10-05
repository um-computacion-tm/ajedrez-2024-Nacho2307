import unittest
from Juego.Piezas.queen import Queen
from Juego.board import Board

class TestQueen(unittest.TestCase):
    def setUp(self):
        self.__board__ = Board()
        self.__white_queen__ = Queen('white')
        self.__black_queen__ = Queen('black')
        self.__board__.__place_piece__(self.__white_queen__, (4, 4))
        self.__board__.__place_piece__(self.__black_queen__, (7, 4))

    @staticmethod
    def validar_movimiento_correcto(pieza, inicio, destino, board, esperado):
        resultado = pieza.__movimiento_correcto__(inicio[0], inicio[1], destino[0], destino[1], board)
        assert resultado == esperado, f"Se esperaba {esperado} pero se obtuvo {resultado}."

    def test_movimiento_correcto(self):
        # Remueve cualquier pieza que pueda bloquear el movimiento de la reina
        if self.__board__.__get_piece__(6, 4) is not None:
            self.__board__.__remove_piece__(6, 4)

        # Movimientos válidos para la reina.
        # Movimientos como torre
        self.assertTrue(self.__white_queen__.__movimiento_correcto__(4, 4, 4, 7, self.__board__))
        self.assertTrue(self.__black_queen__.__movimiento_correcto__(7, 4, 4, 4, self.__board__))

        # Movimientos como alfil
        self.assertFalse(self.__white_queen__.__movimiento_correcto__(4, 4, 7, 7, self.__board__))
        self.assertFalse(self.__black_queen__.__movimiento_correcto__(7, 4, 4, 7, self.__board__))

    def test_movimiento_incorrecto(self):
        self.validar_movimiento_correcto(self.__white_queen__, (4, 4), (5, 6), self.__board__, False)  # Movimiento diagonal inválido
        self.validar_movimiento_correcto(self.__black_queen__, (7, 4), (2, 5), self.__board__, False)  # Movimiento diagonal inválido

if __name__ == '__main__':
    unittest.main()


