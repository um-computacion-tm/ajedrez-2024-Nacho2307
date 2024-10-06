## JUEGO DE AJEDREZ
Proyecto creado por [Ignacio Aguilera Baigorria Jayat]

## Cómo Instalar el Juego

- El juego se ejecuta utilizando Docker. Sigue los siguientes pasos para instalar y correr el juego:

1. **Instalar Docker**  
    - Si no tienes Docker instalado, ejecuta el siguiente comando:
   ```bash
   $ sudo apt install docker

2. **Crear la imagen en Docker del juego**
    - Para crear la imagen ejecuta:
    ```bash
    $ sudo docker build -t ajedrez-2024-nacho2307 . --no-cache

3. **Ejecutar los tests e iniciar el juego**
   - Una vez creada la imagen, puedes ejecutar el siguiente comando para correr los tests e iniciar el juego:
         ```bash
         $ sudo docker run -i ajedrez-2024-nacho2307

## Reglas del Juego
- El juego sigue las reglas básicas del ajedrez con algunas modificaciones:

-- `Reglas originales del ajedrez`: Consultarlas [aquí](https://es.wikipedia.org/wiki/Leyes_del_ajedrez)

-- `Reglas de este juego`: En este ajedrez se respetan los movimientos de las piezas como en el ajedrez tradicional. Sin embargo, no se implementan reglas como jaque, jaque mate, ni movimientos especiales.

## Configuración Inicial del Tablero
- Las piezas blancas se colocan en las filas 6 y 7, mientras que las piezas negras se colocan en las filas 0 y 1:
  - **Piezas Blancas**:
    - Fila 6: Peones
    - Fila 7: Torres, Caballos, Alfiles, Rey, Reina
  - **Piezas Negras**:
    - Fila 0: Torres, Caballos, Alfiles, Rey, Reina
    - Fila 1: Peones

## Cómo Jugar
- El juego se basa en alternar turnos, donde cada jugador mueve una pieza según las reglas del ajedrez tradicional. Aquí te describo la interfaz del juego:

   - La interfaz ofrece un menú con las opciones de `Mover pieza`, `Ofrecer tablas`, `Rendirse`, `Ver instrucciones`, `Guardar partida`, `Cargar partida`, y `Mostrar puntajes`.

***Mover pieza***: Permite mover una pieza. Se solicita la posición actual de la pieza y la posición a la que se desea mover, ambas utilizando coordenadas (Ej: 1 0, 2 0).

- Si el movimiento es válido, se efectúa; si no, se cancela y vuelve a pedirle al jugador que haga el movimiento. Después, se verifica si un jugador ha ganado.
***Ofrecer tablas***: Permite ofrecer tablas (empate). Si el oponente acepta, el juego termina en empate. Si no, el jugador que ofreció las tablas vuelve a su turno.

***Rendirse***: Permite rendirse, lo que otorga la victoria al oponente.

***Guardar partida***: Permite guardar la partida actual usando un ID específico.

***Cargar partida***: Permite cargar una partida guardada introduciendo su ID.

***Mostrar puntajes***: Muestra las puntuaciones actuales de ambos jugadores.

`Guardado de Partidas`: El juego utiliza Redis para permitir a los jugadores guardar sus partidas y reanudar más tarde desde el mismo punto.

### Cómo Ganar
- Para ganar, tu oponente debe quedar solo con el Rey, mientras que tú debes tener el Rey y al menos una pieza adicional. El primero que se quede sin piezas (exceptuando al Rey) pierde. Además, el juego puede terminar en empate si ambos jugadores acuerdan tablas o un jugador decide rendirse.

## Integraciones 

# CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-Nacho2307/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-Nacho2307/tree/main)

# Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/29c65f3e532e1f2648c6/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Nacho2307/maintainability)

# Test Coverage Badge
[![Test Coverage](https://api.codeclimate.com/v1/badges/29c65f3e532e1f2648c6/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Nacho2307/test_coverage)
