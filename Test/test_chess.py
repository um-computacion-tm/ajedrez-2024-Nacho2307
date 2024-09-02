import unittest
from Juego.Chess import Chess
from Juego.Exception import PieceAlreadyCapturedException

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
        # Ajusta el retorno esperado basado en la lógica de `check_victory`
        self.assertEqual(self.chess.check_victory(), "No result")

    def test_esta_en_jaque(self):
        king = self.chess.get_piece_or_raise((7, 4))  
        self.assertFalse(self.chess.esta_en_jaque(king))

    def test_has_legal_moves(self):
        self.assertTrue(self.chess.has_legal_moves("WHITE"))

    def test_is_in_check_after_move(self):
        self.assertFalse(self.chess.is_in_check_after_move("WHITE", (1, 1)))

    def test_obtener_rey(self):
        king = self.chess.obtener_rey("WHITE")
        self.assertEqual(king.__class__.__name__, "King")

if __name__ == '__main__':
    unittest.main()
