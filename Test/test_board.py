import unittest
from Juego.board import Board
from Juego.Piezas.rook import Rook
from Juego.Piezas.knight import Knight
from Juego.Piezas.king import King
from Juego.Piezas.pawn import Pawn

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()

    def test_initial_setup(self):
        self.assertIsInstance(self.__board__.__get_piece__(0, 0), Rook)
        self.assertIsInstance(self.__board__.__get_piece__(0, 4), King)
        self.assertIsInstance(self.__board__.__get_piece__(1, 0), Pawn)
        self.assertIsNone(self.__board__.__get_piece__(2, 0))

    def test_clear_board(self):
        self.__board__.__clear_board__()
        for row in range(8):
            for col in range(8):
                self.assertIsNone(self.__board__.__get_piece__(row, col), "El tablero no se ha limpiado correctamente")

    def test_place_piece(self):
        piece = Rook("White")
        self.__board__.__place_piece__(piece, (3, 3))
        self.assertEqual(self.__board__.__get_piece__(3, 3), piece)

    def test_remove_piece(self):
        piece = Knight("Black")
        self.__board__.__place_piece__(piece, (4, 4))
        self.__board__.__remove_piece__(4, 4)
        self.assertIsNone(self.__board__.__get_piece__(4, 4), "La pieza no se ha eliminado correctamente")

    def test_str_representation(self):
        self.assertIn("♖", str(self.__board__))
        self.assertIn("♙", str(self.__board__))

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
        self.assertEqual(self.__board__.__mostrar_coords__(), expected_output)

    def test_get_pieces(self):
        pieces = self.__board__.__get_pieces__()
        self.assertEqual(len(pieces), 32)

    def test_pieces_on_board(self):
        white_pieces, black_pieces = self.__board__.__pieces_on_board__()
        self.assertEqual(white_pieces, 16)
        self.assertEqual(black_pieces, 16)

    def test_is_valid_move(self):
        rook = Rook("White")
        self.__board__.__place_piece__(rook, (3, 3))
        self.assertTrue(self.__board__.__is_valid_move__(rook, (3, 3), (3, 5)))
        self.assertFalse(self.__board__.__is_valid_move__(rook, (3, 3), (4, 4)))

    def test_check_bounds_raises_exception(self):
        with self.assertRaises(IndexError):
            self.__board__.__check_bounds__(-1, 0)  # Fila negativa
        with self.assertRaises(IndexError):
            self.__board__.__check_bounds__(8, 0)   # Fila fuera de límites
        with self.assertRaises(IndexError):
            self.__board__.__check_bounds__(0, -1)  # Columna negativa
        with self.assertRaises(IndexError):
            self.__board__.__check_bounds__(0, 8)   # Columna fuera de límites

if __name__ == '__main__':
    unittest.main()
