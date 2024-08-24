import unittest
from Juego.Exception import (
    InvalidMoveException,
    OutOfBoundsException,
    PieceAlreadyCapturedException,
    CheckException,
    CheckException,
    CheckmateException,
    ColorException,
    TurnException
)

class ExcepcionAjedrez:
    __tipo__ = "Excepción de Ajedrez"
    __severidad__ = "Alta"

    def obtener_tipo(self):
        return self.__tipo__

    def obtener_severidad(self):
        return self.__severidad__

class TestChessExceptions(unittest.TestCase):

    def test_invalid_move_exception(self):
        with self.assertRaises(InvalidMoveException) as context:
            raise InvalidMoveException("Movimiento inválido")
        self.assertEqual(str(context.exception), "Movimiento inválido")

    def test_out_of_bounds_exception(self):
        with self.assertRaises(OutOfBoundsException) as context:
            raise OutOfBoundsException("Movimiento fuera del tablero")
        self.assertEqual(str(context.exception), "Movimiento fuera del tablero")

    def test_piece_already_captured_exception(self):
        with self.assertRaises(PieceAlreadyCapturedException) as context:
            raise PieceAlreadyCapturedException("Pieza ya capturada")
        self.assertEqual(str(context.exception), "Pieza ya capturada")

    def test_check_exception(self):
        with self.assertRaises(CheckException) as context:
            raise CheckException("Rey en jaque")
        self.assertEqual(str(context.exception), "Rey en jaque")

    def test_checkmate_exception(self):
        with self.assertRaises(CheckmateException) as context:
            raise CheckmateException("Jaque mate")
        self.assertEqual(str(context.exception), "Jaque mate")

    def test_color_exception(self):
        with self.assertRaises(ColorException) as context:
            raise ColorException("Color incorrecto")
        self.assertEqual(str(context.exception), "Color incorrecto")

    def test_turn_exception(self):
        with self.assertRaises(TurnException) as context:
            raise TurnException("No es tu turno")
        self.assertEqual(str(context.exception), "No es tu turno")

if __name__ == '__main__':
    unittest.main()
