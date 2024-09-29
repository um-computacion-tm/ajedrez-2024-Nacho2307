import unittest
from Juego.Piezas.Bishop import Bishop
from Juego.board import Board

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.__clear_board__()
        self.bishop = Bishop("white")
        self.board.__place_piece__(self.bishop, (4, 4))

    @staticmethod
    def validar_movimiento_correcto(pieza, inicio, destino, board, esperado):
        assert pieza.__movimiento_correcto__(inicio[0], inicio[1], destino[0], destino[1], board) == esperado

    def test_movimiento_correcto_diagonal(self):
        self.validar_movimiento_correcto(self.bishop, (4, 4), (6, 6), self.board, True)
        self.validar_movimiento_correcto(self.bishop, (4, 4), (6, 5), self.board, False)

    def test_camino_despejado(self):
        self.assertTrue(self.bishop.__movimiento_correcto__(4, 4, 6, 6, self.board))

        obstaculo = Bishop("black")
        self.board.__place_piece__(obstaculo, (5, 5))
        self.assertFalse(self.bishop.__movimiento_correcto__(4, 4, 6, 6, self.board))

    def test_movimiento_a_casilla_ocupada_por_misma_pieza(self):
        self.board.__place_piece__(self.bishop, (6, 6))  # Colocando la misma pieza
        self.assertFalse(self.bishop.__movimiento_correcto__(4, 4, 6, 6, self.board))

if __name__ == '__main__':
    unittest.main()
