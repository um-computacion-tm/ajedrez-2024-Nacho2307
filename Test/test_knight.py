import unittest
from Juego.Piezas.knight import Knight
from Juego.Piezas.bishop import Bishop  
from Juego.board import Board

class TestKnight(unittest.TestCase):
    """
    Clase de pruebas para la pieza Caballo en el juego de ajedrez.
    Verifica que los movimientos del caballo se comporten según las reglas del juego.
    """

    def setUp(self):
        """Inicializa el tablero y coloca un caballo blanco."""
        self.board = Board()
        self.board.__clear_board__()
        self.caballo_blanco = Knight("white")

    def configurar_pieza_y_verificar_movimiento(self, pieza, posicion_inicial, posicion_destino, esperado, es_captura=False):
        """
        Coloca la pieza en la posición inicial y verifica si el movimiento es válido.
        Si es una captura, coloca una pieza opuesta en la posición de destino.
        """
        self.board.__place_piece__(pieza, posicion_inicial)
        
        if es_captura:
            pieza_opuesta = Bishop("black")
            self.board.__place_piece__(pieza_opuesta, posicion_destino)

        self.assertEqual(pieza.__movimiento_correcto__(posicion_inicial[0], posicion_inicial[1], posicion_destino[0], posicion_destino[1], self.board), esperado)

    def test_movimiento_bloqueado_por_misma_pieza(self):
        """Verifica que el caballo no pueda moverse a una casilla ocupada por una pieza del mismo color."""
        pieza_bloqueante = Bishop("white")
        self.board.__place_piece__(pieza_bloqueante, (2, 5))
        self.configurar_pieza_y_verificar_movimiento(self.caballo_blanco, (4, 4), (2, 5), False)

    def test_movimiento_valido_con_captura(self):
        """Verifica que el caballo pueda capturar una pieza de color opuesto."""
        self.configurar_pieza_y_verificar_movimiento(self.caballo_blanco, (4, 4), (2, 5), True, es_captura=True)

    def test_movimiento_invalido(self):
        """Verifica que el caballo no pueda moverse a una posición inválida."""
        self.assertFalse(self.caballo_blanco.__movimiento_correcto__(4, 4, 4, 5, self.board))

    def test_movimiento_valido_a_casilla_vacia(self):
        """Verifica que el caballo pueda moverse a una casilla vacía."""
        self.configurar_pieza_y_verificar_movimiento(self.caballo_blanco, (4, 4), (2, 5), True)

if __name__ == "__main__":
    unittest.main()
