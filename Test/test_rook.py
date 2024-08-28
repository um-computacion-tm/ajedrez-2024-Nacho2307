import unittest
from Juego.Piezas.Rook import Rook
from Juego.board import Board

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()  # Crea una instancia del tablero
        self.rook = Rook('white')  # Crea una torre blanca

    def colocar_obstaculo(self, row, col, pieza='black'):
        # Coloca una pieza en una posición específica del tablero.
        self.board.set_piece(row, col, Rook(pieza))

    def verificar_movimiento(self, from_pos, to_pos, esperado, mensaje):
        # Método auxiliar para verificar movimientos.
        self.assertEqual(self.rook.movimiento_correcto(from_pos, to_pos, self.board), esperado, mensaje)

    def test_movimiento_correcto_horizontal_vacio(self):
        # Prueba el movimiento horizontal cuando el tablero está vacío.
        self.verificar_movimiento((0, 0), (0, 7), False, "El movimiento horizontal vacío debería ser incorrecto.")

    def test_movimiento_correcto_vertical_vacio(self):
        # Prueba el movimiento vertical cuando el tablero está vacío.
        self.verificar_movimiento((0, 0), (7, 0), False, "El movimiento vertical vacío debería ser incorrecto.")

    def test_movimiento_incorrecto_diagonal(self):
        # Prueba que el movimiento diagonal no es permitido para la torre.
        self.verificar_movimiento((0, 0), (7, 7), False, "El movimiento diagonal no debería ser permitido.")

    def test_movimiento_correcto_misma_posicion(self):
        # Prueba el movimiento a la misma posición.
        self.verificar_movimiento((0, 0), (0, 0), True, "El movimiento a la misma posición debería ser permitido.")

    def test_movimiento_correcto_horizontal_obstaculo(self):
        # Prueba el movimiento horizontal con un obstáculo en el camino.
        self.colocar_obstaculo(0, 5)
        self.verificar_movimiento((0, 0), (0, 7), False, "El movimiento horizontal con obstáculo no debería ser permitido.")

    def test_movimiento_correcto_vertical_obstaculo(self):
        # Prueba el movimiento vertical con un obstáculo en el camino.
        self.colocar_obstaculo(5, 0)
        self.verificar_movimiento((0, 0), (7, 0), False, "El movimiento vertical con obstáculo no debería ser permitido.")
