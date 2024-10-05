import unittest
from Juego.exception import (
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
    PieceNotFoundError,
    ChessMessageException  
)

class TestChessExceptions(unittest.TestCase):
    """
    Clase de pruebas para las excepciones del juego de ajedrez.
    Verifica que las excepciones se lancen y manejen correctamente.
    """

    def _test_exception(self, exception_class, message):
        """Lanza la excepción especificada y verifica que el mensaje sea correcto."""
        with self.assertRaises(exception_class) as context:
            raise exception_class(message)
        self.assertEqual(str(context.exception), message)

    def test_chess_exception(self):
        """Verifica que ChessException se maneje correctamente."""
        self._test_exception(ChessException, "Base Chess Exception")

    def test_invalid_move_exception(self):
        """Verifica que InvalidMoveException se maneje correctamente."""
        self._test_exception(InvalidMoveException, "Invalid move for this piece.")

    def test_out_of_bounds_exception(self):
        """Verifica que OutOfBoundsException se maneje correctamente."""
        self._test_exception(OutOfBoundsException, "Position is out of bounds.")

    def test_piece_already_captured_exception(self):
        """Verifica que PieceAlreadyCapturedException se maneje correctamente."""
        self._test_exception(PieceAlreadyCapturedException, "Piece has already been captured.")

    def test_check_exception(self):
        """Verifica que CheckException se maneje correctamente."""
        self._test_exception(CheckException, "King is in check.")

    def test_checkmate_exception(self):
        """Verifica que CheckmateException se maneje correctamente."""
        self._test_exception(CheckmateException, "Checkmate occurred.")

    def test_color_exception(self):
        """Verifica que ColorException se maneje correctamente."""
        self._test_exception(ColorException, "Incorrect color move.")

    def test_turn_exception(self):
        """Verifica que TurnException se maneje correctamente."""
        self._test_exception(TurnException, "It's the wrong player's turn.")

    def test_invalid_position_exception(self):
        """Verifica que InvalidPositionException se maneje correctamente."""
        self._test_exception(InvalidPositionException, "La posición es inválida. Debe estar dentro del tablero.")

    def test_invalid_piece_movement_exception(self):
        """Verifica que InvalidPieceMovementException se maneje correctamente."""
        self._test_exception(InvalidPieceMovementException, "Movimiento no válido para esta pieza.")

    def test_cant_eat_king_exception(self):
        """Verifica que CantEatKingException se maneje correctamente."""
        self._test_exception(CantEatKingException, "No puedes capturar al Rey.")

    def test_wrong_turn_exception(self):
        """Verifica que WrongTurnException se maneje correctamente."""
        self._test_exception(WrongTurnException, "Es el turno del otro jugador.")

    def test_general_chess_error(self):
        """Verifica que GeneralChessError se maneje correctamente."""
        self._test_exception(GeneralChessError, "Ha ocurrido un error en el juego de ajedrez.")

    def test_piece_not_found_error(self):  
        """Verifica que PieceNotFoundError se maneje correctamente."""
        self._test_exception(PieceNotFoundError, "Pieza no encontrada en el tablero.")

    def test_chess_message_exception_default_message(self):
        """Verifica que el mensaje por defecto de ChessMessageException sea correcto."""
        with self.assertRaises(ChessMessageException) as context:
            raise ChessMessageException()
        self.assertEqual(str(context.exception), "Error en el juego de ajedrez.")

if __name__ == '__main__':
    unittest.main()
