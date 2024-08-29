import unittest
from Juego.Piezas.Rook import Rook
from Juego.board import Board

class TestRook(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.clear_board()  
        self.rook = Rook('white', 0, 0)
        self.board.place_piece(self.rook, (0, 0))

    def _test_movimiento_valido(self, from_pos, to_pos):
        self.assertTrue(self.rook.movimiento_correcto(from_pos, to_pos, self.board))

    def test_movimiento_correcto_horizontal(self):
        self._test_movimiento_valido((0, 0), (0, 5))

    def test_movimiento_correcto_vertical(self):
        self._test_movimiento_valido((0, 0), (5, 0))

    def test_movimiento_invalido_fuera_de_limites(self):
        self._test_movimiento_invalido((0, 0), (0, 8))

    def test_movimiento_invalido_diagonal(self):
        self._test_movimiento_invalido((0, 0), (3, 3))

    def test_movimiento_obstruido_horizontal(self):
        self.board.set_piece(0, 3, Rook('black', 0, 3))
        self._test_movimiento_invalido((0, 0), (0, 5))

    def test_movimiento_obstruido_vertical(self):
        self.board.set_piece(3, 0, Rook('black', 3, 0))
        self._test_movimiento_invalido((0, 0), (5, 0))

    def _test_movimiento_valido(self, from_pos, to_pos):
        self.assertTrue(self.rook.movimiento_correcto(from_pos, to_pos, self.board))

    def _test_movimiento_invalido(self, from_pos, to_pos):
        self.assertFalse(self.rook.movimiento_correcto(from_pos, to_pos, self.board))

if __name__ == "__main__":
    unittest.main()
