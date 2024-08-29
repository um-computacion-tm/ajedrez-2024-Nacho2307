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

    def test_camino_despejado(self):
        piece = Bishop("white")
        # Movimiento diagonal válido (sin obstáculos)
        self.assertTrue(piece.movimiento_correcto(4, 4, 6, 6, self.board))
        # Movimiento diagonal inválido (con obstáculo)
        self.board.__positions__[5][5] = '♟'  # Obstáculo en la posición (5, 5)
        self.assertFalse(piece.movimiento_correcto(4, 4, 6, 6, self.board))

if __name__ == '__main__':
    unittest.main()
