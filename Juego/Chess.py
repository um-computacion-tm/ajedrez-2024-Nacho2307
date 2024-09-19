import copy
from Juego.board import Board
from Juego.Exception import (
    InvalidMoveException,
    OutOfBoundsException,
    PieceAlreadyCapturedException,
    ColorException,
    TurnException
)
from Juego.Piezas.Piece import Piece
from Juego.Piezas.King import King

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def get_board(self):
        return self.__board__

    def get_turn(self):
        return self.__turn__

    def print_board(self):
        print("  0 1 2 3 4 5 6 7")
        for i in range(8):
            fila = f"{i} " + " ".join(
                [str(self.__board__.get_piece(i, j)) if self.__board__.get_piece(i, j) else '.' for j in range(8)]
            )
            print(fila)

    def move(self, from_input, to_input):
        try:
            from_pos = self.parse_position(from_input)
            to_pos = self.parse_position(to_input)
            piece = self.get_piece_or_raise(from_pos)

            print(f"Turno actual: {self.__turn__}, pieza seleccionada: {piece}")  # Depuración

            # Validar turno antes de realizar el movimiento
            self.validate_turn(piece)  # Asegurarse de que la pieza coincide con el turno actual

            if self.is_in_check_after_move(self.__turn__, from_pos, to_pos):
                raise InvalidMoveException("El movimiento resulta en jaque para el rey.")

            self.execute_move(from_pos, to_pos, piece)
            status = self.check_victory()

            if status != "No result":
                return status

            self.change_turn()  # Cambiar turno después del movimiento
            print(f"Nuevo turno después de movimiento: {self.__turn__}")  # Depuración
            print(f"Legal move found for piece {piece} desde {from_pos} hasta {to_pos}")
            return True

        except (OutOfBoundsException, InvalidMoveException, PieceAlreadyCapturedException,
                ColorException, TurnException, ValueError) as e:
            print(f"Error: {str(e)}")
            raise

    def parse_position(self, input_str):
        try:
            row, col = map(int, input_str.split())
            if not (0 <= row <= 7 and 0 <= col <= 7):
                raise OutOfBoundsException(f"Position {input_str} está fuera de los límites.")
            return (row, col)

        except ValueError:
            raise ValueError(f"Entrada inválida: {input_str}. Debe tener el formato 'fila columna', donde ambos valores están entre 1 y 8.")

    def get_piece_or_raise(self, pos):
        piece = self.__board__.get_piece(*pos)
        if piece is None:
            raise PieceAlreadyCapturedException(f'En la posición {pos} no hay ninguna pieza.')
        return piece

    def validate_turn(self, piece):
        print(f"Validando turno: {self.__turn__}, color de la pieza: {piece.get_color()}")
        if piece.get_color().lower() != self.__turn__.lower():
            raise ColorException("No se puede mover una pieza de un color diferente.")

    def execute_move(self, from_pos, to_pos, piece):
        if not piece.movimiento_correcto(from_pos[0], from_pos[1], to_pos[0], to_pos[1], self.__board__):
            raise InvalidMoveException("Movimiento no válido para esta pieza.")
    
        self.__board__.set_piece(to_pos[0], to_pos[1], piece)  # Mover la pieza a la nueva posición
        self.__board__.remove_piece(from_pos[0], from_pos[1])  # Eliminar la pieza de la posición anterior

    def check_victory(self):
        pieces_alive = self.__board__.pieces_on_board()
        white_pieces, black_pieces = pieces_alive

        if white_pieces == 1 and black_pieces == 0:
            return "Black wins"
        elif black_pieces == 1 and white_pieces == 0:
            return "White wins"
        elif white_pieces == 1 and black_pieces == 1:
            return "Draw"
        return "No result"

    def has_legal_moves(self, color):
        king = self.obtener_rey(color)

        if self.esta_en_jaque(king) and not self.hay_movimientos_legales_para_salir_del_jaque(king):
            return False

        # Iterate over all pieces of the given color and check for legal moves
        for row in range(8):
            for col in range(8):
                piece = self.__board__.get_piece(row, col)
                if piece and piece.get_color().lower() == color.lower():
                    if self.has_legal_move_for_piece(piece, (row, col)):
                        return True

        return not self.esta_en_jaque(king)

    def has_legal_move_for_piece(self, piece, from_pos):
        # Itera sobre todas las posibles posiciones a las que la pieza podría moverse
        for to_row in range(8):
            for to_col in range(8):
                # Verifica si el movimiento es correcto para la pieza
                if piece.movimiento_correcto(from_pos[0], from_pos[1], to_row, to_col, self.__board__):
                    # Asegúrate de que el movimiento no ponga al rey en jaque
                    if not self.is_in_check_after_move(piece.get_color(), from_pos, (to_row, to_col)):
                        return True
        return False

    def can_piece_move(self, row, col, color):
        piece = self.__board__.get_piece(row, col)
        if not piece or piece.get_color().lower() != color.lower():
            return False
    
        return self.has_legal_move_for_piece(piece, (row, col))

    def piece_has_moves(self, piece, from_pos):
        for to_row in range(8):
            for to_col in range(8):
                if piece.movimiento_correcto(from_pos[0], from_pos[1], to_row, to_col, self.__board__):
                    # Verificar si el movimiento deja al rey en jaque
                    if not self.is_in_check_after_move(piece.get_color(), from_pos, (to_row, to_col)):
                        return True
        return False

    def is_in_check_after_move(self, color, from_pos, to_pos):
        board_copy = copy.deepcopy(self.__board__)
        piece = board_copy.get_piece(*from_pos)
    
        # Realizar movimiento en la copia del tablero
        board_copy.set_piece(*to_pos, piece)
        board_copy.remove_piece(*from_pos)

        # Verificar si el rey sigue en jaque después del movimiento
        return self.esta_en_jaque(self.obtener_rey(color))

    def obtener_rey(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.__board__.get_piece(row, col)
                if isinstance(piece, King) and piece.get_color().lower() == color.lower():
                    return piece
        return None

    def esta_en_jaque(self, rey):
        # Obtener la posición actual del rey
        rey_position = rey.get_position()
        print(f"Rey {rey} en posición {rey_position}")  # Depuración

        # Recorrer todo el tablero para encontrar piezas enemigas que puedan amenazar al rey
        for row in range(8):
            for col in range(8):
                piece = self.__board__.get_piece(row, col)

                # Verificar si la pieza es del equipo contrario
                if piece and piece.get_color() != rey.get_color():
                    print(f"Evaluando pieza {piece} en posición ({row}, {col})")  # Depuración

                # Verificar si esta pieza puede atacar al rey
                    if piece.movimiento_correcto(row, col, rey_position[0], rey_position[1], self.__board__):
                        print(f"{piece} amenaza al rey desde ({row}, {col}) hasta {rey_position}")  # Depuración
                        return True  # El rey está en jaque

        # Si no se encontraron piezas que amenacen al rey, el rey no está en jaque
        print("El rey no está en jaque.")  # Depuración
        return False

    def change_turn(self):
        if self.__turn__.lower() == "white":
            self.__turn__ = "black"
        else:
            self.__turn__ = "white"