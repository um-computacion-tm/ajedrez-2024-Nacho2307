import unittest
from unittest.mock import patch
from io import StringIO
from Juego.Interfaz import ChessInterface
from Juego.Exception import ChessException

class TestChessInterface(unittest.TestCase):

    def setUp(self):
        # Inicializa una instancia de ChessInterface antes de cada prueba.
        self.interface = ChessInterface()

    def get_output_from_interface(self, inputs):
        # Ejecuta la interfaz con una lista de entradas simuladas y retorna la salida.
        with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.interface.__start__()
            return mock_stdout.getvalue()

    def simulate_move_exception(self, exception_type, message, expected_output):
        with patch('Juego.Interfaz.Chess.__move__', side_effect=exception_type(message)):
            output = self.get_output_from_interface(['1', '1 2', '1 3', '3'])
            self.assertIn(expected_output, output)

    def test_process_move_exception(self):
        # Prueba para simular una excepción específica del movimiento de ajedrez.
        self.simulate_move_exception(ChessException, "Error de movimiento", "Error: Error de movimiento")

    def test_process_move_unexpected_exception(self):
        # Prueba para simular una excepción inesperada durante el movimiento.
        self.simulate_move_exception(Exception, "Error inesperado", "Error inesperado: Error inesperado")

    def test_invalid_move(self):
        # Prueba para simular un movimiento inválido.
        output = self.get_output_from_interface(['1', '1 1', '6 0', '3'])
        self.assertIn("Error: No se puede mover una pieza de un color diferente.", output)

    def test_movement_and_surrender(self):
        # Prueba para simular un movimiento básico y luego la rendición de un jugador.
        output = self.get_output_from_interface(['1', '1 2', '1 3', '3'])
        self.assertIn("Turno de WHITE.", output)
        self.assertIn("WHITE ha decidido rendirse...", output)
        self.assertIn("¡El otro jugador es el campeón!", output)

    def test_offer_draw(self):
        # Prueba para simular la oferta de tablas y la aceptación.
        output = self.get_output_from_interface(['2', 'y'])
        self.assertIn("Juego empatado.", output)

    def test_reject_draw(self):
        # Prueba para simular la oferta de tablas y el rechazo.
        output = self.get_output_from_interface(['2', 'n', '3'])  
        self.assertIn("Tablas rechazadas.", output)

    def test_invalid_option(self):
        # Prueba para simular una opción inválida y asegurar que el sistema maneje el error.
        output = self.get_output_from_interface(['5', '1', '1 2', '1 3', '3'])
        self.assertIn("Opción inválida, intenta de nuevo.", output)
        self.assertIn("Turno de WHITE.", output)

    def test_process_move_victory(self):
        # Simula un movimiento que devuelve un resultado de victoria.
        with patch('Juego.Interfaz.Chess.__move__', return_value="Black wins"):
            output = self.get_output_from_interface(['1', '1 2', '1 3', '3'])
            self.assertIn("Black wins", output)

    def test_invalid_draw_response(self):
        # Simula una respuesta inválida seguida por la aceptación de tablas.
        output = self.get_output_from_interface(['2', 'invalid', 'y'])
        self.assertIn("Respuesta inválida. Intenta de nuevo.", output)
        self.assertIn("Juego empatado.", output)

    def test_display_board_after_successful_move(self):
        # Simula un movimiento exitoso y verifica que el tablero se muestra después.
        with patch('Juego.Interfaz.Chess.__move__', return_value=None):
            output = self.get_output_from_interface(['1', '1 2', '1 3', '3'])
            self.assertIn("Movimiento realizado con éxito.", output)
            self.assertIn("0 1 2 3 4 5 6 7", output)

    def test_show_instructions(self):
        # Simula la selección de la opción '4' para mostrar las instrucciones y luego salir con la opción '3'
        output = self.get_output_from_interface(['4', '3'])
        self.assertIn("Instrucciones del juego de Ajedrez", output)
        self.assertIn("Tablero de juego", output)
        self.assertIn("Piezas del juego", output)
        self.assertIn("Jugabilidad", output)

    def test_load_game(self, exception=None, message=None, expected_output=None):
        # Simula la carga de una partida, manejando excepciones según sea necesario.
        if exception is None:
            with patch('Juego.Interfaz.Chess.__load_game__', return_value=None):
                output = self.get_output_from_interface(['6', 'partida123', '3'])  # Usa un ID de partida simulado y luego salir.
                self.assertIn("Partida cargada con éxito.", output)
                self.assertIn("0 1 2 3 4 5 6 7", output) 
        else:
            with patch('Juego.Interfaz.Chess.__load_game__', side_effect=exception(message)):
                output = self.get_output_from_interface(['6', 'partida123', '3'])  # Usa un ID de partida simulado y luego salir.
                self.assertIn(expected_output, output)

    def test_load_game_success(self):
        self.test_load_game()

    def test_load_game_chess_exception(self):
        self.test_load_game(ChessException, "Error de carga", "Error al cargar la partida: Error de carga")

    def test_load_game_unexpected_exception(self):
        self.test_load_game(Exception, "Error inesperado", "Error inesperado: Error inesperado")

    def test_show_scores(self):
        # Simula la selección de la opción '7' para mostrar las puntuaciones.
        output = self.get_output_from_interface(['7', '3'])  # Selecciona mostrar puntajes y luego salir
        self.assertIn("Puntuaciones actuales:", output)  # Verifica que las puntuaciones se muestren correctamente

if __name__ == '__main__':
    unittest.main()