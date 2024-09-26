import unittest
from io import StringIO
import sys
from unittest.mock import patch
from Juego.Interfaz import ChessInterface

class TestChessInterface(unittest.TestCase):
    
    def setUp(self):
        # Redirige la salida estándar para capturar las impresiones de la interfaz
        self.held_output = StringIO()
        sys.stdout = self.held_output
        self.interface = ChessInterface()
    
    def tearDown(self):
        # Restaura la salida estándar
        sys.stdout = sys.__stdout__

    def test_display_board(self):
        # Verifica que el tablero se imprime correctamente al iniciar el juego
        self.interface.__display_board__()
        output = self.held_output.getvalue()
        # Verifica si la salida contiene las coordenadas del tablero
        self.assertIn("0 1 2 3 4 5 6 7", output)
    
    def test_show_instructions(self):
        # Verifica que las instrucciones se muestran correctamente
        self.interface.__show_instructions__()
        output = self.held_output.getvalue()
        # Verifica si la salida contiene las instrucciones
        self.assertIn("Instrucciones del juego de Ajedrez", output)
    
    def test_handle_surrender(self):
        # Verifica que el mensaje de rendición se muestra correctamente
        self.interface.__handle_surrender__()
        output = self.held_output.getvalue()
        # Verifica si se muestra el mensaje de rendición
        self.assertIn("ha decidido rendirse", output)
    
    def test_handle_player_action_invalid_move(self):
        # Simula un movimiento inválido y verifica que se muestra el mensaje de error
        input_values = ['1 0 2 0', '1 1 2 2', '7 7 7 6']
        def mock_input(s):
            return input_values.pop(0)

        self.interface.__process_move__ = mock_input

        try:
            self.interface.__handle_player_action__()
        except Exception as e:
            output = str(e)
            self.assertIn("Error inesperado", output)
    
    def test_start_game(self):
        # Verifica que se inicie el juego correctamente
        self.interface.__start_game__()
        output = self.held_output.getvalue()
        self.assertIn("¡Bienvenido al juego de Ajedrez!", output)

    def test_game_loop_options(self):
        input_values = ['4', '3']
        
        def mock_input(s):
            return input_values.pop(0)
        
        self.interface.input = mock_input
        self.interface.__start__()

        output = self.held_output.getvalue()
        self.assertIn("Instrucciones del juego de Ajedrez", output)
        self.assertIn("ha decidido rendirse", output)

if __name__ == "__main__":
    unittest.main()