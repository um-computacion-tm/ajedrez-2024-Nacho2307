import unittest
from Juego.chess import Chess
from Juego.board import Board
from Juego.exception import (
    InvalidMoveException,
    OutOfBoundsException,
    PieceAlreadyCapturedException,
    ColorException,
    TurnException
)
from Juego.Piezas.rook import Rook
from Juego.Piezas.king import King
from Juego.Piezas.pawn import Pawn

class TestChess(unittest.TestCase):
    """
    Clase de pruebas para la clase Chess en el juego de ajedrez.
    Verifica que las funcionalidades del juego se comporten según lo esperado.
    """

    def setUp(self):
        """Inicializa una nueva partida de ajedrez para cada prueba."""
        self.__chess__ = Chess()

    def test_load_game(self):
        """Verifica que se pueda cargar un juego guardado correctamente."""
        self.__chess__.__get_board__().__place_piece__(King("white"), (7, 4))
        self.__chess__.__get_board__().__place_piece__(Rook("black"), (0, 4))
        self.__chess__.__save_game__("test_game")

        new_chess = Chess()
        new_chess.__load_game__("test_game")

        # Verificar que el estado del tablero y el turno sean correctos
        self.assertIsNotNone(new_chess.__get_board__().__get_piece__(7, 4))  # Rey blanco en (7, 4)
        self.assertIsNotNone(new_chess.__get_board__().__get_piece__(0, 4))  # Torre negra en (0, 4)
        self.assertEqual(new_chess.__get_turn__(), "WHITE")  # El turno debe ser blanco

    def test_invalid_move_king_in_check(self):
        """Verifica que no se pueda mover una pieza que deja al rey en jaque."""
        self.__chess__.__get_board__().__place_piece__(King("white"), (7, 4))  # Coloca el rey blanco
        self.__chess__.__get_board__().__place_piece__(Rook("black"), (0, 4))  # Coloca una torre negra que amenaza al rey
        with self.assertRaises(InvalidMoveException):
            self.__chess__.__move__("7 4", "6 4")  # Intentar mover al rey blanco deja al rey en jaque

    def test_piece_already_captured(self):
        """Verifica que se lance una excepción al intentar mover desde una posición vacía."""
        with self.assertRaises(PieceAlreadyCapturedException):
            self.__chess__.__move__("3 3", "4 3")

    def test_out_of_bounds_position(self):
        """Verifica que se lancen excepciones al intentar mover a posiciones fuera de los límites."""
        with self.assertRaises(OutOfBoundsException):
            self.__chess__.__move__("0 0", "9 0")  # Movimiento fuera de los límites

        with self.assertRaises(ValueError):
            self.__chess__.__move__("a b", "2 2")  # Entrada inválida de formato

    def test_change_turn_back_and_forth(self):
        """Verifica el cambio de turnos entre jugadores."""
        self.assertEqual(self.__chess__.__get_turn__(), "WHITE")
        self.__chess__.__get_board__().__place_piece__(Pawn("white"), (6, 0)) 
        self.__chess__.__move__("6 0", "5 0")  # Mover un peón blanco
        self.assertEqual(self.__chess__.__get_turn__(), "BLACK")
        self.__chess__.__get_board__().__place_piece__(Pawn("black"), (1, 0))  
        self.__chess__.__move__("1 0", "2 0")  # Mover un peón negro
        self.assertEqual(self.__chess__.__get_turn__(), "WHITE")

    def test_draw(self):
        """Verifica que la partida termine en empate con solo los dos reyes en el tablero."""
        board = self.__chess__.__get_board__()
        board.__clear_board__()  # Limpiar el tablero

        # Colocar solo los dos reyes en el tablero
        board.__place_piece__(King("white"), (7, 4))  # Rey blanco
        board.__place_piece__(King("black"), (0, 4))  # Rey negro

        # Verificar si el juego termina en empate
        result = self.__chess__.__check_victory__()
        self.assertEqual(result, "Draw")

    def test_victory_status_returned(self):
        """Verifica que el juego retorne el estado de victoria correctamente."""
        board = self.__chess__.__get_board__()
        board.__clear_board__()  # Limpiar todas las piezas
    
        # Colocar solo una torre negra en el tablero
        board.__place_piece__(Rook("black"), (0, 4))
    
        # Verificar si el juego termina con victoria para las negras
        result = self.__chess__.__check_victory__()
        self.assertEqual(result, "Black wins")

    def simulate_victory(self, king_color, expected_result):
        """Simula un escenario de victoria y verifica el resultado esperado."""
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
        """Simula la victoria de las blancas."""
        self.simulate_victory("white", "White wins")

    def test_victory_black_wins(self):
        """Simula la victoria de las negras."""
        self.simulate_victory("black", "Black wins")

    def test_move_returns_status(self):
        """Verifica que se retorne el estado correcto al mover una pieza."""
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
        """Verifica que se retorne el estado de victoria al mover una pieza."""
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
        """Verifica que se retorne el estado de empate al mover piezas de manera adecuada."""
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
        """Verifica que se maneje correctamente la carga de un juego inexistente."""
        game_id = "nonexistent_game_id"
        output = self.__chess__.__load_game__(game_id)  # Llama al método que ahora devuelve un mensaje
        self.assertEqual(output, f"No se encontró ninguna partida con el ID: {game_id}")

    def test_move_piece_of_different_color(self):
        """Verifica que no se pueda mover una pieza de color diferente al turno actual."""
        self.__chess__.__get_board__().__place_piece__(King("white"), (7, 4))  # Rey blanco
        self.__chess__.__get_board__().__place_piece__(Pawn("black"), (6, 4))  # Peón negro

        # Intentar mover el peón negro cuando es el turno del blanco
        with self.assertRaises(ColorException):
            self.__chess__.__move__("6 4", "5 4")  # Intentar mover el peón negro

if __name__ == '__main__':
    unittest.main()
