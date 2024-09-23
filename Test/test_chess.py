import unittest
from Juego.Chess import Chess
from Juego.board import Board
from Juego.Exception import (
    InvalidMoveException,
    OutOfBoundsException,
    PieceAlreadyCapturedException,
    ColorException,
    TurnException
)
from Juego.Piezas.Rook import Rook
from Juego.Piezas.King import King
from Juego.Piezas.Pawn import Pawn

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()

    def test_invalid_move_king_in_check(self):
        # Intentar mover una pieza que deja al rey en jaque
        self.chess.get_board().place_piece(King("white"), (7, 4))  # Coloca el rey blanco
        self.chess.get_board().place_piece(Rook("black"), (0, 4))  # Coloca una torre negra que amenaza al rey
        with self.assertRaises(InvalidMoveException):
            self.chess.move("7 4", "6 4")  # Intentar mover al rey blanco deja al rey en jaque

    def test_piece_already_captured(self):
        # Intentar mover desde una posición donde no hay pieza
        with self.assertRaises(PieceAlreadyCapturedException):
            self.chess.move("3 3", "4 3")

    def test_out_of_bounds_position(self):
        # Probar posiciones fuera de los límites
        with self.assertRaises(OutOfBoundsException):
            self.chess.move("0 0", "9 0")  # Movimiento fuera de los límites

        with self.assertRaises(ValueError):
            self.chess.move("a b", "2 2")  # Entrada inválida de formato

    def test_change_turn_back_and_forth(self):
        self.assertEqual(self.chess.get_turn(), "WHITE")
        self.chess.get_board().place_piece(Pawn("white"), (6, 0)) 
        self.chess.move("6 0", "5 0")  # Mover un peón blanco
        self.assertEqual(self.chess.get_turn(), "BLACK")
        self.chess.get_board().place_piece(Pawn("black"), (1, 0))  
        self.chess.move("1 0", "2 0")  # Mover un peón negro
        self.assertEqual(self.chess.get_turn(), "WHITE")

    def test_draw(self):
        board = self.chess.get_board()
        board.clear_board()  # Limpiar el tablero

        # Colocar solo los dos reyes en el tablero
        board.place_piece(King("white"), (7, 4))  # Rey blanco
        board.place_piece(King("black"), (0, 4))  # Rey negro

        # Verificar si el juego termina en empate
        result = self.chess.check_victory()
        self.assertEqual(result, "Draw")

    def test_victory_status_returned(self):
        # Simular un escenario donde las negras ganan
        board = self.chess.get_board()
        board.clear_board()  # Limpiar todas las piezas
    
        # Colocar solo una torre negra en el tablero
        board.place_piece(Rook("black"), (0, 4))
    
        # Verificar si el juego termina con victoria para las negras
        result = self.chess.check_victory()
        self.assertEqual(result, "Black wins")

    def simulate_victory(self, king_color, expected_result):
        board = self.chess.get_board()
        board.clear_board()
    
        # Colocar el rey del color especificado
        king = King(king_color)
        row = 7 if king_color == "white" else 0
        board.place_piece(king, (row, 4))  # Solo coloca al rey
    
        # El resultado debe ser que el otro jugador gana
        result = self.chess.check_victory()
        self.assertEqual(result, expected_result)

    def test_victory_white_wins(self):
        # Simular victoria de las blancas (rey blanco, sin piezas negras)
        self.simulate_victory("white", "White wins")

    def test_victory_black_wins(self):
        # Simular victoria de las negras (rey negro, sin piezas blancas)
        self.simulate_victory("black", "Black wins")

    def test_move_returns_status(self):
        # Configura el tablero con varias piezas para evitar la condición de victoria
        board = self.chess.get_board()
        board.clear_board()
        board.place_piece(Pawn("white"), (6, 4))  # Colocar un peón blanco en (6, 4)
        board.place_piece(King("black"), (0, 4))  # Colocar el rey negro para evitar que gane inmediatamente
        board.place_piece(King("white"), (7, 4))  # Colocar el rey blanco

        # Mover el peón de (6, 4) a (5, 4)
        status = self.chess.move("6 4", "5 4")

        # Verificar que el movimiento fue exitoso y se retornó un estado
        self.assertIsNotNone(status)
        self.assertEqual(status, "Move successful")  

    def test_move_returns_victory_status(self):
        board = self.chess.get_board()
        board.clear_board()

        # Colocar piezas en el tablero
        board.place_piece(Rook("black"), (0, 4))  # Torre negra
        board.place_piece(King("white"), (7, 4))  # Rey blanco
        board.place_piece(Pawn("white"), (6, 0))  # Peón blanco

        # Mover el peón blanco para cambiar de turno
        self.chess.move("6 0", "5 0")  # Movimiento exitoso del peón blanco

        # Mover la torre negra para capturar al rey blanco
        status = self.chess.move("0 4", "7 4")  # Movimiento de la torre negra

        # Verificar que el movimiento retorna "Black wins"
        self.assertEqual(status, "Black wins")

    def test_move_returns_draw_status(self):
        board = self.chess.get_board()
        board.clear_board()

        # Colocar solo los dos reyes para generar un empate
        board.place_piece(King("white"), (7, 4))  # Rey blanco
        board.place_piece(King("black"), (0, 4))  # Rey negro

        # Realizar cualquier movimiento que no cambie la situación de empate
        status = self.chess.move("7 4", "6 4")  # Mover al rey blanco

        # Verificar que el movimiento retorna "Draw"
        self.assertEqual(status, "Draw")

if __name__ == '__main__':
    unittest.main()
