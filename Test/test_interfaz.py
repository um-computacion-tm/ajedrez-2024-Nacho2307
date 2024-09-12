from unittest.mock import patch
from io import StringIO
import unittest
from Juego.Interfaz import ChessInterface
from Juego.Exception import ChessException

class TestChessInterface(unittest.TestCase):

    def setUp(self):
        # Inicializa una instancia de ChessInterface antes de cada prueba.
        self.interface = ChessInterface()

    def get_output_from_interface(self, inputs):
        # Ejecuta la interfaz con una lista de entradas simuladas y retorna la salida.
        with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.interface.start()
            return mock_stdout.getvalue()

    def test_invalid_move(self):
        # Prueba para simular un movimiento inválido.
        output = self.get_output_from_interface(['1', '1 1', '8 8', '3'])
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
        output = self.get_output_from_interface(['2', 'n', '3'])  # Asegúrate de incluir más entradas si es necesario.
        self.assertIn("Tablas rechazadas.", output)

    def test_invalid_option(self):
        # Prueba para simular una opción inválida y asegurar que el sistema maneje el error.
        output = self.get_output_from_interface(['5', '1', '1 2', '1 3', '3'])
        self.assertIn("Opción inválida, intenta de nuevo.", output)
        self.assertIn("Turno de WHITE.", output)  # Verifica que el flujo continúa correctamente

    def test_process_move_exception(self):
        # Prueba para simular una excepción durante el movimiento.
        with patch('Juego.Interfaz.Chess.move', side_effect=ChessException("Error de movimiento")):
            output = self.get_output_from_interface(['1', '1 2', '1 3', '3'])
            self.assertIn("Error: Error de movimiento", output)

    def test_process_move_unexpected_exception(self):
        # Prueba para simular una excepción inesperada durante el movimiento.
        with patch('Juego.Interfaz.Chess.move', side_effect=Exception("Error inesperado")):
            output = self.get_output_from_interface(['1', '1 2', '1 3', '3'])
            self.assertIn("Error inesperado: Error inesperado", output)

    def test_process_move_victory(self):
        # Simula un movimiento que devuelve un resultado de victoria.
        with patch('Juego.Interfaz.Chess.move', return_value="Black wins"):
            output = self.get_output_from_interface(['1', '1 2', '1 3', '3'])
            self.assertIn("Black wins", output)  # Verifica que el resultado de victoria se imprime.

    def test_invalid_draw_response(self):
        # Simula una respuesta inválida seguida por la aceptación de tablas.
        output = self.get_output_from_interface(['2', 'invalid', 'y'])
        self.assertIn("Respuesta inválida. Intenta de nuevo.", output)
        self.assertIn("Juego empatado.", output)

    def test_display_board_after_successful_move(self):
        # Simula un movimiento exitoso y verifica que el tablero se muestra después.
        with patch('Juego.Interfaz.Chess.move', return_value=None):  # Simula que el movimiento es exitoso
            output = self.get_output_from_interface(['1', '1 2', '1 3', '3'])
            self.assertIn("Movimiento realizado con éxito.", output)  # Verifica que el mensaje de éxito se imprime
            self.assertIn("0 1 2 3 4 5 6 7", output)  # Verifica que el tablero se imprime después del movimiento

    def test_show_instructions(self):
        # Simula la selección de la opción '4' para mostrar las instrucciones y luego salir con la opción '3'
        output = self.get_output_from_interface(['4', '3'])  # Agrega '3' para rendirse después de mostrar las instrucciones
        self.assertIn("Instrucciones del juego de Ajedrez", output)  # Verifica que las instrucciones se imprimen
        self.assertIn("Tablero de juego", output)  # Verifica que se menciona el tablero
        self.assertIn("Piezas del juego", output)  # Verifica que se mencionan las piezas
        self.assertIn("Jugabilidad", output)  # Verifica que se menciona la jugabilidad

if __name__ == '__main__':
    unittest.main()
