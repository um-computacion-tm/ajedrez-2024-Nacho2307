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
        #Coloca una pieza en la posición especificada para bloquear el movimiento.
        self.board.__set_piece__(pos[0], pos[1], Rook(color))

    def test_valid_moves(self):
        valid_moves = [
            ((7, 0), (5, 0)),  # Movimiento hacia adelante
            ((7, 0), (7, 7)),  # Movimiento lateral
        ]
        # Validamos todos los movimientos correctos
        for from_pos, to_pos in valid_moves:
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self._validate_move(from_pos, to_pos, True)

    def test_invalid_moves(self):
        invalid_moves = [
            ((7, 0), (6, 1)),  # Movimiento diagonal inválido
            ((7, 0), (5, 1)),  # Movimiento en L inválido
        ]
        # Validamos todos los movimientos incorrectos
        for from_pos, to_pos in invalid_moves:
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self._validate_move(from_pos, to_pos, False)

    def test_move_out_of_bounds(self):
        out_of_bounds_moves = [
            ((7, 0), (8, 0)),  # Movimiento fuera del límite inferior
            ((7, 0), (7, 8)),  # Movimiento fuera del límite derecho
            ((0, 0), (-1, 0)),  # Movimiento fuera del límite superior
            ((0, 0), (0, -1)),  # Movimiento fuera del límite izquierdo
        ]
        for from_pos, to_pos in out_of_bounds_moves:
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self._validate_move(from_pos, to_pos, False)

    def test_path_is_blocked(self):
        self._setup_blocking_piece((6, 0), "black")  # Colocamos una pieza negra en el camino
        self._validate_move((7, 0), (5, 0), False)  # Movimiento bloqueado hacia adelante

    def test_capture_same_color(self):
        self._setup_blocking_piece((5, 0), "white")  # Colocamos una pieza blanca en el camino
        self._validate_move((7, 0), (5, 0), False)  # No debería permitir capturar la misma color

    def test_path_is_blocked_horizontal(self):
        self._setup_blocking_piece((7, 4), "black")  # Colocamos una pieza negra en el camino horizontal
        self._validate_move((7, 0), (7, 5), False)  # Movimiento bloqueado hacia la derecha

if __name__ == '__main__':
    unittest.main()
