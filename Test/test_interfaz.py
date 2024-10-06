import unittest
from colorama import Fore, Style
from unittest.mock import patch, MagicMock
import io
from Juego.interfaz import ChessInterface
from Juego.exception import ChessException

class TestChessInterface(unittest.TestCase):
    """
    Clase de pruebas para la interfaz del juego de ajedrez.
    Verifica que las interacciones de la interfaz se comporten según lo esperado.
    """

    def setUp(self):
        """Inicializa una nueva instancia de la interfaz de ajedrez para cada prueba."""
        self.interface = ChessInterface()

    def simulate_input(self, inputs):
        """Simula la entrada del usuario."""
        return patch('builtins.input', side_effect=inputs)

    def capture_output(self):
        """Captura la salida de la consola."""
        return patch('sys.stdout', new=io.StringIO())

    def check_handle_option(self, option, method, return_value, expected_result):
        """Verifica que la opción seleccionada se maneje correctamente."""
        with patch.object(self.interface, method, return_value=return_value) as mock_method:
            result = self.interface.__handle_option__(option)
            mock_method.assert_called_once()
            self.assertEqual(result, expected_result)

    def check_load_game(self, side_effect, expected_message, expected_result):
        """Verifica la carga de una partida desde la interfaz."""
        with patch.object(self.interface.__chess__, '__load_game__', side_effect=side_effect):
            with self.simulate_input(['test_game_id']):
                with self.capture_output() as fake_stdout:
                    result = self.interface.__handle_option__('6')
                    output = fake_stdout.getvalue()
                    self.assertIn(expected_message, output)
                    self.assertEqual(result, expected_result)

    def test_get_move_positions(self):
        """Verifica que se obtengan correctamente las posiciones de movimiento."""
        with patch('builtins.input', side_effect=['2 3', '4 5']):
            from_pos, to_pos = self.interface.__get_move_positions__()
            self.assertEqual(from_pos, '2 3')
            self.assertEqual(to_pos, '4 5')

    def test_handle_draw(self):
        """Verifica que se manejen correctamente las respuestas sobre tablas."""
        with self.simulate_input(['y']):
            result = self.interface.__handle_draw__()
            self.assertTrue(result)
        
        with self.simulate_input(['n']):
            result = self.interface.__handle_draw__()
            self.assertFalse(result)

        # Test respuesta inválida
        with self.simulate_input(['maybe', 'y']):
            with self.capture_output() as fake_stdout:
                result = self.interface.__handle_draw__()
                output = fake_stdout.getvalue()
                self.assertIn("Respuesta inválida. Intenta de nuevo.", output)
                self.assertTrue(result)

    def test_handle_surrender(self):
        """Verifica que se maneje correctamente la rendición del jugador."""
        with self.capture_output() as fake_stdout:
            self.interface.__handle_surrender__()
            output = fake_stdout.getvalue()
            self.assertIn("ha decidido rendirse", output)
            self.assertIn("¡El otro jugador es el campeón!", output)

    def test_save_game(self):
        """Verifica que se guarde correctamente una partida."""
        game_id = 'test_game_id'
    
        with self.simulate_input([game_id]):
            with self.capture_output() as fake_stdout:
                self.interface.__save_game__()
                output = fake_stdout.getvalue()
                self.assertIn(f"Partida guardada con ID: {game_id}", output)

    def test_display_board(self):
        """Verifica que el tablero se muestre correctamente."""
        tablero = self.interface.__chess__.__get_board__().__mostrar_coords__()
        self.assertIn("♖", tablero)
        self.assertIn("0", tablero)

    def test_show_scores_and_instructions(self):
        """Verifica que se muestren correctamente las puntuaciones e instrucciones."""
        with self.capture_output() as fake_stdout:
            self.interface.__show_scores__()
            output = fake_stdout.getvalue()
            self.assertIn("Puntuaciones actuales:", output)
        
        with self.capture_output() as fake_stdout:
            self.interface.__show_instructions__()
            output = fake_stdout.getvalue()
            self.assertIn("Instrucciones del juego de Ajedrez:", output)

    def test_display_turn_and_dramatic_message(self):
        """Verifica que se muestre correctamente el turno y los mensajes dramáticos."""
        with self.capture_output() as fake_stdout:
            self.interface.__display_turn__()
            output = fake_stdout.getvalue()
            self.assertIn("Turno de", output)
        
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
        """Verifica que el bucle principal del juego funcione correctamente."""
        self.interface.__start__()
        mock_display_board.assert_called_once()
        self.assertTrue(mock_display_turn.called)
        self.assertEqual(mock_get_user_option.call_count, 2)
        self.assertEqual(mock_handle_option.call_count, 2)
        mock_handle_option.assert_any_call('1')
        mock_handle_option.assert_any_call('3')

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_option(self, mock_input):
        """Verifica que se obtenga correctamente la opción del usuario."""
        result = self.interface.__get_user_option__()
        self.assertEqual(result, '1')

    def test_handle_option(self):
        """Verifica que se manejen correctamente varias opciones del menú."""
        self.check_handle_option('1', '__handle_move__', None, False)
        self.check_handle_option('2', '__handle_draw__', True, True)
        self.check_handle_option('3', '__handle_surrender__', None, True)
        self.check_handle_option('7', '__show_scores__', None, False)
        self.check_handle_option('4', '__show_instructions__', None, False)
        self.check_handle_option('5', '__save_game__', None, False)

    def test_handle_option_load_game(self):
        """Verifica que se cargue correctamente una partida desde el menú."""
        with patch.object(self.interface.__chess__, '__load_game__') as mock_load_game:
            with self.simulate_input(['test_game_id']):
                with self.capture_output() as fake_stdout:
                    result = self.interface.__handle_option__('6')
                    mock_load_game.assert_called_once_with('test_game_id')
                    output = fake_stdout.getvalue()
                    self.assertIn("Partida cargada con éxito.", output)

    def test_handle_option_load_game_exceptions(self):
        """Verifica el manejo de excepciones al cargar partidas."""
        self.check_load_game(ChessException("Error de carga"),
                            "Error al cargar la partida: Error de carga",
                            False)
        self.check_load_game(Exception("Error inesperado"),
                            "Error inesperado: Error inesperado",
                            False)

    def test_handle_move_unexpected_exception(self):
        """Verifica el manejo de excepciones inesperadas al mover una pieza."""
        with patch.object(self.interface, '__get_move_positions__', return_value=('1', '1')), \
            patch.object(self.interface.__chess__, '__move__', side_effect=Exception("Error inesperado")):
            with self.capture_output() as fake_stdout:
                self.interface.__handle_move__()
                output = fake_stdout.getvalue()
                self.assertIn("Error inesperado: Error inesperado", output)

    def test_process_move_messages(self):
        """Verifica los mensajes generados al procesar un movimiento."""
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
