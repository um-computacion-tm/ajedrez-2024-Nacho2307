# Clase base para las excepciones del ajedrez
class ChessException(Exception):
    pass

# Excepción para movimientos inválidos en el juego de ajedrez
class InvalidMoveException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# Excepción para cuando una pieza se mueve fuera del tablero
class OutOfBoundsException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# Excepción para cuando se intenta capturar una pieza que ya ha sido capturada
class PieceAlreadyCapturedException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# Excepción para cuando el rey está en jaque (en amenaza de ser capturado)
class CheckException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# Excepción para cuando el rey está en jaque mate (no puede evitar la captura)
class CheckmateException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# Excepción para cuando se intenta mover una pieza del color equivocado
class ColorException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# Excepción para cuando se intenta mover una pieza fuera de turno
class TurnException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# Excepción para posiciones inválidas en el tablero
class InvalidPositionException(ChessException):
    def __init__(self, message="La posición es inválida. Debe estar dentro del tablero."):
        self.message = message
        super().__init__(self.message)

# Excepción para movimientos inválidos para una pieza específica
class InvalidPieceMovementException(ChessException):
    def __init__(self, message="Movimiento no válido para esta pieza."):
        self.message = message
        super().__init__(self.message)

# Excepción para cuando se intenta capturar al rey (lo cual no está permitido)
class CantEatKingException(ChessException):
    def __init__(self, message="No puedes capturar al Rey."):
        self.message = message
        super().__init__(self.message)

# Excepción para cuando se intenta hacer un movimiento en el turno de otro jugador
class WrongTurnException(ChessException):
    def __init__(self, message="Es el turno del otro jugador."):
        self.message = message
        super().__init__(self.message)

# Excepción general para errores en el juego de ajedrez
class GeneralChessError(ChessException):
    def __init__(self, message="Ha ocurrido un error en el juego de ajedrez."):
        self.message = message
        super().__init__(self.message)

# Excepción para cuando una pieza no se encuentra en el tablero
class PieceNotFoundError(ChessException):
    def __init__(self, message="Pieza no encontrada en el tablero."):
        self.message = message
        super().__init__(self.message)
