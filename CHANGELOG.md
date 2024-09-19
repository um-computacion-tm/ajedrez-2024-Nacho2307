# Changelog

Todos los cambios notables de este proyecto se documentarán en este archivo.

El formato se basa en [Mantener un registro de cambios](https://keepachangelog.com/en/1.1.0/) y este proyecto se adhiere al [Versionado Semántico](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2024-08-11

### Añadido
- Integración con `CircleCI` para la integración continua.
- Integración con `CodeClimate` para el análisis de calidad del código.
- Archivo `README.md` con información básica del proyecto.
- Archivo `CHANGELOG.md` para registrar los cambios importantes.
- Archivo `codeclimate.yml` para la configuración de `CodeClimate`.
- Archivo `requirements.txt` con las dependencias del proyecto.
- Archivo `.gitignore` para excluir archivos innecesarios del control de versiones.
- Archivo `.circleci/config.yml` para configurar el pipeline de `CircleCI`.
- Archivo `main.py` con la función `multiply` que toma dos argumentos y devuelve su producto.
- Archivo `test.py` con pruebas unitarias para la función `multiply` importada desde `main.py`, para asegurar que devuelve el resultado esperado.

## [0.0.2] - 2024-08-13

### Añadido
- Clase `Board` para representar el tablero del ajedrez
- Clase `Piece` para representar una pieza de ajedrez.
- Clases `Rook`, `Knight`, `Bishop`, `Pawn`, `Queen` y `King` para representar las diferentes piezas de ajedrez.
- Método `get_piece` en la clase 'Board' para obtener una pieza en una posición específica del tablero.

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

-Se agrego el metodo `__str__` para una representacion en texto del tablero, en el archivo `board.py`.
-Se creo la clase 'Rook' que hereda de `Piece`.
-Se implemento el `__init__` que inicializa la torre con su color, nombre y simbolo.
-Se implemento el metodo 'movimiento_correcto' que determina si un movimiento de la torre es valido.
-Se creo la clase `Piece` para representar una pieza cualquiera en el ajedrez.
-Se implemento el metodo `__str__` que devuelve el simbolo de la pieza como texto.

#### Cambios Generales
- Refactorización del código para mejorar la legibilidad y eliminar duplicaciones.

#### Cambios en Funciones Existentes
-Se refactorizó para delegar la lógica de movimiento a la nueva función `_move_piece`.
- Mejor manejo de errores en caso de que el movimiento no sea válido.

#### Eliminaciones
- Se eliminó la lógica de movimiento y cambio de turno que estaba duplicada en otros archivos, como `cli.py`, centralizándola en la clase `Chess`.

## Cambios 
-Correcion de la funcion `__str__` en `board.py`, ahora muestra el tablero en texto.

## [0.0.5] - 2024-08-16

### Añadido

- Se agrego la carpeta `Test` para verificar el testeo de las piezas.
- Se agrego el `test_rook.py` para verificar el movimiento correcto de la pieza `Rook`.

## Refactorización de pruebas de Rook

- Se creó un método de ayuda `test_rook_movement` para reducir la duplicación de código en las pruebas de movimiento del Rook.
- Se refactorizaron las pruebas `test_movimiento_valido_horizontal`, `test_movimiento_valido_vertical`, `test_movimiento_incorrecto_diagonal` y `test_movimiento_incorrecto_no_recto` para utilizar el método helper.

## [0.0.6] - 2024-08-17

### Añadido

- Se agrego el archivo `Bishop.py` para el movimiento diagonal de la pieza.
- Se agrego el archivo `test_bishop.py` para el testeo de la pieza.

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

- Archivo llamado `Knight.py` donde esta el movimiento del caballo.
- Archivo llamado `test_knight.py` para la clase `Knight`.

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

## [0.1.11] - 2024-08-23

### Añadido

- Implementación del método `mostrar_coords` para mostrar el tablero de ajedrez con coordenadas de filas y columnas.
- El tablero ahora muestra números del `0` al `7` en la parte superior e izquierda, facilitando a los jugadores la referencia de posiciones.
- Se agrego el `test_exception.py` para la clase `Exception`.
- `test_invalid_move_exception`: prueba que se lanza una `InvalidMoveException` cuando se intenta realizar un movimiento inválido.
- `test_out_of_bounds_exception`: prueba que se lanza una `OutOfBoundsException` cuando se intenta realizar un movimiento fuera del tablero.
- `test_piece_already_captured_exception`: prueba que se lanza una `PieceAlreadyCapturedException` cuando se intenta capturar una pieza que ya ha sido capturada.
- `test_check_exception`: prueba que se lanza una `CheckException` cuando el rey está en jaque.
- `test_checkmate_exception`: prueba que se lanza una `CheckmateException` cuando se produce un jaque mate.
- `test_color_exception`: prueba que se lanza una `ColorException` cuando se intenta utilizar un color incorrecto.
- `test_turn_exception`: prueba que se lanza una `TurnException` cuando no es el turno del jugador.

## [0.1.12] - 2024-08-27

### Añadido
 
- Se agrego el archivo `Test_exception.py` para la clase `Exception`.
- Se modificaron los archivos `Pawn.py` y `Rook.py` para la duplicacion de codigo.

## [0.1.13] - 2024-08-28

### Cambio

- Se cambio el archivo `Pawn.py` por la duplicacion de codigo
- Se cambio el archivo `Rook.py` por la duplicacion de codigo.

## [0.1.14] - 2024-08-29

### Añadido

- `Nuevo Método parse_position(input_str)`: Convierte la entrada del usuario en coordenadas numéricas.
- `Nuevo Método get_piece_or_raise(pos)`: Obtiene la pieza en la posición indicada o lanza una excepción si no existe.
- `Nuevo Método validate_turn(piece)`: Valida si el turno es correcto en función del color de la pieza.
- `Nuevo Método execute_move(from_pos, to_pos, piece)`: Realiza el movimiento de una pieza, validando el movimiento y actualizando el tablero.


## [0.1.15] - 2024-08-30

### Añadido

- Se añadieron pruebas para la clase `Queen`:
  - `test_movimiento_correcto`: Verifica los movimientos válidos de la reina, incluyendo movimientos en línea recta (como torre) y en diagonal (como alfil). Asegura que la reina se mueve correctamente en línea recta y verifica que el movimiento en diagonal no sea válido para una reina.
  - `test_movimiento_incorrecto`: Comprueba movimientos inválidos de la reina para asegurar que los movimientos ilegales no sean aceptados.

## [0.1.16] - 2024-08-31

### Añadido

- Se añadieron pruebas para la clase `Pawn`:
  - `test_valid_moves`: Verifica los movimientos válidos de un peón blanco, incluyendo movimiento simple, movimiento doble inicial y captura diagonal.
  - `test_invalid_moves`: Comprueba movimientos inválidos de un peón blanco, como movimientos triples y diagonales incorrectos sin captura.
  - `test_double_initial_move_with_obstruction`: Asegura que un peón blanco no pueda realizar un movimiento doble inicial si hay una pieza que obstruye el camino.
  - `test_diagonal_capture`: Valida las capturas diagonales del peón blanco, comprobando si captura piezas de color contrario y no captura piezas del mismo color.

## [0.1.17] - 2024-09-01

### Añadido

- Se añadieron pruebas para la clase `Board`:
  - `test_initial_setup`: Verifica que el tablero se inicializa correctamente con las piezas en las posiciones correctas.
  - `test_clear_board`: Asegura que el tablero se limpia correctamente.
  - `test_place_piece`: Comprueba la colocación de piezas en el tablero.
  - `test_remove_piece`: Verifica la eliminación de piezas del tablero.
  - `test_show_coords`: Valida la representación del tablero con coordenadas.
  - `test_get_piece`: Prueba la obtención de una pieza específica en una posición dada.
  - `test_check_bounds`: Verifica que la función de límites maneje correctamente las posiciones válidas e inválidas.

## [0.1.18] - 2024-09-02

### Añadido

- Se añadieron pruebas para la clase `Chess`:
  - `test_get_piece_or_raise_with_piece`: Verifica la obtención de una pieza.
  - `test_get_piece_or_raise_without_piece`: Asegura que se lance una excepción cuando la pieza no esté presente.
  - `test_check_victory_no_result`: Verifica si el estado de victoria retorna "No result".
  - `test_esta_en_jaque`: Valida el estado de jaque del rey.
  - `test_has_legal_moves`: Confirma si existen movimientos legales para el lado blanco.
  - `test_is_in_check_after_move`: Prueba si el estado de jaque cambia después de un movimiento.
  - `test_obtener_rey`: Obtiene y verifica la pieza del rey para el lado blanco.

## [0.1.19] - 2024-09-04

### Añadido

- Se añadió la prueba `test_get_pieces` en el 'test_board.py' para cubrir el método `get_pieces` en la clase `Board`.
- Esta prueba asegura que todas las piezas en el tablero sean devueltas correctamente por el método `get_pieces`.
- Verifica que se obtengan las piezas correctas con sus respectivos colores y que la longitud de la lista de piezas sea la esperada.

## [0.1.20] - 2024-09-05

### Añadido

- Nuevos test para la clase King, asegurando una cobertura completa del código:
- **test_incio**: Verificación del color y símbolo del Rey al inicializarse.
- **test_mover_valido**: Prueba de un movimiento válido del Rey dentro de su rango permitido.
- **test_mover_invalido**: Prueba de un movimiento inválido fuera del rango permitido, asegurando que se - levante la excepción InvalidMoveException.
- **test_mismo_lugar**: Verificación de que el Rey puede permanecer en su posición actual sin error.
- **test_movimiento_correcto**: Pruebas para verificar movimientos correctos e incorrectos del Rey usando un MockBoard que simula un tablero.

- Pruebas adicionales para cubrir completamente la clase Piece, asegurando que todos los métodos sean probados:
- **Método dentro_de_limites**: Se añadieron pruebas que verifican diferentes combinaciones de coordenadas, tanto dentro como fuera del rango permitido (0 a 7).
- **Método check_move**: Se añadieron pruebas para movimientos válidos e inválidos, cubriendo los casos cuando los movimientos están fuera de los límites del tablero.
- **Método get_coordinates**: Prueba que verifica la correcta obtención de las coordenadas actuales y las nuevas de la pieza.
- **Métodomovimiento_correcto**:Piecea
- **Métodopossible_moves**:NotImplementedErrorse lanPiece.
- **Método movimiento_posible y movimiento_correcto no implementados**: Pruebas para asegurar que se lance NotImplementedError al invocar estos métodos desde la clase base Piece

## [0.2.21] - 2024-09-06

### Añadido

- **Verificación de Movimiento**: Implementada simulación de movimiento usando `copy.deepcopy` para evitar manipulaciones manuales del tablero.
- **Condiciones de Victoria**: Ajustadas las condiciones en `check_victory` para detectar correctamente la victoria y el empate.
- **Optimización de Movimientos Legales**: Mejorada la eficiencia en la comprobación de movimientos legales en `has_legal_moves` y `can_piece_move`.
- **Entrada de Posición**: Mejorado el manejo de errores y los mensajes en `parse_position` para entradas inválidas.
- **Documentación y Estilo**: Añadidos comentarios descriptivos y mejoras en la consistencia del estilo de codificación.

### Correcciones

- **Simulación de Movimiento**: Usado `copy.deepcopy` para simular y deshacer movimientos de manera más confiable.

## [0.2.22] - 2024-09-07

### Cambios en la interfaz

- **Nombre de la clase**:
  - La clase `Interfaz` ha sido renombrada a `ChessInterface`.

- **Estructura y lógica**:
  - **Método `start`**:
    - Ahora gestiona el flujo del juego principal.
    - Muestra el turno actual y maneja las opciones del usuario (mover pieza, ofrecer tablas, rendirse).
  
  - **Métodos adicionales**:
    - Se han añadido los métodos `display_turn` y `get_user_option` para mejorar la claridad y modularidad del código.
    - `get_user_option` obtiene la opción del usuario y `display_turn` muestra el turno actual del jugador.
  
  - **Método `handle_move`**:
    - Se ha dividido en `get_move_positions` para obtener las posiciones de movimiento y `process_move` para procesar el movimiento.
    - Mejora la modularidad al separar la obtención y el procesamiento de los movimientos.
  
  - **Método `handle_draw`**:
    - No ha cambiado en funcionalidad, pero ahora tiene una estructura más clara y modular.
  
  - **Método `display_board`**:
    - Muestra el estado actual del tablero.
  
- **Errores y Excepciones**:
  - Se ha simplificado el manejo de excepciones en el método `process_move`, centralizando la lógica de errores en un solo lugar.

- **Entrada/Salida**:
  - **Uso de `input` y `print`**:
    - Las entradas del usuario se manejan con `input`, y las salidas con `print`, siguiendo una estructura más limpia y modular.

### Eliminaciones

- **Métodos eliminados**:
  - `mostrar_menu`, `obtener_opcion_menu`, `solicitar_movimiento`, `manejar_excepcion`, `iniciar_juego`, y `main` han sido eliminados en favor de una interfaz más simple y directa.

- **Atributos eliminados**:
  - `self._chess_` ha sido reemplazado por `self.chess`.

### Mejoras

- **Modularidad**:
  - La nueva interfaz es más modular y legible, con funciones separadas para cada responsabilidad específica.
  
- **Manejo de errores**:
  - Se ha mejorado el manejo de errores y se ha centralizado la lógica en el método `process_move`.

- **Claridad**:
  - El flujo del programa es más claro, con funciones específicas para cada tarea, facilitando la comprensión y el mantenimiento del código.

### Cambios en el test de la interfaz

- **Renombramiento de la clase de prueba**:
  - La clase `TestInterfaz` ha sido renombrada a `TestChessInterface` para reflejar el nuevo nombre de la clase de la interfaz (`ChessInterface`).

- **Modularización de pruebas**:
  - Se ha añadido el método `setUp` para inicializar una instancia de `ChessInterface` antes de cada prueba, mejorando la organización y la reutilización del código de prueba.

- **Método auxiliar `get_output_from_interface`**:
  - Se ha introducido el método `get_output_from_interface` para simplificar la simulación de entradas y la captura de salidas, reemplazando la lógica personalizada utilizada anteriormente.

- **Pruebas actualizadas**:
  - **`test_invalid_move`**:
    - Se ha simplificado para usar `get_output_from_interface` en lugar de lógica de simulación de entrada/salida personalizada.
    - Verifica si el mensaje de error para movimiento inválido está presente en la salida.

  - **`test_movement_and_surrender`**:
    - Se ha actualizado para usar `get_output_from_interface`.
    - Verifica la salida después de simular un movimiento básico y la rendición del jugador.

  - **`test_offer_draw`**:
    - Se ha actualizado para usar `get_output_from_interface`.
    - Verifica si el mensaje de aceptación de tablas está presente en la salida.

### Eliminaciones y mejoras

- **Eliminación de código redundante**:
  - Se ha eliminado el método `_simulate_input_output`, que estaba duplicado con `get_output_from_interface`.

- **Mejora en la claridad y mantenimiento**:
  - La nueva estructura permite una mejor claridad y mantenimiento al utilizar métodos auxiliares para las simulaciones de entrada/salida.

## [0.2.23] - 2024-09-11

### Cambios en el test de la interfaz

-**Nueva prueba test_reject_draw**: Agregada para cubrir el caso donde un jugador rechaza una oferta de tablas.
-**Nueva prueba test_invalid_option**: Simula la entrada de una opción inválida en el menú y asegura que el sistema maneje el error correctamente.
-**Nueva prueba test_process_move_exception**: Verifica que se maneje correctamente una excepción de tipo ChessException durante el movimiento de una pieza.
-**Nueva prueba test_process_move_unexpected_exception**: Añadida para simular y cubrir una excepción inesperada durante el movimiento de una pieza.
-**Nueva prueba test_process_move_victory**: Verifica que cuando un movimiento devuelve un resultado de victoria (por ejemplo, "Black wins"), se imprime el resultado correcto.
-**Nueva prueba test_invalid_draw_response**: Cubre el caso donde un jugador da una respuesta inválida a una oferta de tablas, seguido por la aceptación de la misma.
-**Nueva prueba test_display_board_after_successful_move**: Asegura que el tablero se imprime después de un movimiento exitoso, cubriendo la línea self.display_board().
-Cobertura de casos adicionales para manejar excepciones durante el movimiento y respuestas inválidas del jugador.
-Cobertura de todas las líneas de la clase ChessInterface, incluyendo las verificaciones del tablero después de movimientos exitosos y condiciones de victoria.

## [0.2.24] - 2024-09-12

### Agregado

- **Color y estilo con Colorama**: Se ha añadido la librería `colorama` para mejorar la experiencia visual en la consola. Los mensajes ahora tienen colores específicos:
  - Mensaje de bienvenida con texto amarillo brillante.
  - Turnos de los jugadores mostrados en verde.
  - Mensajes de errores en rojo.
  - Mensajes de éxito en azul o cian.

- **Nueva opción de instrucciones**: Se ha agregado una nueva opción al menú principal para ver las instrucciones del juego (`opción 4`). Esto proporciona a los jugadores una descripción de las reglas básicas y cómo interactuar con el juego.

- **Animación dramática de mensajes**: Se ha implementado una animación al mostrar mensajes importantes, como la rendición de un jugador. Los caracteres se muestran uno a uno con un retraso temporal para mejorar la experiencia del usuario.

### Cambio

- **Gestión de tablas**: La opción de tablas (`opción 2`) ahora muestra mensajes en color magenta cuando el juego termina en tablas.

- **Manejo de rendición**: La rendición de un jugador (`opción 3`) ahora incluye un mensaje animado con colores para mostrar que el otro jugador ha ganado.

- **Interfaz de consola mejorada**: 
  - Los mensajes de bienvenida y las interacciones han sido mejorados visualmente.
  - La función `display_turn()` ahora muestra el turno del jugador con estilo y color.

### Agregado en `test_interfaz.py`
- **Test para mostrar instrucciones**: Se ha agregado el test `test_show_instructions` que simula la selección de la opción `4` en el menú, mostrando las instrucciones del juego y finalizando con la opción `3` (rendición).

- **Test de excepción inesperada**: En `test_process_move_unexpected_exception`, se simula una excepción inesperada durante el movimiento, verificando que se maneja correctamente.

- **Test para victoria**: Se añadió `test_process_move_victory`, que simula un movimiento exitoso que da como resultado una victoria y verifica que el mensaje de victoria ("Black wins") se imprime.

### Cambio `Test_interfaz.py`
- **Test de rendición mejorado**: El test `test_movement_and_surrender` ha sido modificado para reflejar el nuevo mensaje de rendición ("WHITE ha decidido rendirse..." y "¡El otro jugador es el campeón!") utilizando `colorama` para el formato de texto.

- **Test de oferta de tablas**: El test `test_offer_draw` ha sido mejorado para incluir la verificación de un mensaje con formato que indica que el juego ha terminado en empate con estilo y color en la consola.

- **Uso de `colorama` en tests**: Todos los tests que verifican mensajes impresos han sido actualizados para manejar el formato de texto y colores proporcionado por `colorama`.

- **Opción inválida mejorada**: El test `test_invalid_option` ahora incluye mensajes estilizados en rojo para manejar mejor la selección de opciones inválidas por el usuario.

- **Manejo de excepciones de movimiento**: Los tests `test_process_move_exception` y `test_process_move_unexpected_exception` ahora cubren tanto errores específicos del juego como errores inesperados, asegurando una cobertura completa en el manejo de excepciones.

- **Test de tablero después del movimiento**: En `test_display_board_after_successful_move`, se verificó que el tablero se imprime correctamente después de un movimiento exitoso, incluyendo el formato visual con coordenadas.

## [0.2.25] - 2024-09-16
## [0.2.26] - 2024-09-17 
## [0.2.27] - 2024-09-18 (refactorizacion chess duplicacion)
## [0.2.28] - 2024-09-19 ( refactorizacion test interfaz)

*Refactorización de tests repetitivos*:

- Se refactorizó la lógica común entre `test_process_move_exception` y `test_process_move_unexpected_exception`.
- Creación de un método auxiliar `simulate_move_exception` para manejar la simulación de excepciones durante los movimientos.
***Cambios en los tests***:

- `test_process_move_exception`:
- Ahora utiliza el nuevo método `simulate_move_exception` para simular excepciones relacionadas con los movimientos de ajedrez.
- `test_process_move_unexpected_exception`:
Reutiliza el método `simulate_move_exception` para manejar excepciones inesperadas de manera más clara.
