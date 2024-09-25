import unittest
from Juego.Piezas.Knight import Knight
from Juego.Piezas.Bishop import Bishop  
from Juego.board import Board

class TestKnight(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.board.clear_board()
        self.caballo_blanco = Knight("white")
    
    def configurar_pieza_y_verificar_movimiento(self, pieza, posicion_inicial, posicion_destino, esperado, es_captura=False):
        # Coloca la pieza en la posición inicial
        self.board.place_piece(pieza, posicion_inicial)
        
        # Si es una captura, coloca una pieza opuesta en el destino
        if es_captura:
            pieza_opuesta = Bishop("black")
            self.board.place_piece(pieza_opuesta, posicion_destino)

        # Verifica si el movimiento es válido o no
        self.assertEqual(pieza.movimiento_correcto(posicion_inicial[0], posicion_inicial[1], posicion_destino[0], posicion_destino[1], self.board), esperado)

    def test_movimiento_bloqueado_por_misma_pieza(self):
        # Prueba que el caballo no puede moverse a una casilla ocupada por una pieza del mismo color
        pieza_bloqueante = Bishop("white")  # Misma pieza que bloquea el movimiento
        self.board.place_piece(pieza_bloqueante, (2, 5))  # Colocamos una pieza del mismo color en la casilla de destino
        self.configurar_pieza_y_verificar_movimiento(self.caballo_blanco, (4, 4), (2, 5), False)

    def test_movimiento_valido_con_captura(self):
        # Prueba que el caballo puede capturar una pieza de color opuesto
        self.configurar_pieza_y_verificar_movimiento(self.caballo_blanco, (4, 4), (2, 5), True, es_captura=True)

    def test_movimiento_invalido(self):
        # Movimiento inválido (caballo no se mueve en "L")
        self.assertFalse(self.caballo_blanco.movimiento_correcto(4, 4, 4, 5, self.board))

    def test_movimiento_valido_a_casilla_vacia(self):
        # Prueba que el caballo puede moverse a una casilla vacía
        self.configurar_pieza_y_verificar_movimiento(self.caballo_blanco, (4, 4), (2, 5), True)

if __name__ == "__main__":
    unittest.main()
