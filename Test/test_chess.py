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
        self.__chess__ = Chess()

    def test_load_game(self):
        # Configurar un juego inicial y guardarlo
        self.__chess__.__get_board__().__place_piece__(King("white"), (7, 4))
        self.__chess__.__get_board__().__place_piece__(Rook("black"), (0, 4))
        self.__chess__.__save_game__("test_game")

        # Crear una nueva instancia de Chess y cargar el juego guardado
        new_chess = Chess()
        new_chess.__load_game__("test_game")

        # Verificar que el estado del tablero y el turno sean correctos
        self.assertIsNotNone(new_chess.__get_board__().__get_piece__(7, 4))  # Rey blanco en (7, 4)
        self.assertIsNotNone(new_chess.__get_board__().__get_piece__(0, 4))  # Torre negra en (0, 4)
        self.assertEqual(new_chess.__get_turn__(), "WHITE")  # El turno debe ser blanco

    def test_invalid_move_king_in_check(self):
        # Intentar mover una pieza que deja al rey en jaque
        self.__chess__.__get_board__().__place_piece__(King("white"), (7, 4))  # Coloca el rey blanco
        self.__chess__.__get_board__().__place_piece__(Rook("black"), (0, 4))  # Coloca una torre negra que amenaza al rey
        with self.assertRaises(InvalidMoveException):
            self.__chess__.__move__("7 4", "6 4")  # Intentar mover al rey blanco deja al rey en jaque

    def test_piece_already_captured(self):
        # Intentar mover desde una posición donde no hay pieza
        with self.assertRaises(PieceAlreadyCapturedException):
            self.__chess__.__move__("3 3", "4 3")

    def test_out_of_bounds_position(self):
        # Probar posiciones fuera de los límites
        with self.assertRaises(OutOfBoundsException):
            self.__chess__.__move__("0 0", "9 0")  # Movimiento fuera de los límites

        with self.assertRaises(ValueError):
            self.__chess__.__move__("a b", "2 2")  # Entrada inválida de formato

    def test_change_turn_back_and_forth(self):
        self.assertEqual(self.__chess__.__get_turn__(), "WHITE")
        self.__chess__.__get_board__().__place_piece__(Pawn("white"), (6, 0)) 
        self.__chess__.__move__("6 0", "5 0")  # Mover un peón blanco
        self.assertEqual(self.__chess__.__get_turn__(), "BLACK")
        self.__chess__.__get_board__().__place_piece__(Pawn("black"), (1, 0))  
        self.__chess__.__move__("1 0", "2 0")  # Mover un peón negro
        self.assertEqual(self.__chess__.__get_turn__(), "WHITE")

    def test_draw(self):
        board = self.__chess__.__get_board__()
        board.__clear_board__()  # Limpiar el tablero

        # Colocar solo los dos reyes en el tablero
        board.__place_piece__(King("white"), (7, 4))  # Rey blanco
        board.__place_piece__(King("black"), (0, 4))  # Rey negro

        # Verificar si el juego termina en empate
        result = self.__chess__.__check_victory__()
        self.assertEqual(result, "Draw")

    def test_victory_status_returned(self):
        # Simular un escenario donde las negras ganan
        board = self.__chess__.__get_board__()
        board.__clear_board__()  # Limpiar todas las piezas
    
        # Colocar solo una torre negra en el tablero
        board.__place_piece__(Rook("black"), (0, 4))
    
        # Verificar si el juego termina con victoria para las negras
        result = self.__chess__.__check_victory__()
        self.assertEqual(result, "Black wins")

    def simulate_victory(self, king_color, expected_result):
        board = self.__chess__.__get_board__()
        board.__clear_board__()
    
        # Colocar el rey del color especificado
        king = King(king_color)
        row = 7 if king_color == "white" else 0
        board.__place_piece__(king, (row, 4))  # Solo coloca al rey
    
        # El resultado debe ser que el otro jugador gana
        result = self.__chess__.__check_victory__()
        self.assertEqual(result, expected_result)

    def test_victory_white_wins(self):
        # Simular victoria de las blancas (rey blanco, sin piezas negras)
        self.simulate_victory("white", "White wins")

    def test_victory_black_wins(self):
        # Simular victoria de las negras (rey negro, sin piezas blancas)
        self.simulate_victory("black", "Black wins")

    def test_move_returns_status(self):
        # Configura el tablero con varias piezas para evitar la condición de victoria
        board = self.__chess__.__get_board__()
        board.__clear_board__()
        board.__place_piece__(Pawn("white"), (6, 4))  # Colocar un peón blanco en (6, 4)
        board.__place_piece__(King("black"), (0, 4))  # Colocar el rey negro para evitar que gane inmediatamente
        board.__place_piece__(King("white"), (7, 4))  # Colocar el rey blanco

        # Mover el peón de (6, 4) a (5, 4)
        status = self.__chess__.__move__("6 4", "5 4")

        # Verificar que el movimiento fue exitoso y se retornó un estado
        self.assertIsNotNone(status)
        self.assertEqual(status, "Move successful")  

    def test_move_returns_victory_status(self):
        board = self.__chess__.__get_board__()
        board.__clear_board__()

        # Colocar piezas en el tablero
        board.__place_piece__(Rook("black"), (0, 4))  # Torre negra
        board.__place_piece__(King("white"), (7, 4))  # Rey blanco
        board.__place_piece__(Pawn("white"), (6, 0))  # Peón blanco

        # Mover el peón blanco para cambiar de turno
        self.__chess__.__move__("6 0", "5 0")  # Movimiento exitoso del peón blanco

        # Mover la torre negra para capturar al rey blanco
        status = self.__chess__.__move__("0 4", "7 4")  # Movimiento de la torre negra

        # Verificar que el movimiento retorna "Black wins"
        self.assertEqual(status, "Black wins")

    def test_move_returns_draw_status(self):
        board = self.__chess__.__get_board__()
        board.__clear_board__()

        # Colocar solo los dos reyes para generar un empate
        board.__place_piece__(King("white"), (7, 4))  # Rey blanco
        board.__place_piece__(King("black"), (0, 4))  # Rey negro

        # Realizar cualquier movimiento que no cambie la situación de empate
        status = self.__chess__.__move__("7 4", "6 4")  # Mover al rey blanco

        # Verificar que el movimiento retorna "Draw"
        self.assertEqual(status, "Draw")

    def test_load_nonexistent_game(self):
        game_id = "nonexistent_game_id"
        output = self.__chess__.__load_game__(game_id)  # Llama al método que ahora devuelve un mensaje
        self.assertEqual(output, f"No se encontró ninguna partida con el ID: {game_id}")

if __name__ == '__main__':
    unittest.main()
