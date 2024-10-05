from colorama import Fore, Style
from Juego.Chess import Chess
from Juego.Exception import ChessException
import time

class ChessInterface:
    def __init__(self):
        #Inicializa la interfaz de usuario de ajedrez y la instancia de Chess.
        self.__chess__ = Chess()  # Atributo que guarda la instancia del juego de ajedrez.

    def __start__(self):
        print(Fore.YELLOW + "✨ ¡Bienvenido al juego de Ajedrez! ✨" + Style.RESET_ALL)
        self.__display_board__()
    
        game_over = False  # Variable para controlar la finalización del juego
    
        while not game_over:
            self.__display_turn__()
            option = self.__get_user_option__()
            game_over = self.__handle_option__(option)

    def __handle_option__(self, option):
        if option == '1':
            self.__handle_move__()
        elif option == '2':
            return self.__handle_draw__()  # Si se aceptan las tablas, termina el juego
        elif option == '3':
            self.__handle_surrender__()
            return True  # Termina el juego después de la rendición
        elif option == '4':
            self.__show_instructions__()  
        elif option == '5':
            self.__save_game__()
        elif option == '6':
                game_id = input("Introduce el ID de la partida que deseas cargar: ")
                try:
                    self.__chess__.__load_game__(game_id)
                    print(Fore.GREEN + "Partida cargada con éxito." + Style.RESET_ALL)
                    self.__display_board__()
                except ChessException as e:
                    print(Fore.RED + f"Error al cargar la partida: {e}" + Style.RESET_ALL)
                except Exception as e:
                    print(Fore.RED + f"Error inesperado: {e}" + Style.RESET_ALL)
        elif option == '7':  # Nueva opción para mostrar puntajes
                self.__show_scores__()
        else:
                print(Fore.RED + "Opción inválida, intenta de nuevo." + Style.RESET_ALL)

        return False  # Continúa el juego si no se ha rendido ni aceptado tablas

    def __save_game__(self):
        game_id = input("Introduce un ID para guardar la partida: ")
        self.__chess__.__save_game__(game_id)

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
        from_pos = input("Introduce las coordenadas de la pieza a mover (ej. 1 1 para fila 1, columna 1): ")
        to_pos = input("Introduce las coordenadas de destino (ej. 3 3 para fila 3, columna 3): ")
        return from_pos, to_pos

    def __process_move__(self, from_pos, to_pos):
    # Procesa el movimiento de una pieza y muestra el resultado.
        try:
            result = self.__chess__.__move__(from_pos, to_pos)  # Intenta realizar el movimiento.

            if isinstance(result, str):
                print(Fore.CYAN + result + Style.RESET_ALL)  # Si hay un mensaje de victoria, lo muestra.
                return False  # Si hay un mensaje de victoria, el movimiento no es un movimiento exitoso.
            else:
                print(Fore.BLUE + "Movimiento realizado con éxito." + Style.RESET_ALL)  # Movimiento exitoso.
                self.__display_board__()  # Muestra el tablero después del movimiento.
                self.__show_scores__()  # Muestra las puntuaciones después del movimiento.
                return True  # Indica que el movimiento fue exitoso.
        except ChessException as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)  # Maneja errores específicos del juego.
            return False  # Retorna False si hubo un error.
        except Exception as e:
            print(Fore.RED + f"Error inesperado: {e}" + Style.RESET_ALL)  # Maneja cualquier otro error inesperado.
            return False  # Retorna False si hubo un error inesperado.

    def __handle_surrender__(self):
        #Maneja la rendición de un jugador y finaliza el juego.
        message = f"{self.__chess__.__get_turn__()} ha decidido rendirse..."
        self.__dramatic_message__(message)  # Muestra un mensaje dramático de rendición.
        print(Fore.RED + "¡El otro jugador es el campeón!" + Style.RESET_ALL)

    def __dramatic_message__(self, message):
        #Muestra un mensaje caracter por caracter de manera dramática.
        for char in message:
            print(char, end='', flush=True)  # Muestra el mensaje carácter a carácter.
            time.sleep(0.05)  # Añade un pequeño retraso entre cada carácter.
        print()

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
    interface.__start__()