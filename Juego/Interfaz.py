from Juego.Chess import Chess
from Juego.Exception import ChessException

class ChessInterface:
    def __init__(self):
        self.chess = Chess()

    def start(self):
        print("Bienvenido al juego de Ajedrez.")
        self.display_board()  # Muestra el tablero solo una vez al inicio

        while True:
            self.display_turn()
            option = self.get_user_option()

            if option == '1':
                self.handle_move()
            elif option == '2':
                if self.handle_draw():
                    break
            elif option == '3':
                print(f"{self.chess.get_turn()} se ha rendido. ¡El otro jugador gana!")
                break
            else:
                print("Opción inválida, intenta de nuevo.")

    def get_user_option(self):
        return input("Opciones: \n1. Mover pieza\n2. Ofrecer tablas\n3. Rendirse\nElige una opción: ").strip()

    def display_turn(self):
        turn = self.chess.get_turn()
        print(f"\nTurno de {turn}.")

    def handle_move(self):
        from_pos, to_pos = self.get_move_positions()
        self.process_move(from_pos, to_pos)

    def get_move_positions(self):
        from_pos = input("Introduce las coordenadas de la pieza a mover (ej. 1 1 para fila 1, columna 1): ")
        to_pos = input("Introduce las coordenadas de destino (ej. 3 3 para fila 3, columna 3): ")
        return from_pos, to_pos

    def process_move(self, from_pos, to_pos):
        try:
            result = self.chess.move(from_pos, to_pos)

            if isinstance(result, str):
                print(result)
                if result != "No result":
                    return True
            else:
                print("Movimiento realizado con éxito.")
                self.display_board()  # Muestra el tablero después de un movimiento
        except ChessException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def handle_draw(self):
        print(f"{self.chess.get_turn()} ofrece tablas.")
        response = input(f"{self.chess.get_turn()}, ¿aceptas las tablas? (y/n): ").strip().lower()

        if response == 'y':
            print("\nJuego empatado.")
            return True
        elif response == 'n':
            print("Tablas rechazadas.")
            return False
        else:
            print("Respuesta inválida. Intenta de nuevo.")
            return self.handle_draw()

    def display_board(self):
        print(self.chess.get_board().mostrar_coords())  # Muestra el tablero

if __name__ == "__main__":
    interface = ChessInterface()
    interface.start()