import unittest
from Juego.board import Board
from Juego.Piezas.Rook import Rook
from Juego.Piezas.Knight import Knight
from Juego.Piezas.King import King
from Juego.Piezas.Pawn import Pawn

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_setup(self):
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(0, 4), King)
        self.assertIsInstance(self.board.get_piece(1, 0), Pawn)
        self.assertIsNone(self.board.get_piece(2, 0))

    def test_clear_board(self):
        self.board.clear_board()
        for row in range(8):
            for col in range(8):
                self.assertIsNone(self.board.get_piece(row, col), "El tablero no se ha limpiado correctamente")

    def test_place_piece(self):
        piece = Rook("White")
        self.board.place_piece(piece, (3, 3))
        self.assertEqual(self.board.get_piece(3, 3), piece)

    def test_remove_piece(self):
        piece = Knight("Black")
        self.board.place_piece(piece, (4, 4))
        self.board.remove_piece(4, 4)
        self.assertIsNone(self.board.get_piece(4, 4), "La pieza no se ha eliminado correctamente")

    def test_str_representation(self):
        self.assertIn("♖", str(self.board))
        self.assertIn("♙", str(self.board))

    def test_show_coordinates(self):
        expected_output = (
            "  0 1 2 3 4 5 6 7\n"
            "0 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n"
            "1 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟\n"
            "2 . . . . . . . .\n"
            "3 . . . . . . . .\n"
            "4 . . . . . . . .\n"
            "5 . . . . . . . .\n"
            "6 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n"
            "7 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n"
        )
        self.assertEqual(self.board.mostrar_coords(), expected_output)

    def test_get_pieces(self):
        pieces = self.board.get_pieces()
        self.assertEqual(len(pieces), 32)

    def test_pieces_on_board(self):
        white_pieces, black_pieces = self.board.pieces_on_board()
        self.assertEqual(white_pieces, 16)
        self.assertEqual(black_pieces, 16)

    def test_is_valid_move(self):
        rook = Rook("White")
        self.board.place_piece(rook, (3, 3))
        self.assertTrue(self.board.is_valid_move(rook, (3, 3), (3, 5)))
        self.assertFalse(self.board.is_valid_move(rook, (3, 3), (4, 4)))

    def test_check_bounds_raises_exception(self):
        with self.assertRaises(IndexError):
            self.board._check_bounds(-1, 0)  # Fila negativa
        with self.assertRaises(IndexError):
            self.board._check_bounds(8, 0)   # Fila fuera de límites
        with self.assertRaises(IndexError):
            self.board._check_bounds(0, -1)  # Columna negativa
        with self.assertRaises(IndexError):
            self.board._check_bounds(0, 8)   # Columna fuera de límites

if __name__ == '__main__':
    unittest.main()
