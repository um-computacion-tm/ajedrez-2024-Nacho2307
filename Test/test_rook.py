import unittest
from Juego.Piezas.rook import Rook
from Juego.board import Board

class TestRook(unittest.TestCase):
    """Clase de prueba para la pieza Torre en el juego de ajedrez."""

    def setUp(self):
        """Configura el tablero y coloca una torre blanca en la posición inicial."""
        self.board = Board()
        self.board.__clear_board__()
        self.rook = Rook("white", 7, 0)
        self.board.__set_piece__(7, 0, self.rook)

    def _validate_move(self, from_pos, to_pos, expected_result):
        """
        Valida si el movimiento de la torre desde la posición inicial a la destino es correcto.
        """
        origen_x, origen_y = from_pos
        destino_x, destino_y = to_pos

        movimiento_valido = self.rook.__movimiento_correcto__(origen_x, origen_y, destino_x, destino_y, self.board)
        self.assertEqual(movimiento_valido, expected_result)

    def _setup_blocking_piece(self, pos, color):
        """Coloca una pieza bloqueante en la posición especificada."""
        self.board.__set_piece__(pos[0], pos[1], Rook(color))

    def _setup_blocking(self, blocked_pos, color):
        """Configura una pieza bloqueante en el tablero."""
        self.board.__set_piece__(blocked_pos[0], blocked_pos[1], Rook(color))

    def _test_moves(self, moves, expected_result, setup_func=None):
        """
        Ejecuta pruebas de movimiento para una lista de movimientos.
        """
        for from_pos, to_pos in moves:
            if setup_func:
                setup_func(from_pos)
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self._validate_move(from_pos, to_pos, expected_result)

    def test_valid_moves(self):
        """Prueba que los movimientos válidos de la torre sean aceptados."""
        movimientos_validos = self._generate_valid_moves()
        self._test_moves(movimientos_validos, True)

    def _generate_valid_moves(self):
        """Genera movimientos válidos para la torre."""
        return [
            ((7, 0), (5, 0)),  # Movimiento hacia adelante
            ((7, 0), (7, 7)),  # Movimiento lateral
        ]

    def test_invalid_moves(self):
        """Prueba que los movimientos inválidos de la torre sean rechazados."""
        movimientos_invalidos = [
            ((7, 0), (6, 1)),  # Movimiento diagonal inválido
            ((7, 0), (5, 1)),  # Movimiento en L inválido
        ]
        for from_pos, to_pos in movimientos_invalidos:
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self._validate_move(from_pos, to_pos, False)

    def test_move_out_of_bounds(self):
        """Prueba que los movimientos fuera de límites sean rechazados."""
        out_of_bounds_moves = [
            ((7, 0), (8, 0)),
            ((7, 0), (7, 8)),
            ((0, 0), (-1, 0)),
            ((0, 0), (0, -1)),
        ]
        self._test_moves(out_of_bounds_moves, False)

    def test_path_is_blocked(self):
        """Prueba que la torre no pueda moverse si el camino está bloqueado."""
        movimientos = [((7, 0), (5, 0))]  # Movimiento bloqueado hacia adelante
        self._test_moves(movimientos, False, lambda pos: self._setup_blocking_piece((6, 0), "black"))

    def test_capture_same_color(self):
        """Prueba que la torre no pueda capturar piezas del mismo color."""
        def setup_func(pos):
            self._setup_blocking_piece((5, 0), "white")

        movimientos = [((7, 0), (5, 0))]  
        self._test_moves(movimientos, False, setup_func)

    def test_path_is_blocked_horizontal(self):
        """Prueba que la torre no pueda moverse horizontalmente si el camino está bloqueado."""
        self._setup_blocking((7, 4), "black")
        movimientos = [((7, 0), (7, 5))]
        self._test_moves(movimientos, False)

if __name__ == '__main__':
    unittest.main()
