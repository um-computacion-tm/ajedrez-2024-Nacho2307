import unittest
from Juego.Chess import Chess
from Juego.Exception import (
    PieceAlreadyCapturedException,
    InvalidMoveException,
    OutOfBoundsException,
    ColorException,
    TurnException
)

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()

    def test_get_piece_or_raise_with_piece(self):
        king = self.chess.get_piece_or_raise((0, 4))
        self.assertEqual(king.__class__.__name__, "King")

    def test_get_piece_or_raise_without_piece(self):
        with self.assertRaises(PieceAlreadyCapturedException):
            self.chess.get_piece_or_raise((4, 4))

    def test_check_victory_no_result(self):
        self.assertEqual(self.chess.check_victory(), "No result")

    def test_esta_en_jaque(self):
        king = self.chess.get_piece_or_raise((7, 4))  
        self.assertFalse(self.chess.esta_en_jaque(king))

    def test_has_legal_moves(self):
        self.assertTrue(self.chess.has_legal_moves("WHITE"))

    def test_is_in_check_after_move(self):
        self.assertFalse(self.chess.is_in_check_after_move("WHITE", (1, 1), (3, 1)))

    def test_obtener_rey(self):
        king = self.chess.obtener_rey("WHITE")
        self.assertEqual(king.__class__.__name__, "King")

    def test_move_valid(self):
        self.assertTrue(self.chess.move("1 4", "3 4"))

    def test_move_invalid_out_of_bounds(self):
        with self.assertRaises(OutOfBoundsException):
            self.chess.move("8 8", "9 9")  # Posición fuera del rango

    def test_move_invalid_color(self):
        with self.assertRaises(ColorException):
            self.chess.move("1 4", "2 4")  # Moviendo una pieza del turno equivocado

    def test_move_invalid_move(self):
        with self.assertRaises(InvalidMoveException):
            self.chess.move("1 0", "2 2")  # Movimiento no válido para un peón

    def test_turn_change(self):
        self.chess.move("1 4", "3 4")  # Movimiento válido
        self.assertEqual(self.chess.get_turn(), "BLACK")  # Después de mover, debe cambiar el turno

    def test_print_board(self):
        self.chess.print_board()  # Asegúrate de que la impresión del tablero no falle

    def test_no_legal_moves_for_color(self):
        self.assertFalse(self.chess.has_legal_moves("BLACK"))  # Dependiendo de la posición inicial, es posible que no haya movimientos legales

if __name__ == '__main__':
    unittest.main()
