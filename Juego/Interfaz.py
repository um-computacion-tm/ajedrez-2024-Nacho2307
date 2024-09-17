from colorama import Fore, Style
from Juego.Chess import Chess
from Juego.Exception import ChessException
import time

class ChessInterface:
    def __init__(self):
        #Inicializa la interfaz de usuario de ajedrez y la instancia de Chess.
        self.__chess__ = Chess()  # Atributo que guarda la instancia del juego de ajedrez.

    def start(self):
        #Inicia el bucle principal del juego donde los jugadores interactúan mediante el input de consola.
        print(Fore.YELLOW + "✨ ¡Bienvenido al juego de Ajedrez, creado por Ignacio Aguilera Baigorria Jayat! ✨" + Style.RESET_ALL)
        self.display_board()

        while True:
            self.display_turn()  # Muestra el turno actual.
            option = self.get_user_option()  # Obtiene la opción del jugador.

            if option == '1':
                self.handle_move()  # Maneja el movimiento de una pieza.
            elif option == '2':
                if self.handle_draw():  # Maneja la oferta de tablas.
                    print(Fore.MAGENTA + "El juego ha terminado en tablas. ¡Buen juego!" + Style.RESET_ALL)
                    break
            elif option == '3':
                self.handle_surrender()  # Maneja la rendición.
                break
            elif option == '4':
                self.show_instructions()  # Muestra las instrucciones del juego.
            else:
                print(Fore.RED + "Opción inválida, intenta de nuevo." + Style.RESET_ALL)

    def get_user_option(self):
        #Muestra las opciones disponibles y obtiene la opción elegida por el jugador.
        #Returns:
            #str: La opción elegida por el jugador.
        return input("Opciones: \n1. Mover pieza\n2. Ofrecer tablas\n3. Rendirse\n4. Ver instrucciones\nElige una opción: ").strip()

    def display_turn(self):
        #Muestra el turno del jugador actual.
        turn = self.__chess__.get_turn()  # Obtiene el turno actual del juego.
        print(Fore.GREEN + f"\nTurno de {turn}." + Style.RESET_ALL)

    def handle_move(self):
        #Solicita las coordenadas de origen y destino del movimiento y procesa el movimiento de la pieza.
        from_pos, to_pos = self.get_move_positions()  # Obtiene las posiciones de origen y destino del jugador.
        self.process_move(from_pos, to_pos)  # Procesa el movimiento de la pieza.

    def get_move_positions(self):
        #Solicita al jugador que introduzca las coordenadas de origen y destino para el movimiento.
        #Returns:
            #tuple: Coordenadas de origen y destino.
        from_pos = input("Introduce las coordenadas de la pieza a mover (ej. 1 1 para fila 1, columna 1): ")
        to_pos = input("Introduce las coordenadas de destino (ej. 3 3 para fila 3, columna 3): ")
        return from_pos, to_pos

    def process_move(self, from_pos, to_pos):
        #Procesa el movimiento de una pieza y muestra el resultado.
        #Args:
            #from_pos (str): Coordenadas de origen.
            #to_pos (str): Coordenadas de destino.
        try:
            result = self.__chess__.move(from_pos, to_pos)  # Intenta realizar el movimiento.

            if isinstance(result, str):
                print(Fore.CYAN + result + Style.RESET_ALL)  # Si hay un mensaje de éxito, lo muestra.
            else:
                print(Fore.BLUE + "Movimiento realizado con éxito." + Style.RESET_ALL)  # Movimiento exitoso.
                self.display_board()  # Muestra el tablero después del movimiento.
        except ChessException as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)  # Maneja errores específicos del juego.
        except Exception as e:
            print(Fore.RED + f"Error inesperado: {e}" + Style.RESET_ALL)  # Maneja cualquier otro error inesperado.

    def handle_draw(self):
        current_turn = self.__chess__.get_turn()
        opponent = "BLACK" if current_turn == "WHITE" else "WHITE"  # Identificar al oponente
        print(f"{current_turn} ofrece tablas.")
        response = input(f"{opponent}, ¿aceptas las tablas? (y/n): ").strip().lower()  # Preguntar al oponente

        if response == 'y':
            print("\nJuego empatado.")
            return True  # Las tablas fueron aceptadas.
        elif response == 'n':
            print("Tablas rechazadas.")
            return False  # Las tablas fueron rechazadas.
        else:
            print("Respuesta inválida. Intenta de nuevo.")
            return self.handle_draw()  # Si la respuesta es inválida, vuelve a solicitarla.

    def handle_surrender(self):
        #Maneja la rendición de un jugador y finaliza el juego.
        message = f"{self.__chess__.get_turn()} ha decidido rendirse..."
        self.dramatic_message(message)  # Muestra un mensaje dramático de rendición.
        print(Fore.RED + "¡El otro jugador es el campeón!" + Style.RESET_ALL)

    def dramatic_message(self, message):
        #Muestra un mensaje caracter por caracter de manera dramática.
        #Args:
            # message (str): El mensaje a mostrar.
        for char in message:
            print(char, end='', flush=True)  # Muestra el mensaje carácter a carácter.
            time.sleep(0.05)  # Añade un pequeño retraso entre cada carácter.
        print()

    def display_board(self):
        #Muestra el estado actual del tablero de ajedrez.
        print(self.__chess__.get_board().mostrar_coords())  # Muestra el tablero con coordenadas.

    def show_instructions(self):
        #Muestra las instrucciones básicas del juego de ajedrez.
        print(Fore.CYAN + "\nInstrucciones del juego de Ajedrez:" + Style.RESET_ALL)
        print(Fore.YELLOW + """
1. Tablero de juego:
    - El tablero es de tamaño 8x8 con la configuración inicial estándar de piezas.

2. Piezas del juego:
    - Cada jugador tiene las siguientes piezas:
        - 1 Rey
        - 1 Reina
        - 2 Torres
        - 2 Alfiles
        - 2 Caballos
        - 8 Peones

3. Jugabilidad:
    - Los jugadores mueven las piezas según las reglas estándar del ajedrez.

4. Condiciones de finalización del juego:
    - El juego termina cuando:
        - Un jugador captura todas las piezas del oponente.
        - Ambos jugadores deciden empatar.
        - Un jugador se rinde.

5. Cómo jugar:
    - Para mover una pieza, ingresa las coordenadas de la pieza y las coordenadas de destino (ej. '1 1 a 3 3').
    - Ofrece tablas si crees que ninguno ganará.
    - Si ya no quieres continuar, puedes rendirte.
""" + Style.RESET_ALL)


if __name__ == "__main__":
    interface = ChessInterface()
    interface.start()
