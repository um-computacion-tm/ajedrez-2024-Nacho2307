import unittest
from Juego.Piezas.Pawn import Pawn
from Juego.Piezas.Piece import Piece
from Juego.board import Board

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.white_pawn = self.__board__.get_piece(6, 1)  # Peón blanco en su posición inicial
        if not self.white_pawn:
            self.white_pawn = Pawn("White", 6, 1)
            self.__board__.set_piece(6, 1, self.white_pawn)

    def test_valid_moves(self):
        valid_moves = [
            ((6, 1), (5, 1)),  # Movimiento simple hacia adelante
            ((6, 1), (4, 1)),  # Movimiento doble inicial
        ]
        # Captura diagonal
        self.__board__.set_piece(5, 2, Piece("Black", "Knight"))
        valid_moves.append(((6, 1), (5, 2)))

        self._test_moves(valid_moves, True)

    def test_invalid_moves(self):
        invalid_moves = [
            ((6, 1), (3, 1)),  # Movimiento triple
            ((6, 1), (5, 3)),  # Movimiento diagonal incorrecto sin captura
        ]
        self._test_moves(invalid_moves, False)

    def test_double_initial_move_with_obstruction(self):
        self.assertTrue(self._test_move((6, 1), (4, 1)))
        # Bloquear el camino con otra pieza
        self.__board__.set_piece(5, 1, Piece("Black", "Rook"))
        self.assertFalse(self._test_move((6, 1), (4, 1)))

    def test_diagonal_capture(self):
        capture_cases = [
            ((5, 2), "Black", True),  # Captura válida
            ((5, 2), "White", False),  # Captura inválida, mismo color
        ]
        for pos, color, expected in capture_cases:
            self.__board__.set_piece(pos[0], pos[1], Piece(color, "Knight"))
            with self.subTest(pos=pos, color=color):
                self.assertEqual(self._test_move((6, 1), pos), expected)

    def _test_moves(self, moves, expected_result):
       
        for from_pos, to_pos in moves:
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self.assertEqual(self._test_move(from_pos, to_pos), expected_result)

    def _test_move(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return self.white_pawn.movimiento_correcto(from_row, from_col, to_row, to_col, self.__board__)

if __name__ == '__main__':
    unittest.main()
