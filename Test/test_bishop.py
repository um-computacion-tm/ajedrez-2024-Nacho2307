import unittest
from Juego.Piezas.Bishop import Bishop
from Juego.board import Board

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.board = Board()  # Inicializa un tablero vacío

    def test_movimiento_correcto_diagonal(self):
        piece = Bishop("white")
        # Movimiento diagonal válido
        self.assertTrue(piece.movimiento_correcto(2, 2, 4, 4, self.board))
        # Movimiento diagonal inválido
        self.assertFalse(piece.movimiento_correcto(2, 2, 4, 5, self.board))

    def test_diagonal_move(self):
        piece = Bishop("white")
        # Movimiento diagonal válido (sin obstáculos)
        self.assertTrue(piece.diagonal_move(self.board.__positions__, (4, 4)))
        # Movimiento diagonal inválido (con obstáculo)
        self.board.__positions__[3][3] = '♟'  # Obstáculo
        self.assertFalse(piece.diagonal_move(self.board.__positions__, (4, 4)))

if __name__ == '__main__':
    unittest.main()
