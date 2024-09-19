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
    
    def test_initial_setup(self):
        # Verifica la disposición inicial del tablero
        board = self.chess.get_board()
        self.assertIsInstance(board.get_piece(0, 4), King)
        self.assertIsInstance(board.get_piece(1, 0), Pawn)
    
    def test_valid_move(self):
        # Mover un peón blanco hacia adelante
        result = self.chess.move("6 0", "5 0")
        self.assertTrue(result)
        self.assertIsNone(self.chess.get_board().get_piece(6, 0))
        self.assertIsInstance(self.chess.get_board().get_piece(5, 0), Pawn)

    def test_invalid_move(self):
        # Intentar mover una pieza a una posición fuera de límites
        with self.assertRaises(OutOfBoundsException):
            self.chess.move("0 0", "8 0")
    
    def test_move_wrong_turn(self):
        # Intentar mover una pieza negra cuando es el turno de las blancas
        with self.assertRaises(ColorException):
            self.chess.move("1 0", "2 0")
    
    def test_check_turn_change(self):
        # Verificar el cambio de turno después de un movimiento
        self.chess.move("6 0", "5 0")  # Mover peón blanco
        self.assertEqual(self.chess.get_turn(), "black")
    
    def test_check_victory(self):
        # Simular victoria de las blancas (eliminando todas las piezas negras excepto el rey)
        board = self.chess.get_board()
        board.clear_board()
        white_king = King("White")
        black_king = King("Black")
        board.place_piece(white_king, (7, 4))
        board.place_piece(black_king, (0, 4))
        result = self.chess.check_victory()
        self.assertEqual(result, "Draw")
    
    def test_legal_moves_exist(self):
        # Verifica que haya movimientos legales para una pieza
        result = self.chess.has_legal_moves("White")
        self.assertTrue(result)

    def test_no_legal_moves(self):
        # Simular una situación de jaque mate
        board = self.chess.get_board()
        board.clear_board()

        # Colocamos al rey blanco en una posición donde no tiene escapatoria (jaque mate)
        white_king = King("White")
        black_rook1 = Rook("Black")
        black_rook2 = Rook("Black")

        board.place_piece(white_king, (7, 4))  # Rey blanco en (7, 4)
        board.place_piece(black_rook1, (6, 4))  # Torre negra en (6, 4)
        board.place_piece(black_rook2, (7, 5))  # Torre negra en (7, 5)

        # Verificamos si el rey blanco está en jaque
        self.assertTrue(self.chess.esta_en_jaque(white_king), "El rey blanco debería estar en jaque")

        # Verificamos si el rey blanco tiene movimientos legales (debería estar en jaque mate)
        result = self.chess.has_legal_moves("White")
        self.assertFalse(result, "El rey blanco debería estar en jaque mate y no tener movimientos legales")


if __name__ == "__main__":
    unittest.main()
