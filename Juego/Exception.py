# "Base para los errores del ajedrez"
class ChessException(Exception):
    pass

class InvalidMoveException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# "Es para cuando una pieza se mueve fuera del tablero"
class OutOfBoundsException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# "Es para cuando se intenta capturar una pieza que ya capturaron"
class PieceAlreadyCapturedException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# "Para cuando el rey está en jaque"
class CheckException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# "Para cuando el rey está en Jaque mate"
class CheckmateException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# "Excepción para cuando mueves una pieza del color equivocado"
class ColorException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# "Cuando intentas mover una pieza fuera de turno"
class TurnException(ChessException):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
