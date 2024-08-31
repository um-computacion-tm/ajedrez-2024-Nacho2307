import unittest
from Juego.Piezas.Pawn import Pawn
from Juego.Piezas.Piece import Piece
from Juego.board import Board

class TestPawn(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.white_pawn = self.__board__.get_piece(6, 1)  # Peón blanco en su posición inicial
        if not self.white_pawn:
          self.white_pawn = Pawn("White", 6, 1)
          self.__board__.set_piece(6, 1, self.white_pawn)
            
    def test_valid_move(self):
        # Movimiento simple hacia adelante
        self.assertTrue(self._test_move((6, 1), (5, 1)))  
        # Movimiento doble inicial
        self.assertTrue(self._test_move((6, 1), (4, 1)))  
        # Captura diagonal
        self.__board__.set_piece(5, 2, Piece("Black", "Knight"))  # Colocar una pieza negra para capturar
        self.assertTrue(self._test_move((6, 1), (5, 2)))  

    def test_invalid_move(self):
        # Movimiento triple
        self.assertFalse(self._test_move((6, 1), (3, 1)))  
        # Movimiento diagonal incorrecto sin captura
        self.assertFalse(self._test_move((6, 1), (5, 3)))  

    def test_double_initial_move(self):
     self.assertTrue(self._test_move((6, 1), (4, 1)))
    # Bloquear el camino con otra pieza
     self.__board__.set_piece(5, 1, Piece("Black", "Rook"))
     self.assertFalse(self._test_move((6, 1), (4, 1)))

    def test_diagonal_capture(self):
        self.__board__.set_piece(5, 2, Piece("Black", "Knight"))
        self.assertTrue(self._test_move((6, 1), (5, 2)))
        self.__board__.set_piece(5, 2, Piece("White", "Knight"))
        self.assertFalse(self._test_move((6, 1), (5, 2)))

    def _test_move(self, from_pos, to_pos):
        return self.white_pawn.movimiento_correcto(from_pos, to_pos, self.__board__)

if __name__ == '__main__':
    unittest.main()
