import unittest
from Juego.Piezas.Rook import Rook
from Juego.Piezas.Knight import Knight
from Juego.Piezas.King import King
from Juego.Piezas.Bishop import Bishop
from Juego.Piezas.Pawn import Pawn
from Juego.Piezas.Queen import Queen
from Juego.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_setup(self):
        # Test que el tablero se inicializa correctamente con las piezas en las posiciones correctas.
        expected = (
            "♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜\n"
            "♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            "♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙\n"
            "♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖\n"
        )
        self.assertEqual(str(self.board), expected)

    def test_clear_board(self):
        # Test que el tablero se limpia correctamente.
        self.board.clear_board()
        expected = (
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
            ". . . . . . . .\n"
        )
        self.assertEqual(str(self.board), expected)

    def test_place_piece(self):
        # Test para verificar la colocación de piezas en el tablero.
        self.board.clear_board()
        rook = Rook("White")
        self.board.place_piece(rook, (4, 4))
        self.assertEqual(self.board.get_piece(4, 4), rook)

    def test_remove_piece(self):
        # Test para verificar la eliminación de piezas del tablero.
        self.board.clear_board()
        rook = Rook("White")
        self.board.place_piece(rook, (4, 4))
        self.board.remove_piece(4, 4)
        self.assertIsNone(self.board.get_piece(4, 4))

    def test_show_coords(self):
        # Test para verificar la representación del tablero con coordenadas.
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

    def test_get_piece(self):
        # Test para verificar la obtención de una pieza específica en una posición dada.
        rook = Rook("White")
        self.board.place_piece(rook, (2, 3))
        self.assertEqual(self.board.get_piece(2, 3), rook)

    def test_check_bounds(self):
        # Test para verificar que la función de límites funciona correctamente.
        self.board._check_bounds(0, 0)
        self.board._check_bounds(7, 7)
        with self.assertRaises(IndexError):
            self.board._check_bounds(-1, 0)
        with self.assertRaises(IndexError):
            self.board._check_bounds(0, 8)

    def test_get_pieces(self):
        self.board.clear_board()  # Limpiar el tablero para empezar de cero

        # Colocar algunas piezas manualmente
        rook_white = Rook("White")
        rook_black = Rook("Black")
        self.board.place_piece(rook_white, (0, 0))
        self.board.place_piece(rook_black, (7, 7))

        # Obtener todas las piezas en el tablero
        pieces = self.board.get_pieces()

        # Verificar que la lista de piezas tenga la longitud correcta
        self.assertEqual(len(pieces), 2)

        # Verificar que las piezas sean las correctas
        self.assertIsInstance(pieces[0], Rook)
        self.assertIsInstance(pieces[1], Rook)
        self.assertEqual(pieces[0].get_color(), "White")
        self.assertEqual(pieces[1].get_color(), "Black")

if __name__ == "__main__":
    unittest.main()
