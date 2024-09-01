import unittest
import io
import sys
from Juego.Chess import Chess
from Juego.Exception import *
from Juego.Interfaz import Interfaz

class TestInterfaz(unittest.TestCase):
    def setUp(self):
        self.interfaz = Interfaz()

    def _simulate_input(self, input_string, function_to_test):
        """
        Simula la entrada del usuario y la salida estándar para una función específica.
        """
        input_backup = sys.stdin
        sys.stdin = io.StringIO(input_string)
        output_backup = sys.stdout
        sys.stdout = io.StringIO()
        
        try:
            function_to_test()
            output = sys.stdout.getvalue()
        finally:
            sys.stdin = input_backup
            sys.stdout = output_backup
        
        return output

    def test_solicitar_movimiento(self):
        # Simula la entrada del usuario para que ingrese un movimiento válido
        output = self._simulate_input('6 0 5 0\n', lambda: self.interfaz.solicitar_movimiento())
    
        # Verifica si el movimiento se procesa correctamente
        self.assertTrue(self.interfaz._chess_.__board__.get_piece(6, 0).movimiento_correcto(6, 0, 5, 0, self.interfaz._chess_.__board__))

    def test_iniciar_juego(self):
        # Simula la entrada del usuario para elegir la opción de iniciar el juego y luego salir
        output = self._simulate_input('1\nq\n', self.interfaz.iniciar_juego)
        
        # Verifica que el mensaje de "Juego terminado" esté en la salida
        self.assertIn("Juego terminado.", output)

    def test_main(self):
        # Simula la entrada del usuario para seleccionar la opción de salir
        output = self._simulate_input('2\n', self.interfaz.main)
    
        # Verifica si el mensaje de salida está presente en la salida
        self.assertIn("Gracias por jugar. ¡Crack!", output)

if __name__ == '__main__':
    unittest.main()
