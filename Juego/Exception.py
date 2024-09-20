# Clase base para las excepciones del ajedrez
class ChessException(Exception):
    pass

# Clase base para excepciones con mensaje opcional
class ChessMessageException(ChessException):
    def __init__(self, message=None):
        if message is None:
            message = "Error en el juego de ajedrez."
        super().__init__(message)

# Excepción para movimientos inválidos en el juego de ajedrez
class InvalidMoveException(ChessMessageException):
    pass

# Excepción para cuando una pieza se mueve fuera del tablero
class OutOfBoundsException(ChessMessageException):
    pass

# Excepción para cuando se intenta capturar una pieza que ya ha sido capturada
class PieceAlreadyCapturedException(ChessMessageException):
    pass

# Excepción para cuando el rey está en jaque (en amenaza de ser capturado)
class CheckException(ChessMessageException):
    pass

# Excepción para cuando el rey está en jaque mate (no puede evitar la captura)
class CheckmateException(ChessMessageException):
    pass

# Excepción para cuando se intenta mover una pieza del color equivocado
class ColorException(ChessMessageException):
    pass

# Excepción para cuando se intenta mover una pieza fuera de turno
class TurnException(ChessMessageException):
    pass

# Excepción para posiciones inválidas en el tablero
class InvalidPositionException(ChessMessageException):
    def __init__(self, message="La posición es inválida. Debe estar dentro del tablero."):
        super().__init__(message)

# Excepción para movimientos inválidos para una pieza específica
class InvalidPieceMovementException(ChessMessageException):
    def __init__(self, message="Movimiento no válido para esta pieza."):
        super().__init__(message)

# Excepción para cuando se intenta capturar al rey (lo cual no está permitido)
class CantEatKingException(ChessMessageException):
    def __init__(self, message="No puedes capturar al Rey."):
        super().__init__(message)

# Excepción para cuando se intenta hacer un movimiento en el turno de otro jugador
class WrongTurnException(ChessMessageException):
    def __init__(self, message="Es el turno del otro jugador."):
        super().__init__(message)

# Excepción general para errores en el juego de ajedrez
class GeneralChessError(ChessMessageException):
    def __init__(self, message="Ha ocurrido un error en el juego de ajedrez."):
        super().__init__(message)

# Excepción para cuando una pieza no se encuentra en el tablero
class PieceNotFoundError(ChessMessageException):
    def __init__(self, message="Pieza no encontrada en el tablero."):
        super().__init__(message)
