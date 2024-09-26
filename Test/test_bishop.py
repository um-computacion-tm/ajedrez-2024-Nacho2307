import unittest
from Juego.Piezas.Bishop import Bishop
from Juego.Piezas.Piece import Piece
from Juego.board import Board

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.board = Board()  # Inicializa el tablero real
        self.board.__clear_board__()  # Limpia el tablero antes de cada prueba
        self.bishop = Bishop("white")
        self.board.__place_piece__(self.bishop, (4, 4))  # Coloca el alfil en la posición (4, 4)

    def test_movimiento_correcto_diagonal(self):
        # Movimiento diagonal válido
        self.assertTrue(self.bishop.__movimiento_correcto__(4, 4, 6, 6, self.board))
        # Movimiento diagonal inválido (no diagonal)
        self.assertFalse(self.bishop.__movimiento_correcto__(4, 4, 6, 5, self.board))

    def test_camino_despejado(self):
        # Movimiento diagonal válido (sin obstáculos)
        self.assertTrue(self.bishop.__movimiento_correcto__(4, 4, 6, 6, self.board))

        # Coloca una pieza como obstáculo
        obstaculo = Bishop("black")
        self.board.__place_piece__(obstaculo, (5, 5))  # Obstáculo en la posición (5, 5)

        # Movimiento diagonal inválido debido al obstáculo
        self.assertFalse(self.bishop.__movimiento_correcto__(4, 4, 6, 6, self.board))

    def test_movimiento_a_casilla_ocupada_por_misma_pieza(self):
        # Coloca una pieza del mismo color en la casilla de destino (6, 6)
        misma_pieza = Bishop("white")
        self.board.__place_piece__(misma_pieza, (6, 6))

        # Verifica que no se puede mover a una casilla ocupada por una pieza del mismo color
        self.assertFalse(self.bishop.__movimiento_correcto__(4, 4, 6, 6, self.board))

if __name__ == '__main__':
    unittest.main()
