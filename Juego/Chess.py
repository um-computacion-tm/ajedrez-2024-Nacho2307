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
        for row in self.__board__.__positions__:
            print(" | ".join([Piece.get_symbol() if Piece else " " for Piece in row]))
            print("-" * 33)

    def move(self, from_input, to_input):
        try:
            from_pos = self.parse_position(from_input)
            to_pos = self.parse_position(to_input)
            piece = self.get_piece_or_raise(from_pos)
            self.validate_turn(piece)
            
            if self.is_in_check_after_move(self.__turn__, from_pos, to_pos):
                raise InvalidMoveException("El movimiento resulta en jaque para el rey.")

            self.execute_move(from_pos, to_pos, piece)
            status = self.check_victory()

            if status != "No result":
                return status
            
            self.change_turn()
            return True

        except (OutOfBoundsException, InvalidMoveException, PieceAlreadyCapturedException,
                ColorException, TurnException, ValueError) as e:
            print(f"Error: {str(e)}")
            raise

    def parse_position(self, input_str):
        try:
            row, col = map(int, input_str.split())
            row -= 1
            col -= 1

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
        if piece.get_color().lower() != self.__turn__.lower():
            raise ColorException("No se puede mover una pieza de un color diferente.")

    def execute_move(self, from_pos, to_pos, piece):
        if not piece.movimiento_correcto(from_pos[0], from_pos[1], to_pos[0], to_pos[1], self.__board__):
            raise InvalidMoveException("Movimiento no válido para esta pieza.")
        
        self.__board__.set_piece(*to_pos, piece)
        self.__board__.set_piece(*from_pos, None)

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
        print(f"Checking legal moves for {color}")
        for row in range(8):
            for col in range(8):
                if self.can_piece_move(row, col, color):
                    print(f"Legal move found for {color} at position {(row, col)}")
                    return True
        print("No legal moves found")
        return False

    def can_piece_move(self, row, col, color):
        piece = self.__board__.get_piece(row, col)
        if piece and piece.get_color().lower() == color.lower():
            return self.piece_has_moves(piece, (row, col))
        return False
    
    def piece_has_moves(self, piece, from_pos):
        print(f"Checking piece at {from_pos}: {piece}")
        for to_row in range(8):
            for to_col in range(8):
                if piece.movimiento_correcto(from_pos[0], from_pos[1], to_row, to_col, self.__board__):
                    print(f"Legal move found for piece at {from_pos} to {(to_row, to_col)}")
                    return True
        return False

    def is_in_check_after_move(self, color, from_pos, to_pos):
        board_copy = copy.deepcopy(self.__board__)
        piece = board_copy.get_piece(*from_pos)
        board_copy.set_piece(*to_pos, piece)
        board_copy.set_piece(*from_pos, None)

        king = self.obtener_rey(color)
        return self.esta_en_jaque(king)

    def obtener_rey(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.__board__.get_piece(row, col)
                if isinstance(piece, King) and piece.get_color().lower() == color.lower():
                    return piece
        return None

    def esta_en_jaque(self, rey):
        rey_position = rey.get_position()
        for row in range(8):
            for col in range(8):
                piece = self.__board__.get_piece(row, col)
                if piece and piece.get_color() != rey.get_color():
                    if piece.movimiento_correcto(row, col, rey_position[0], rey_position[1], self.__board__):
                        return True
        return False

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
