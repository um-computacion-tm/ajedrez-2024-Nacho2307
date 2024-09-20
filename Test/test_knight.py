import unittest
from Juego.Piezas.Knight import Knight
from Juego.Piezas.Bishop import Bishop  # Para usar como pieza de destino
from Juego.board import Board

class TestKnight(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()
        self.board.clear_board()  # Limpia el tablero antes de cada prueba
        self.caballo_blanco = Knight("white")
        self.board.place_piece(self.caballo_blanco, (4, 4))  # Caballo blanco en (4, 4)
    
    def test_movimiento_correcto(self):
        # Movimiento correcto
        self.assertTrue(self.caballo_blanco.movimiento_correcto(4, 4, 2, 5, self.board))
    
    def test_movimiento_bloqueado_por_misma_pieza(self):
        # Coloca una pieza del mismo color en el destino
        misma_pieza = Bishop("white")
        self.board.place_piece(misma_pieza, (2, 5))
        
        # Verifica que el caballo no puede moverse a una casilla ocupada por una pieza del mismo color
        self.assertFalse(self.caballo_blanco.movimiento_correcto(4, 4, 2, 5, self.board))

    def test_movimiento_valido_con_captura(self):
        # Coloca una pieza de color opuesto en el destino
        pieza_opuesta = Bishop("black")
        self.board.place_piece(pieza_opuesta, (2, 5))
        
        # Verifica que el caballo puede capturar una pieza de color diferente
        self.assertTrue(self.caballo_blanco.movimiento_correcto(4, 4, 2, 5, self.board))

    def test_movimiento_invalido(self):
        # Movimiento inválido (caballo no se mueve en "L")
        self.assertFalse(self.caballo_blanco.movimiento_correcto(4, 4, 4, 5, self.board))

if __name__ == "__main__":
    unittest.main()
