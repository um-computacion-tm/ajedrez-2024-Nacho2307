import unittest
from Juego.Piezas.Rook import Rook
from Juego.board import Board

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()  # Crea una instancia del tablero
        self.rook = Rook('white')  # Crea una torre blanca

    def colocar_obstaculo(self, row, col, pieza='black'):
        """Coloca una pieza en una posición específica del tablero."""
        self.board.set_piece(row, col, Rook(pieza))

    def test_movimiento_correcto_horizontal_vacio(self):
        """Prueba el movimiento horizontal cuando el tablero está vacío."""
        self.assertFalse(self.rook.movimiento_correcto(0, 0, 0, 7, self.board))

    def test_movimiento_correcto_vertical_vacio(self):
        """Prueba el movimiento vertical cuando el tablero está vacío."""
        self.assertFalse(self.rook.movimiento_correcto(0, 0, 7, 0, self.board))

    def test_movimiento_incorrecto_diagonal(self):
        """Prueba que el movimiento diagonal no es permitido para la torre."""
        self.assertFalse(self.rook.movimiento_correcto(0, 0, 7, 7, self.board))

    def test_movimiento_correcto_horizontal_obstaculo(self):
        """Prueba el movimiento horizontal con un obstáculo en el camino."""
        self.colocar_obstaculo(0, 5)
        self.assertFalse(self.rook.movimiento_correcto(0, 0, 0, 7, self.board))

    def test_movimiento_correcto_vertical_obstaculo(self):
        """Prueba el movimiento vertical con un obstáculo en el camino."""
        self.colocar_obstaculo(5, 0)
        self.assertFalse(self.rook.movimiento_correcto(0, 0, 7, 0, self.board))

    def test_movimiento_correcto_misma_posicion(self):
        """Prueba el movimiento a la misma posición."""
        self.assertTrue(self.rook.movimiento_correcto(0, 0, 0, 0, self.board))

    def test_movimiento_incorrecto_fuera_de_los_limites(self):
        """Prueba los movimientos fuera de los límites del tablero."""
        self.assertFalse(self.rook.movimiento_correcto(0, 0, 8, 0, self.board))
        self.assertFalse(self.rook.movimiento_correcto(0, 0, 0, 8, self.board))
        self.assertFalse(self.rook.movimiento_correcto(0, 0, -1, 0, self.board))
        self.assertFalse(self.rook.movimiento_correcto(0, 0, 0, -1, self.board))

if __name__ == '__main__':
    unittest.main()
