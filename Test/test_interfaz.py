from unittest.mock import patch
from io import StringIO
import unittest
from Juego.Interfaz import ChessInterface

class TestChessInterface(unittest.TestCase):

    def setUp(self):
        #Inicializa una instancia de ChessInterface antes de cada prueba.
        self.interface = ChessInterface()

    def get_output_from_interface(self, inputs):
        #Ejecuta la interfaz con una lista de entradas simuladas y retorna la salida.
        with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.interface.start()
            return mock_stdout.getvalue()

    def test_invalid_move(self):
        #Prueba para simular un movimiento inválido.
        output = self.get_output_from_interface(['1', '1 1', '8 8', '3'])
        self.assertIn("Error: No se puede mover una pieza de un color diferente.", output)

    def test_movement_and_surrender(self):
        
        #Prueba para simular un movimiento básico y luego la rendición de un jugador.
        output = self.get_output_from_interface(['1', '1 2', '1 3', '3'])
        self.assertIn("Turno de WHITE.", output)
        self.assertIn("WHITE se ha rendido. ¡El otro jugador gana!", output)

    def test_offer_draw(self):
        #Prueba para simular la oferta de tablas y la aceptación.
        output = self.get_output_from_interface(['2', 'y'])
        self.assertIn("Juego empatado.", output)

if __name__ == '__main__':
    unittest.main()
