import unittest
from Juego.Piezas.pawn import Pawn
from Juego.Piezas.piece import Piece
from Juego.board import Board

class TestPawn(unittest.TestCase):
    """
    Clase de pruebas para la pieza Peón en el juego de ajedrez.
    Verifica que los movimientos del peón se comporten según las reglas del juego.
    """

    def setUp(self):
        """Inicializa el tablero y coloca un peón blanco en su posición inicial."""
        self.board = Board()
        self.white_pawn = Pawn("white", 6, 1)  # Peón blanco en su posición inicial
        self.board.__set_piece__(6, 1, self.white_pawn)

    def _test_moves(self, moves, expected_result):
        """
        Prueba múltiples movimientos de un peón y verifica los resultados esperados.
        """
        for from_pos, to_pos in moves:
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self.assertEqual(self._test_move(from_pos, to_pos), expected_result)

    def _test_move(self, from_pos, to_pos):
        """Verifica si el movimiento del peón desde la posición inicial a la de destino es válido."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return self.white_pawn.__movimiento_correcto__(from_row, from_col, to_row, to_col, self.board)

    def test_valid_moves(self):
        """Verifica que los movimientos válidos del peón se comporten como se espera."""
        valid_moves = [
            ((6, 1), (5, 1)),  # Movimiento simple hacia adelante
            ((6, 1), (4, 1)),  # Movimiento doble inicial
        ]
        self.board.__set_piece__(5, 2, Piece("black", "Knight"))  # Captura diagonal
        valid_moves.append(((6, 1), (5, 2)))
        self._test_moves(valid_moves, True)

    def test_invalid_moves(self):
        """Verifica que los movimientos inválidos del peón se comporten como se espera."""
        invalid_moves = [
            ((6, 1), (3, 1)),  # Movimiento triple
            ((6, 1), (5, 3)),  # Movimiento diagonal incorrecto sin captura
        ]
        self._test_moves(invalid_moves, False)

    def test_double_initial_move_with_obstruction(self):
        """Verifica que el movimiento doble inicial sea válido solo si el camino está despejado."""
        self.assertTrue(self._test_move((6, 1), (4, 1)))  # Movimiento inicial válido
        self.board.__set_piece__(5, 1, Piece("black", "Rook"))  # Bloquear el camino
        self.assertFalse(self._test_move((6, 1), (4, 1)))  # Movimiento bloqueado

    def test_diagonal_capture(self):
        """Verifica que el peón puede capturar correctamente a una pieza opuesta."""
        capture_cases = [
            ((5, 2), "black", True),  # Captura válida
            ((5, 2), "white", False),  # Captura inválida, mismo color
        ]
        for pos, color, expected in capture_cases:
            self.board.__set_piece__(pos[0], pos[1], Piece(color, "Knight"))
            with self.subTest(pos=pos, color=color):
                self.assertEqual(self._test_move((6, 1), pos), expected)

if __name__ == '__main__':
    unittest.main()
