import unittest
from Juego.Exception import (
    InvalidPositionException,
    InvalidPieceMovementException,
    CantEatKingException,
    WrongTurnException,
    GeneralChessError,
    ChessException,
    InvalidMoveException,
    OutOfBoundsException,
    PieceAlreadyCapturedException,
    CheckException,
    CheckmateException,
    ColorException,
    TurnException,
    PieceNotFoundError  
)

class TestChessExceptions(unittest.TestCase):
    def _test_exception(self, exception_class, expected_message):
        with self.assertRaises(exception_class) as context:
            raise exception_class()
        self.assertEqual(str(context.exception), expected_message)

    def test_chess_exception(self):
        # ChessException base test
        self._test_exception(ChessException, "Error en el juego de ajedrez")

    def test_invalid_move_exception(self):
        self._test_exception(InvalidMoveException, "Movimiento inválido")

    def test_out_of_bounds_exception(self):
        self._test_exception(OutOfBoundsException, "La pieza está fuera del tablero")

    def test_piece_already_captured_exception(self):
        self._test_exception(PieceAlreadyCapturedException, "La pieza ya ha sido capturada")

    def test_check_exception(self):
        self._test_exception(CheckException, "El rey está en jaque")

    def test_checkmate_exception(self):
        self._test_exception(CheckmateException, "El rey está en jaque mate")

    def test_color_exception(self):
        self._test_exception(ColorException, "Movimiento del color equivocado")

    def test_turn_exception(self):
        self._test_exception(TurnException, "Es el turno del otro jugador")

    def test_invalid_position_exception(self):
        self._test_exception(InvalidPositionException, "La posición es inválida. Debe estar dentro del tablero")

    def test_invalid_piece_movement_exception(self):
        self._test_exception(InvalidPieceMovementException, "Movimiento no válido para esta pieza")

    def test_cant_eat_king_exception(self):
        self._test_exception(CantEatKingException, "No puedes capturar al Rey")

    def test_wrong_turn_exception(self):
        self._test_exception(WrongTurnException, "Es el turno del otro jugador")

    def test_general_chess_error(self):
        self._test_exception(GeneralChessError, "Ha ocurrido un error en el juego de ajedrez")

    def test_piece_not_found_error(self):
        self._test_exception(PieceNotFoundError, "Pieza no encontrada en el tablero")

if __name__ == '__main__':
    unittest.main()

