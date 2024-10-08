import unittest
from Juego.Piezas.bishop import Bishop
from Juego.board import Board

class TestBishop(unittest.TestCase):
    """
    Clase de pruebas para la clase Bishop en el juego de ajedrez.
    Verifica que los movimientos del alfil sean correctos según las reglas del ajedrez.
    """

    @staticmethod
    def validar_movimiento_correcto(pieza, inicio, destino, board, esperado):
        """Valida si el movimiento de la pieza es correcto."""
        resultado = pieza.__movimiento_correcto__(inicio[0], inicio[1], destino[0], destino[1], board)
        assert resultado == esperado, f"Se esperaba {esperado} pero se obtuvo {resultado}."

    def setUp(self):
        """Inicializa el tablero y coloca un alfil en la posición inicial."""
        self.board = Board()
        self.board.__clear_board__()
        self.bishop = Bishop("white")
        self.board.__place_piece__(self.bishop, (4, 4))

    def test_movimiento_correcto_diagonal(self):
        """Prueba movimientos diagonales correctos e incorrectos del alfil."""
        self.validar_movimiento_correcto(self.bishop, (4, 4), (6, 6), self.board, True)
        self.validar_movimiento_correcto(self.bishop, (4, 4), (6, 5), self.board, False)

    def test_camino_despejado(self):
        """Verifica si el alfil puede moverse a una posición sin obstáculos."""
        self.assertTrue(self.bishop.__movimiento_correcto__(4, 4, 6, 6, self.board))

        obstaculo = Bishop("black")
        self.board.__place_piece__(obstaculo, (5, 5))
        self.assertFalse(self.bishop.__movimiento_correcto__(4, 4, 6, 6, self.board))

    def test_movimiento_a_casilla_ocupada_por_misma_pieza(self):
        """Verifica que el alfil no pueda moverse a una casilla ocupada por su propia pieza."""
        self.board.__place_piece__(self.bishop, (6, 6))
        self.assertFalse(self.bishop.__movimiento_correcto__(4, 4, 6, 6, self.board))

if __name__ == '__main__':
    unittest.main()
