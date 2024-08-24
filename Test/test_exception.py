import unittest
from Juego.Exception import (
    InvalidMoveException,
    OutOfBoundsException,
    PieceAlreadyCapturedException,
    CheckException,
    CheckmateException,
    ColorException,
    TurnException
)

class TestChessExceptions(unittest.TestCase):
    def _test_exception(self, exception_class, message):
        with self.assertRaises(exception_class) as context:
            raise exception_class(message)
        self.assertEqual(str(context.exception), message)

    def test_invalid_move_exception(self):
        self._test_exception(InvalidMoveException, "Movimiento inválido")

    def test_out_of_bounds_exception(self):
        self._test_exception(OutOfBoundsException, "Movimiento fuera del tablero")

    def test_piece_already_captured_exception(self):
        self._test_exception(PieceAlreadyCapturedException, "Pieza ya capturada")

    def test_check_exception(self):
        self._test_exception(CheckException, "Rey en jaque")

    def test_checkmate_exception(self):
        self._test_exception(CheckmateException, "Jaque mate")

    def test_color_exception(self):
        self._test_exception(ColorException, "Color incorrecto")

    def test_turn_exception(self):
        self._test_exception(TurnException, "No es tu turno")

if __name__ == '__main__':
    unittest.main()
