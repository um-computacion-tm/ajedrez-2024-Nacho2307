from Chess import Chess
from Juego.Exception import *

class Interfaz:
    def __init__(self):
        self.__chess__ = Chess()  
        
    def main(self):  
        while True:
            self.__Play__(self.__chess__)  

    def Play(self, chess):  
        try: 
            # Mostrar el tablero y el turno actual
            print(chess.board)  
            print(f"Turno: {chess.turn}")
           
            from_row = int(input("From row: "))
            from_col = int(input("From col: "))
            to_row = int(input("To row: "))
            to_col = int(input("To col: "))
        except Exception as e:
            print("Error")
            return

        try:
            chess.move(from_row, from_col, to_row, to_col)  
        except Exception as e:
            print(f"Error al intentar mover la pieza: {e}")
            return

        chess.change_turn()

if __name__ == '__main__':
    interfaz = Interfaz()  
    interfaz.main()  
