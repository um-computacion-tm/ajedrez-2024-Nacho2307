import unittest
from Juego.Piezas.Rook import Rook
from Juego.board import Board

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board.__clear_board__()
        self.rook = Rook("white", 7, 0)
        self.board.__set_piece__(7, 0, self.rook)

    def _validate_move(self, from_pos, to_pos, expected_result):
        origen_x, origen_y = from_pos
        destino_x, destino_y = to_pos

        movimiento_valido = self.rook.__movimiento_correcto__(origen_x, origen_y, destino_x, destino_y, self.board)

        self.assertEqual(movimiento_valido, expected_result)

    def _setup_blocking_piece(self, pos, color):
        self.board.__set_piece__(pos[0], pos[1], Rook(color))

    def _test_moves(self, moves, expected_result, setup_func=None):
        for from_pos, to_pos in moves:
            if setup_func:
                setup_func(from_pos)
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self._validate_move(from_pos, to_pos, expected_result)

    def _setup_blocking(self, blocked_pos, color, description):
        def setup_func(pos):
            self._setup_blocking_piece(blocked_pos, color)

        return setup_func, description

    def test_valid_moves(self):
        movimientos_validos = self._generate_valid_moves()
    
        # Validamos todos los movimientos correctos
        self._test_moves(movimientos_validos, True)

    def _generate_valid_moves(self):
        return [
            ((7, 0), (5, 0)),  # Movimiento hacia adelante
            ((7, 0), (7, 7)),  # Movimiento lateral
        ]

    def test_invalid_moves(self):
        movimientos_invalidos = [
            ((7, 0), (6, 1)),  # Movimiento diagonal inválido
            ((7, 0), (5, 1)),  # Movimiento en L inválido
        ]
    
        # Validamos los movimientos incorrectos
        for from_pos, to_pos in movimientos_invalidos:
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self._validate_move(from_pos, to_pos, False)

    def test_move_out_of_bounds(self):
        out_of_bounds_moves = [
            ((7, 0), (8, 0)),
            ((7, 0), (7, 8)),
            ((0, 0), (-1, 0)),
            ((0, 0), (0, -1)),
        ]
        self._test_moves(out_of_bounds_moves, False)

    def test_path_is_blocked(self):
        movimientos = [((7, 0), (5, 0))]  # Movimiento bloqueado hacia adelante
        self._test_moves(movimientos, False, lambda pos: self._setup_blocking_piece((6, 0), "black"))

    def test_capture_same_color(self):
        def setup_func(pos):
            self._setup_blocking_piece((5, 0), "white")

        movimientos = [((7, 0), (5, 0))]  
        self._test_moves(movimientos, False, setup_func)

    def test_path_is_blocked_horizontal(self):
        setup_func, _ = self._setup_blocking((7, 4), "black", "Movimiento bloqueado hacia la derecha")
        movimientos = [((7, 0), (7, 5))]
        self._test_moves(movimientos, False, setup_func)

if __name__ == '__main__':
    unittest.main()
