import unittest
from Juego.Chess import Chess
from Juego.board import Board
from Juego.Exception import (
    InvalidMoveException,
    OutOfBoundsException,
    PieceAlreadyCapturedException,
    ColorException,
    TurnException
)
from Juego.Piezas.Rook import Rook
from Juego.Piezas.King import King
from Juego.Piezas.Pawn import Pawn

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_invalid_move_king_in_check(self):
        # Intentar mover una pieza que deja al rey en jaque
        self.chess.get_board().place_piece(King("white"), (7, 4))  # Coloca el rey blanco
        self.chess.get_board().place_piece(Rook("black"), (0, 4))  # Coloca una torre negra que amenaza al rey
        with self.assertRaises(InvalidMoveException):
            self.chess.move("7 4", "6 4")  # Intentar mover al rey blanco deja al rey en jaque

    def test_piece_already_captured(self):
        # Intentar mover desde una posición donde no hay pieza
        with self.assertRaises(PieceAlreadyCapturedException):
            self.chess.move("3 3", "4 3")

    def test_out_of_bounds_position(self):
        # Probar posiciones fuera de los límites
        with self.assertRaises(OutOfBoundsException):
            self.chess.move("0 0", "9 0")  # Movimiento fuera de los límites

        with self.assertRaises(ValueError):
            self.chess.move("a b", "2 2")  # Entrada inválida de formato

    def test_change_turn_back_and_forth(self):
        # Verificar que el cambio de turno funciona en ambas direcciones
        self.assertEqual(self.chess.get_turn(), "WHITE")
        self.chess.move("6 0", "5 0")  # Mover un peón blanco
        self.assertEqual(self.chess.get_turn(), "BLACK")
        self.chess.move("1 0", "2 0")  # Mover un peón negro
        self.assertEqual(self.chess.get_turn(), "WHITE")

    def test_draw(self):
        # Simular tablas: solo queda el rey blanco y el rey negro
        board = self.chess.get_board()
        board.clear_board()
        white_king = King("white")
        black_king = King("black")
        board.place_piece(white_king, (7, 4))  # Coloca el rey blanco
        board.place_piece(black_king, (0, 4))  # Coloca el rey negro
        result = self.chess.check_victory()
        self.assertEqual(result, "Draw")

    def test_victory_status_returned(self):
        # Simular victoria de las blancas y verificar que el estado se devuelve correctamente
        board = self.chess.get_board()
        board.clear_board()
        white_king = King("white")
        black_king = King("black")
        board.place_piece(white_king, (7, 4))  # Coloca el rey blanco
        result = self.chess.move("7 4", "6 4")  # Este movimiento debería devolver el estado del juego
        self.assertEqual(result, "White wins")

    def simulate_victory(self, king_color, expected_result):
        board = self.chess.get_board()
        board.clear_board()
        king = King(king_color)
        # Colocar al rey en la fila correspondiente según el color
        row = 7 if king_color == "white" else 0
        board.place_piece(king, (row, 4))
        result = self.chess.check_victory()
        self.assertEqual(result, expected_result)

    def test_victory_white_wins(self):
        # Simular victoria de las blancas
        self.simulate_victory("white", "White wins")

    def test_black_wins(self):
        # Simular victoria de las negras
        self.simulate_victory("black", "Black wins")
