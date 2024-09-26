from colorama import Fore, Style
from Juego.Chess import Chess
from Juego.Exception import ChessException


class ChessInterface:
    def __init__(self):
        #Inicializa la interfaz de usuario de ajedrez y la instancia de Chess.
        self.__chess__ = Chess()  # Atributo que guarda la instancia del juego de ajedrez.

    def __start__(self):
        self.__start_game__()
        self.__game_loop__()

    def __start_game__(self):
        print(Fore.YELLOW + "✨ ¡Bienvenido al juego de Ajedrez! ✨" + Style.RESET_ALL)
        self.__display_board__()

    def __game_loop__(self):
        while True:
            try:
                action = input("Elija una opción:\n1. Mover pieza\n2. Ofrecer tablas\n3. Rendirse\n4. Instrucciones\n")
                if action == '3':
                    self.__handle_surrender__()
                    break
                elif action == '4':
                    self.__show_instructions__()
                elif action == '2':
                    self.__offer_draw__()
                elif action == '1':
                    self.__handle_player_action__()
                else:
                    print("Opción no válida. Por favor, intente de nuevo.")
            except Exception as e:
                print(Fore.RED + "Error inesperado: " + str(e) + Style.RESET_ALL)

    def __handle_player_action__(self):
    # Aquí manejas el proceso de mover piezas
        move = input("Introduce el movimiento (formato: fila_inicial columna_inicial fila_final columna_final): ")
        try:
            self.__process_move__(move)
            self.__display_board__()
        except ChessException as e:
            print(Fore.RED + "Error: " + str(e) + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "Error inesperado: " + str(e) + Style.RESET_ALL)

    def __handle_draw__(self):
        current_turn = self.__chess__.__get_turn__()  # Obtener el turno actual
        opponent = "BLACK" if current_turn == "WHITE" else "WHITE"  # Identificar al oponente
        print(f"{current_turn} ofrece tablas.")
        response = input(f"{opponent}, ¿aceptas las tablas? (y/n): ").strip().lower()  # Preguntar al oponente

        if response == 'y':
            print("Juego empatado.")
            return True  # Las tablas fueron aceptadas, termina el juego
        elif response == 'n':
            print("Tablas rechazadas.")
            return False  # Las tablas fueron rechazadas, el juego continúa
        else:
            print("Respuesta inválida. Intenta de nuevo.")
            return self.__handle_draw__()  # Volver a solicitar respuesta si es inválida

    # Método para mostrar las puntuaciones actuales
    def __show_scores__(self):
        print(Fore.CYAN + "\nPuntuaciones actuales:" + Style.RESET_ALL)
        self.__chess__.__show_scores__()  # Mostrar las puntuaciones usando el método en Chess

    def __get_user_option__(self):
        #Muestra las opciones disponibles y obtiene la opción elegida por el jugador.
        #Returns:
            #str: La opción elegida por el jugador.
        return input("Opciones: \n1. Mover pieza\n2. Ofrecer tablas\n3. Rendirse\n4. Ver instrucciones\n5. Guardar partida\n6. Cargar partida\n7. Mostrar puntajes\nElige una opción: ").strip()

    def __display_turn__(self):
        #Muestra el turno del jugador actual.
        turn = self.__chess__.__get_turn__()  # Obtiene el turno actual del juego.
        print(Fore.GREEN + f"\nTurno de {turn}." + Style.RESET_ALL)

    def __handle_move__(self):
        #Solicita las coordenadas de origen y destino del movimiento y procesa el movimiento de la pieza.
        from_pos, to_pos = self.__get_move_positions__()  # Obtiene las posiciones de origen y destino del jugador.
        self.__process_move__(from_pos, to_pos)  # Procesa el movimiento de la pieza.

    def __get_move_positions__(self):
        #Solicita al jugador que introduzca las coordenadas de origen y destino para el movimiento.
        #Returns:
            #tuple: Coordenadas de origen y destino.
        from_pos = input("Introduce las coordenadas de la pieza a mover (ej. 1 1 para fila 1, columna 1): ")
        to_pos = input("Introduce las coordenadas de destino (ej. 3 3 para fila 3, columna 3): ")
        return from_pos, to_pos

    def __process_move__(self, from_pos, to_pos):
        # Procesa el movimiento de una pieza y muestra el resultado.
        try:
            result = self.__chess__.__move__(from_pos, to_pos)  # Intenta realizar el movimiento.

            if isinstance(result, str):
                print(Fore.CYAN + result + Style.RESET_ALL)  # Si hay un mensaje de victoria, lo muestra.
            else:
                print(Fore.BLUE + "Movimiento realizado con éxito." + Style.RESET_ALL)  # Movimiento exitoso.
                self.__display_board__()  # Muestra el tablero después del movimiento.
                self.__show_scores__()  # Muestra las puntuaciones después del movimiento
        except ChessException as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)  # Maneja errores específicos del juego.
        except Exception as e:
            print(Fore.RED + f"Error inesperado: {e}" + Style.RESET_ALL)  # Maneja cualquier otro error inesperado.

    def __handle_surrender__(self):
        #Maneja la rendición de un jugador y finaliza el juego.
        message = f"{self.__chess__.__get_turn__()} ha decidido rendirse..."
        print(Fore.RED + "¡El otro jugador es el campeón!" + Style.RESET_ALL)

    def __display_board__(self):
        #Muestra el estado actual del tablero de ajedrez.
        print(self.__chess__.__get_board__().__mostrar_coords__())  # Muestra el tablero con coordenadas.

    def __show_instructions__(self):
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