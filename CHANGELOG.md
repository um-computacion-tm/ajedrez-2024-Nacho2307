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

## [0.0.3] - 2024-08-13

### Añadido

- Posiciones de la piezas blancas agregadas al tablero
- Se agregó la clase `Chess` para gestionar el juego de ajedrez.
- Se agregó el método `move` para mover piezas en el tablero.
- Se agregó el método `change_turn` para cambiar el turno del juego.
- Se agregó la propiedad `turn` para obtener el turno actual del juego.
- Se agregó una verificación adicional en el método `move` para asegurarse de que la pieza que se va a mover es del color del turno actual.
- Se agrego 2 mensajes de error para informar al usuario que si no hay una pieza en la posición de inicial o si no es su turno.
