import unittest
from colorama import Fore, Style
from unittest.mock import patch, MagicMock
import io
from Juego.interfaz import ChessInterface
from Juego.exception import ChessException

class TestChessInterface(unittest.TestCase):

    def setUp(self):
        self.interface = ChessInterface()

    def simulate_input(self, inputs):
        return patch('builtins.input', side_effect=inputs)

    def capture_output(self):
        return patch('sys.stdout', new=io.StringIO())

    def check_draw_response(self, response, expected_result):
        with self.simulate_input([response]):
            result = self.interface.__handle_draw__()
            self.assertEqual(result, expected_result)

    def check_handle_option(self, option, method, return_value, expected_result):
        with patch.object(self.interface, method, return_value=return_value) as mock_method:
            result = self.interface.__handle_option__(option)
            mock_method.assert_called_once()
            self.assertEqual(result, expected_result)

    def check_load_game(self, side_effect, expected_message, expected_result):
        with patch.object(self.interface.__chess__, '__load_game__', side_effect=side_effect):
            with self.simulate_input(['test_game_id']):
                with self.capture_output() as fake_stdout:
                    result = self.interface.__handle_option__('6')
                    output = fake_stdout.getvalue()
                    self.assertIn(expected_message, output)
                    self.assertEqual(result, expected_result)

    def check_output(self, method, expected_string):
        with self.capture_output() as fake_stdout:
            method()
            output = fake_stdout.getvalue()
            self.assertIn(expected_string, output)

    def test_get_move_positions(self):
        with patch('builtins.input', side_effect=['2 3', '4 5']):
            from_pos, to_pos = self.interface.__get_move_positions__()
            self.assertEqual(from_pos, '2 3')
            self.assertEqual(to_pos, '4 5')

    def test_handle_draw(self):
        # Test for drawing responses
        self.check_draw_response('y', True)
        self.check_draw_response('n', False)

        # Test invalid response
        with self.simulate_input(['maybe', 'y']):
            with self.capture_output() as fake_stdout:
                result = self.interface.__handle_draw__()
                output = fake_stdout.getvalue()
                self.assertIn("Respuesta inválida. Intenta de nuevo.", output)
                self.assertTrue(result)

    def test_handle_surrender(self):
        with self.capture_output() as fake_stdout:
            self.interface.__handle_surrender__()
            output = fake_stdout.getvalue()
            self.assertIn("ha decidido rendirse", output)
            self.assertIn("¡El otro jugador es el campeón!", output)

    def test_save_game(self):
        with self.simulate_input(['test_game_id']):
            with self.capture_output() as fake_stdout:
                self.interface.__save_game__()
                output = fake_stdout.getvalue()
                self.assertIn("Partida guardada con ID: test_game_id", output)

    def test_display_board(self):
        tablero = self.interface.__chess__.__get_board__().__mostrar_coords__()
        self.assertIn("♖", tablero)
        self.assertIn("0", tablero)

    def test_show_scores_and_instructions(self):
        # Test for showing scores and instructions
        self.check_output(self.interface.__show_scores__, "Puntuaciones actuales:")
        self.check_output(self.interface.__show_instructions__, "Instrucciones del juego de Ajedrez:")

    def test_display_turn_and_dramatic_message(self):
        # Test for displaying turn and dramatic message
        self.check_output(self.interface.__display_turn__, "Turno de")
        message = "Prueba"
        with self.capture_output() as fake_stdout:
            self.interface.__dramatic_message__(message)
            output = fake_stdout.getvalue()
            self.assertIn(message, output)

    @patch('Juego.interfaz.ChessInterface.__display_board__')
    @patch('Juego.interfaz.ChessInterface.__display_turn__')
    @patch('Juego.interfaz.ChessInterface.__get_user_option__', side_effect=['1', '3'])
    @patch('Juego.interfaz.ChessInterface.__handle_option__', side_effect=[False, True])
    def test_main_game_loop(self, mock_handle_option, mock_get_user_option, mock_display_turn, mock_display_board):
        self.interface.__start__()
        mock_display_board.assert_called_once()
        self.assertTrue(mock_display_turn.called)
        self.assertEqual(mock_get_user_option.call_count, 2)
        self.assertEqual(mock_handle_option.call_count, 2)
        mock_handle_option.assert_any_call('1')
        mock_handle_option.assert_any_call('3')

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_option(self, mock_input):
        result = self.interface.__get_user_option__()
        self.assertEqual(result, '1')

    def test_handle_option(self):
        # Test for handling various options
        self.check_handle_option('1', '__handle_move__', None, False)
        self.check_handle_option('2', '__handle_draw__', True, True)
        self.check_handle_option('3', '__handle_surrender__', None, True)
        self.check_handle_option('7', '__show_scores__', None, False)
        self.check_handle_option('4', '__show_instructions__', None, False)
        self.check_handle_option('5', '__save_game__', None, False)

    def test_handle_option_load_game(self):
        with patch.object(self.interface.__chess__, '__load_game__') as mock_load_game:
            with self.simulate_input(['test_game_id']):
                with self.capture_output() as fake_stdout:
                    result = self.interface.__handle_option__('6')
                    mock_load_game.assert_called_once_with('test_game_id')
                    output = fake_stdout.getvalue()
                    self.assertIn("Partida cargada con éxito.", output)

    def test_handle_option_load_game_exceptions(self):
        # Test for loading game exceptions
        self.check_load_game(ChessException("Error de carga"),
                            "Error al cargar la partida: Error de carga",
                            False)
        self.check_load_game(Exception("Error inesperado"),
                            "Error inesperado: Error inesperado",
                            False)

    def test_handle_move_unexpected_exception(self):
        with patch.object(self.interface, '__get_move_positions__', return_value=('1', '1')), \
                patch.object(self.interface.__chess__, '__move__', side_effect=Exception("Error inesperado")):
            with self.capture_output() as fake_stdout:
                self.interface.__handle_move__()
                output = fake_stdout.getvalue()
                self.assertIn("Error inesperado: Error inesperado", output)

    def test_process_move_messages(self):
        # Test for processing move messages
        with patch.object(self.interface.__chess__, '__move__', return_value="¡Victoria!"), \
                self.capture_output() as fake_stdout:
            self.interface.__process_move__('1', '1')
            output = fake_stdout.getvalue()
            self.assertIn("¡Victoria!", output)

        with patch.object(self.interface.__chess__, '__move__', return_value=None):
            with self.capture_output() as fake_stdout:
                with patch.object(self.interface, '__display_board__') as mock_display_board, \
                        patch.object(self.interface, '__show_scores__') as mock_show_scores:
                    self.interface.__process_move__('1', '1')
                    output = fake_stdout.getvalue()
                    self.assertIn("Movimiento realizado con éxito.", output)
                    mock_display_board.assert_called_once()
                    mock_show_scores.assert_called_once()

        with patch.object(self.interface.__chess__, '__move__', side_effect=ChessException("Movimiento no válido.")):
            with self.capture_output() as fake_stdout:
                result = self.interface.__process_move__('1', '1')
                output = fake_stdout.getvalue()
                self.assertFalse(result)
                self.assertIn("Error: Movimiento no válido.", output)

if __name__ == '__main__':
    unittest.main()
