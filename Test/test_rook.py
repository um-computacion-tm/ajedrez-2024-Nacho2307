import unittest
from Juego.Piezas.Rook import Rook
from Juego.board import Board

class TestRook(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.clear_board()
        self.rook = Rook('white', 0, 0)
        self.board.place_piece(self.rook, (0, 0))

    def assert_move(self, from_pos, to_pos, should_move):
        result = self.rook.movimiento_correcto(from_pos[0], from_pos[1], to_pos[0], to_pos[1], self.board)
        self.assertEqual(result, should_move)

    def test_movimiento_correcto_horizontal(self):
        self.assert_move((0, 0), (0, 5), True)

    def test_movimiento_correcto_vertical(self):
        self.assert_move((0, 0), (5, 0), True)

    def test_movimiento_invalido_fuera_de_limites(self):
        self.assert_move((0, 0), (0, 8), False)

    def test_movimiento_invalido_diagonal(self):
        self.assert_move((0, 0), (3, 3), False)

    def test_movimiento_obstruido_horizontal(self):
        self._test_movimiento_obstruido((0, 3), (0, 0), (0, 5), False)

    def test_movimiento_obstruido_vertical(self):
        self._test_movimiento_obstruido((3, 0), (0, 0), (5, 0), False)

    def _test_movimiento_obstruido(self, obstruccion_pos, from_pos, to_pos, should_move):
        self.board.place_piece(Rook('black', obstruccion_pos[0], obstruccion_pos[1]), obstruccion_pos)
        self.assert_move(from_pos, to_pos, should_move)

if __name__ == "__main__":
    unittest.main()
