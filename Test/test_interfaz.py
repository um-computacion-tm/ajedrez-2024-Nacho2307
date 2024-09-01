import unittest
from Juego.Chess import Chess
from Juego.Exception import *
from Juego.Interfaz import Interfaz

class TestInterfaz(unittest.TestCase):
    def setUp(self):
        self.interfaz = Interfaz()

    def test_solicitar_movimiento(self):
        import io
        import sys
    # Simula la entrada del usuario para que ingrese un movimiento válido
        input_backup = sys.stdin
        sys.stdin = io.StringIO('6 0 5 0\n')
        output_backup = sys.stdout
        sys.stdout = io.StringIO()
    
        from_input, to_input = self.interfaz.solicitar_movimiento()
    
    # Restaurar la entrada y salida estándar
        sys.stdin = input_backup
        output = sys.stdout.getvalue()
        sys.stdout = output_backup
    
    # Verifica si el movimiento se procesa correctamente
        self.assertTrue(self.interfaz._chess_.__board__.get_piece(6, 0).movimiento_correcto(6, 0, 5, 0, self.interfaz._chess_.__board__))


    def test_iniciar_juego(self):
        import io
        import sys
        # Simula la entrada del usuario para elegir la opción de iniciar el juego y luego salir
        input_backup = sys.stdin
        sys.stdin = io.StringIO('1\nq\n')
        output_backup = sys.stdout
        sys.stdout = io.StringIO()
        
        # Ejecuta el método iniciar_juego
        self.interfaz.iniciar_juego()
        
        # Restaurar la entrada y salida estándar
        sys.stdin = input_backup
        output = sys.stdout.getvalue()
        sys.stdout = output_backup
        
        # Verifica que el mensaje de "Juego terminado" esté en la salida
        self.assertIn("Juego terminado.", output)

    def test_main(self):
        import io
        import sys
     # Simula la entrada del usuario para seleccionar la opción de salir
        input_backup = sys.stdin
        sys.stdin = io.StringIO('2\n')  # Opciones: 1 para jugar, 2 para salir
        output_backup = sys.stdout
        sys.stdout = io.StringIO()
    
        self.interfaz.main()
    
    # Restaurar la entrada y salida estándar
        sys.stdin = input_backup
        output = sys.stdout.getvalue()
        sys.stdout = output_backup
    
    # Verifica si el mensaje de salida está presente en la salida
        self.assertIn("Gracias por jugar. ¡Crack!", output)


if __name__ == '__main__':
    unittest.main()
