from Juego.Chess import Chess
from Juego.Exception import *

class Interfaz:
    def __init__(self):
        self._chess_ = Chess()

    def mostrar_menu(self):
        # Muestra el menú principal del juego.
        print('\nChessGame - By Ignacio Aguilera Baigorria Jayat')
        print('------------------------------\n')
        print('Seleccione una opción:')
        print('1. Iniciar Juego')
        print('2. Salir\n')

    def obtener_opcion_menu(self):
        # Obtiene y valida la opción del menú ingresada por el usuario.
        seleccion = input("Escriba su selección aquí (1 o 2): ")
        while seleccion not in ["1", "2"]:
            print("Opción inválida. Por favor, seleccione 1 o 2.")
            seleccion = input("Escriba su selección aquí (1 o 2): ")
        return int(seleccion)

    def solicitar_movimiento(self):
        # Solicita al usuario las coordenadas para mover una pieza y muestra información adicional.
        while True:
            try:
                movimiento = input("Ingrese el movimiento en el siguiente formato:\n"
                                   "  fila_origen columna_origen fila_destino columna_destino\n"
                                   "Las filas y columnas deben estar entre 0 y 7 (inclusive).\n"
                                   "Ejemplo: '1 0 2 0' para mover una pieza de la fila 1, columna 0 a la fila 2, columna 0.\n"
                                   "Formato (o 'q' para salir): ")
                if movimiento.lower() == 'q':
                    return None
                from_row, from_col, to_row, to_col = map(int, movimiento.split())

                # Mostrar la pieza en la posición de origen
                piece = self._chess_.__board__.get_piece(from_row, from_col)
                if piece:
                    print(f"Pieza seleccionada: {piece} ({piece.__class__.__name__})")
                    print(f"Posición de origen: ({from_row}, {from_col})")
                    
                    # Mostrar las casillas a las que puede moverse la pieza
                    valid_moves = piece.movimiento_posible(from_row, from_col, self._chess_.__board__)
                    if valid_moves:
                        print("Casillas a las que puede moverse:")
                        for move in valid_moves:
                            print(f" - ({move[0]}, {move[1]})")
                    else:
                        print("Esta pieza no puede moverse desde la posición que esta.")
                    
                return from_row, from_col, to_row, to_col
            except ValueError:
                print("Entrada inválida. Tenes que ingresar cuatro números separados por espacios.")

    def manejar_excepcion(self, e):
        # Maneja las excepciones específicas del juego.
        if isinstance(e, (InvalidMoveException, OutOfBoundsException, PieceAlreadyCapturedException,
                          CheckException, CheckmateException, ColorException, TurnException)):
            print(f"Error: {e.message}")
        else:
            print(f"Error inesperado: {e}")

    def iniciar_juego(self):
        # Inicia el bucle principal del juego de ajedrez.
        while True:
            print(f"\nTurno del jugador: {self._chess_.turn()}")
            print(self._chess_.__board__.mostrar_coords())

            movimiento = self.solicitar_movimiento()
            if movimiento is None:
                print("Juego terminado.")
                break

            try:
                from_row, from_col, to_row, to_col = movimiento
                if self._chess_.move(from_row, from_col, to_row, to_col):
                    self._chess_.change_turn()  # Cambia el turno después del movimiento
                else:
                    print("Movimiento inválido. Intente de nuevo.")
            except (InvalidMoveException, OutOfBoundsException, PieceAlreadyCapturedException,
                    CheckException, CheckmateException, ColorException, TurnException) as e:
                self.manejar_excepcion(e)
            except Exception as e:
                print(f"Error inesperado: {e}")

    def main(self):
        # Punto de entrada principal de la aplicación.
        while True:
            self.mostrar_menu()
            opcion = self.obtener_opcion_menu()

            if opcion == 1:
                self.iniciar_juego()
            elif opcion == 2:
                print("Gracias por jugar. ¡Crack!")
                break

if __name__ == "__main__":
    interfaz = Interfaz()
    interfaz.main()

