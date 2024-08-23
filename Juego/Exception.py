# "Base para los errores del ajedrez"
class ChessExeption(Exception):
    pass
    
class InvalidMoveException(ChessExeption):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# "Es para cuando una pieza se mueve fuera del tablero"        
class OutOfBoundsException(ChessExeption):
    def __init__(self, message):
     self.message= message
     super().__init__(message)

# "Es para cuando una se intenta capturar una pieza que ya capturaron"
class PieceAlreadyCapturedException(ChessExeption):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# "Para cuando el rey esta en jaque"
class CheckException(ChessExeption):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# "Para cuando el rey esta en Jaque mate"
class CheckmateException(ChessExeption):
    def ___init__(self, message): 
     self.message= message
     super().__init__(message)

# "Excepcion para cuando moves una pieza del color equivocado"
class ColorException(ChessExeption):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
        
# "Cuando intentas mover una pieza fuera de turno"
class TurnException(ChessExeption):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
        
