# Changelog

Todos los cambios notables de este proyecto se documentarán en este archivo.

El formato se basa en [Mantener un registro de cambios](https://keepachangelog.com/en/1.1.0/) y este proyecto se adhiere al [Versionado Semántico](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2024-08-11

### Añadido
- Integración con CircleCI para la integración continua.
- Integración con CodeClimate para el análisis de calidad del código.
- Archivo `README.md` con información básica del proyecto.
- Archivo `CHANGELOG.md` para registrar los cambios importantes.
- Archivo `codeclimate.yml` para la configuración de CodeClimate.
- Archivo `requirements.txt` con las dependencias del proyecto.
- Archivo `.gitignore` para excluir archivos innecesarios del control de versiones.
- Archivo `.circleci/config.yml` para configurar el pipeline de CircleCI.
- Archivo `main.py` con la función `multiply` que toma dos argumentos y devuelve su producto.
- Archivo `test.py` con pruebas unitarias para la función `multiply` importada desde `main.py`, para asegurar que devuelve el resultado esperado.

## [0.0.2] - 2024-08-13

### Añadido
- Clase 'Board' para representar el tablero del ajedrez
- Clase Piece para representar una pieza de ajedrez.
- Clases 'Rook', 'Knight', 'Bishop', 'Pawn', 'Queen' y 'King' para representar las diferentes piezas de ajedrez.
- Método 'get_piece' en la clase 'Board' para obtener una pieza en una posición específica del tablero.

## [0.0.3] - 2024-08-14

### Añadido

- Posiciones de la piezas blancas agregadas al tablero
- Se agregó la clase `Chess` para gestionar el juego de ajedrez.
- Se agregó el método `move` para mover piezas en el tablero.
- Se agregó el método `change_turn` para cambiar el turno del juego.
- Se agregó la propiedad `turn` para obtener el turno actual del juego.
- Se agregó una verificación adicional en el método `move` para asegurarse de que la pieza que se va a mover es del color del turno actual.
- Se agrego 2 mensajes de error para informar al usuario que si no hay una pieza en la posición de inicial o si no es su turno.

## [0.0.4] - 2024-08-15

### Añadido

-Se agrego el metodo '__str__' para una representacion en texto del tablero, en el archivo board.py
-Se creo la clase 'Rook' que hereda de 'Piece'.
-Se implemento el '__init__' que inicializa la torre con su color, nombre y simbolo.
-Se implemento el metodo 'movimiento_correcto' que determina si un movimiento de la torre es valido.
-Se creo la clase 'Piece' para representar una pieza cualquiera en el ajedrez.
-Se implemento el metodo '__str__' que devuelve el simbolo de la pieza como texto.

#### Cambios Generales
- Refactorización del código para mejorar la legibilidad y eliminar duplicaciones.

#### Cambios en Funciones Existentes
-Se refactorizó para delegar la lógica de movimiento a la nueva función `_move_piece`.
- Mejor manejo de errores en caso de que el movimiento no sea válido.

#### Eliminaciones
- Se eliminó la lógica de movimiento y cambio de turno que estaba duplicada en otros archivos, como `cli.py`, centralizándola en la clase `Chess`.

## Cambios 
-Correcion de la funcion '__str__' en board.py, ahora muestra el tablero en texto.

## [0.0.5] - 2024-08-16

### Añadido

- Se agrego la carpeta 'Test' para verificar el testeo de las piezas.
- Se agrego el 'test_rook.py' para verificar el movimiento correcto de la pieza 'Rook'.

## Refactorización de pruebas de Rook

- Se creó un método de ayuda `test_rook_movement` para reducir la duplicación de código en las pruebas de movimiento del Rook.
- Se refactorizaron las pruebas `test_movimiento_valido_horizontal`, `test_movimiento_valido_vertical`, `test_movimiento_incorrecto_diagonal` y `test_movimiento_incorrecto_no_recto` para utilizar el método helper.

## [0.0.6] - 2024-08-17

### Añadido

- Se agrego el archivo 'Bishop.py' para el movimiento diagonal de la pieza.
- Se agrego el archivo 'test_bishop.py' para el testeo de la pieza.

## [0.0.7] - 2024-08-19

### Añadido

-Implementación del método `mover` que actualiza la posición del rey si el movimiento es válido

# Refactorizacion del test de bishop

- Uso de `with self.subTest(...)` en el método `_test_moves` para mejorar la trazabilidad y depuración de las pruebas individuales.

## [0.0.8] - 2024-08-20

### Añadido

-Creado el archivo de pruebas `test_rey.py` para la clase `King`.

## [0.0.9] - 2024-08-21

### Añadido

- Archivo llamado "Knight.py" donde esta el movimiento del caballo.
- Archivo llamado "test_knight.py" para la clase "Knight".

## [0.0.10] - 2024-08-22

### Añadido

- Agregada `ChessException` como excepción base para todos los errores relacionados con ajedrez.
- Agregada `InvalidMoveException` para movimientos inválidos.
- Agregada `OutOfBoundsException` para movimientos que se salen del tablero.
- Agregada `PieceAlreadyCapturedException` para intentar capturar una pieza que ya ha sido capturada.
- Agregada `CheckException` para cuando el rey está en jaque
- Agregada `CheckmateException` para cuando el rey está en jaque mate.
- Agregada `ColorException` para intentar mover una pieza del color equivocado.
- Agregada `TurnException` para intentar mover una pieza fuera de turno.

## [0.0.11] - 2024-08-23

### Añadido

- Implementación del método 'mostrar_coords' para mostrar el tablero de ajedrez con coordenadas de filas y columnas.
- El tablero ahora muestra números del `0` al `7` en la parte superior e izquierda, facilitando a los jugadores la referencia de posiciones.
- Se agrego el 'test_exception.py' para la clase 'Exception'.
- test_invalid_move_exception: prueba que se lanza una InvalidMoveException cuando se intenta realizar un movimiento inválido.
- test_out_of_bounds_exception: prueba que se lanza una OutOfBoundsException cuando se intenta realizar un movimiento fuera del tablero.
- test_piece_already_captured_exception: prueba que se lanza una PieceAlreadyCapturedException cuando se intenta capturar una pieza que ya ha sido capturada.
- test_check_exception: prueba que se lanza una CheckException cuando el rey está en jaque.
- test_checkmate_exception: prueba que se lanza una CheckmateException cuando se produce un jaque mate.
- test_color_exception: prueba que se lanza una ColorException cuando se intenta utilizar un color incorrecto.
- test_turn_exception: prueba que se lanza una TurnException cuando no es el turno del jugador.

## [0.0.12] - 2024-08-27

### Añadido
 
- Se agrego el archivo 'Test_exception.py' para la clase 'Exception'.
- Se modificaron los archivos 'Pawn.py' y 'Rook.py' para la duplicacion de codigo.

## [0.0.13] - 2024-08-28

### Cambio

- Se cambio el archivo 'Pawn.py' por la duplicacion de codigo
- Se cambio el archivo 'Rookpy' por la duplicacion de codigo.

## [0.0.14] - 2024-08-29

### Añadido

- Nuevo Método parse_position(input_str): Convierte la entrada del usuario en coordenadas numéricas.
- Nuevo Método get_piece_or_raise(pos): Obtiene la pieza en la posición indicada o lanza una excepción si no existe.
- Nuevo Método validate_turn(piece): Valida si el turno es correcto en función del color de la pieza.
- Nuevo Método execute_move(from_pos, to_pos, piece): Realiza el movimiento de una pieza, validando el movimiento y actualizando el tablero.


## [0.0.15] - 2024-08-30

### Añadido

- Test queen 

## [0.0.16] - 2024-08-31

### Añadido

-test pawn


## [0.0.17] - 2024-09-01

### Añadido

- Test board

## [0.0.18] - 2024-09-02

### Añadido
