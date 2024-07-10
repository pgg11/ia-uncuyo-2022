# Planteo de la posible solución

### Definición del entorno

* Tablero: El tablero puede ser de 5x5 o 9x9. El primero será de utilidad para tener un espacio de estados reducido que facilitará la exploración completa del espacio de estados y acciones, lo que permitirá un entrenamiento rápido. El tablero de 9x9 es el tablero original de quoridor, por lo que brindará realismo al proyecto. Una vez que el agente ha aprendido en un tablero más pequeño, se puede transferir ese conocimiento al tablero más grande, ayudando a escalar el aprendizaje.

* Definición del estado: Para representar el estado del tablero se tomaran en cuenta 
    1. posición de ambos peones
    2. ubicación de las vallas
    3. número de vallas restantes de cada jugador

* Reglas del juego:
    1. Movimiento del peón:
        * Un peón puede moverse una unidad en horizontal o vertical.
        * Puede saltar sobre el peón del oponente si están adyacentes sin valla entre ellos.
        * Si hay una valla detrás del peón contrario, puede moverse a la izquierda o derecha.
    2. Colocación de vallas:
        * Una valla puede colocarse horizontal o verticalmente.
        * No se puede bloquear completamente el camino del oponente(tiene que haber al menos un camino posible hacia la meta).


### Definición del enfoque RL

* Elección del algoritmo: Q-learning es una buena opción para empezar debido a su simplicidad y eificacia, en particular en problemas de toma de decisiones discretos. **Falta analizar otros posibles algoritmos** 

* Definición de las acciones:

    1. Movimiento del peón: Arriba, abajo, izquierda derecha o saltar sobre el peón contrario(si es posible).
    2. Colocación de vallas: Colocar una valla horizontal o vertical en una posición específica.

* Función de recompensa:

    1. Movimientos hacia la meta - Recompensa positiva.
    2. Movimientos laterales - Recompensa neutra.
    3. Movimientos hacia atrás - Recompensa negativa.
    4. Colocar una valla - Recompensa a analizar(dependiendo la efectividad de la misma para bloquear al oponente).

### Definición del enfoque determinístico

* Movimiento hacia el objetivo: Por defecto, el peón se moverá hacia adelante (hacia la meta).

* Evasión de obstáculos: Si hay una valla en el camino, el peón se moverá lateralmente (izquierda o derecha), la elección de la dirección será aleatoria para evitar patrones predecibles.

* Colocación de vallas: Si el peón contrario está lo suficientemente lejos, intenta bloquearlo colocando vallas en forma de "U", de no ser posible, prioriza el movimiento hacia la meta. Es necesario adaptar las decisiones en función de la proximidad del peón contrario y la cantidad de vallas restantes.

### Proceso de Q-learning en Quoridor

* Inicialización: Se crea una tabla Q con valores iniciales para todas las combinaciones posibles de estados y acciones.

* Interacción con el Entorno:

    1. Se comienza desde un estado inicial (configuración inicial del tablero).
    2. Se elige una acción basada en una política ϵ-greedy.
    3. Se ejecuta la acción en el entorno y se observa la recompensa y el nuevo estado.

* Actualización de la Tabla Q: Se utilizará la fórmula de actualización de Q-learning para ajustar los valores Q basados en la recompensa recibida y el nuevo estado observado.

* Repetición: Repetir el proceso hasta que el agente aprenda a jugar de manera óptima.