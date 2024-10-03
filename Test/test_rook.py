import unittest
from Juego.Piezas.Rook import Rook
from Juego.board import Board

class TestRook(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.board.__clear_board__()  # Limpiar el tablero antes de cada prueba
        self.rook = Rook("white", 7, 0)  # Torre blanca en su posición inicial
        self.board.__set_piece__(7, 0, self.rook)

    # Método que realiza la validación del movimiento correcto o incorrecto
    def _validate_move(self, from_pos, to_pos, expected_result):
        result = self.rook.__movimiento_correcto__(from_pos[0], from_pos[1], to_pos[0], to_pos[1], self.board)
        self.assertEqual(result, expected_result)

    def _setup_blocking_piece(self, pos, color):
        # Coloca una pieza en la posición especificada para bloquear el movimiento.
        self.board.__set_piece__(pos[0], pos[1], Rook(color))

    def _test_moves(self, moves, expected_result, setup_func=None):
        for from_pos, to_pos in moves:
            if setup_func:
                setup_func(from_pos)
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self._validate_move(from_pos, to_pos, expected_result)

    def _setup_blocking(self, blocked_pos, color, description):
        # Método genérico para configurar una pieza que bloquea en una posición.
        def setup_func(pos):
            self._setup_blocking_piece(blocked_pos, color)

        return setup_func, description

    def test_valid_moves(self):
        valid_moves = [
            ((7, 0), (5, 0)),  # Movimiento hacia adelante
            ((7, 0), (7, 7)),  # Movimiento lateral
        ]
        # Validamos todos los movimientos correctos
        self._test_moves(valid_moves, True)

    def test_invalid_moves(self):
        invalid_moves = [
            ((7, 0), (6, 1)),  # Movimiento diagonal inválido
            ((7, 0), (5, 1)),  # Movimiento en L inválido
        ]
        # Validamos todos los movimientos incorrectos
        self._test_moves(invalid_moves, False)

    def test_move_out_of_bounds(self):
        out_of_bounds_moves = [
            ((7, 0), (8, 0)),  # Movimiento fuera del límite inferior
            ((7, 0), (7, 8)),  # Movimiento fuera del límite derecho
            ((0, 0), (-1, 0)),  # Movimiento fuera del límite superior
            ((0, 0), (0, -1)),  # Movimiento fuera del límite izquierdo
        ]
        self._test_moves(out_of_bounds_moves, False)

    def test_path_is_blocked(self):
        setup_func, _ = self._setup_blocking((6, 0), "black", "Movimiento bloqueado hacia adelante")
        movimientos = [((7, 0), (5, 0))]
        self._test_moves(movimientos, False, setup_func)

    def test_capture_same_color(self):
        setup_func, _ = self._setup_blocking((5, 0), "white", "No debería permitir capturar la misma color")
        movimientos = [((7, 0), (5, 0))]
        self._test_moves(movimientos, False, setup_func)

    def test_path_is_blocked_horizontal(self):
        setup_func, _ = self._setup_blocking((7, 4), "black", "Movimiento bloqueado hacia la derecha")
        movimientos = [((7, 0), (7, 5))]
        self._test_moves(movimientos, False, setup_func)

if __name__ == '__main__':
    unittest.main()
