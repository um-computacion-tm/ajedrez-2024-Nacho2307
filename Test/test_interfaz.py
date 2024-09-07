import unittest
from Juego.Interfaz import Interfaz

class TestInterfaz(unittest.TestCase):

    def setUp(self):
        self.interfaz = Interfaz()

    def _simulate_input_output(self, inputs, target_function, expected_output):
        """
        Simula la entrada y salida para una función objetivo y verifica el resultado esperado.
        """
        import io
        import sys
        # Simula la entrada del usuario
        input_backup = sys.stdin
        sys.stdin = io.StringIO(inputs)
        output_backup = sys.stdout
        sys.stdout = io.StringIO()
        
        # Ejecuta la función objetivo
        target_function()
        
        # Restaurar la entrada y salida estándar
        sys.stdin = input_backup
        output = sys.stdout.getvalue()
        sys.stdout = output_backup
        
        # Verifica el resultado esperado
        self.assertIn(expected_output, output)

    def test_solicitar_movimiento(self):
        self._simulate_input_output('6 0 5 0\n', self.interfaz.solicitar_movimiento, "Movimiento válido.")

    def test_iniciar_juego(self):
        self._simulate_input_output('1\nq\n', self.interfaz.iniciar_juego, "Juego terminado.")

    def test_main(self):
        self._simulate_input_output('2\n', self.interfaz.main, "Gracias por jugar. ¡Crack!")

if __name__ == '__main__':
    unittest.main()