## Introducción
El desarrollo de agentes inteligentes para juegos estratégicos ha sido un tema central en el campo de la inteligencia artificial. Este trabajo se centra en el uso del aprendizaje por refuerzo (Reinforcement Learning, RL), una rama de aprendizaje automático en la que un agente interactúa con un entorno para maximizar una recompensa acumulada.

Quoridor se presenta como un desafío estratégico de gran interés en el ámbito de los juegos de tablero, al combinar la planificación a largo plazo con la adaptación a las acciones del oponente. En este proyecto, el aprendizaje por refuerzo se utiliza para explorar cómo un agente puede aprender a navegar un espacio de estados dinámico, empleando representaciones eficientes del tablero, estrategias de movimiento y colocación de barreras.

Este trabajo se centra en el diseño, implementación y análisis de dos tipos de agentes para el juego Quoridor: un agente determinista, basado en reglas predefinidas, y un agente adaptativo, entrenado mediante Q-learning, un algoritmo de aprendizaje por refuerzo.

Para evaluar de manera efectiva al agente basado en Q-learning, se introdujeron algunas modificaciones al juego original. Entre ellas, un sistema de puntuación y un límite de turnos, que permiten medir el desempeño en escenarios más controlados y facilitan el entrenamiento del agente.

El agente adaptativo será evaluado en partidas automáticas contra un agente determinista, cuyo comportamiento está basado en un conjunto fijo de reglas, como avanzar prioritariamente hacia la meta y bloquear estratégicamente al oponente mediante la colocación de barreras. Esta comparación permitirá analizar las diferencias en desempeño entre un enfoque basado en aprendizaje por refuerzo y otro basado en reglas fijas, destacando las ventajas de un agente que aprende y se adapta dinámicamente.

Este informe describe el desarrollo del proyecto en cinco secciones principales: el marco teórico, que aborda los fundamentos conceptuales del aprendizaje por refuerzo y su aplicación en Quoridor; el diseño experimental, donde se detalla la implementación de los agentes y las métricas de evaluación; el análisis y discusión de resultados, que interpreta los hallazgos obtenidos durante las pruebas; y las conclusiones, que sintetizan los aprendizajes y plantean posibles líneas futuras de trabajo.

## Marco Teórico 

Quoridor es un juego de tablero que plantea desafíos estratégicos y tácticos. Los jugadores deben avanzar hacia su objetivo mientras colocan barreras para dificultar el progreso del oponente, garantizando siempre un camino accesible hacia la meta. Esta combinación de planificación ofensiva y defensiva convierte a Quoridor en un entorno ideal para estudiar agentes inteligentes que toman decisiones en tiempo real.

#### Aprendizaje por Refuerzo
El aprendizaje por refuerzo se basa en la interacción entre un agente y un entorno. El agente observa el estado del entorno, ejecuta una acción, recibe una recompensa y transita hacia un nuevo estado. El objetivo del agente es aprender una política que maximice la recompensa acumulada a lo largo del tiempo. La política puede ser una función determinista o probabilística que asocia estados con acciones.

Un concepto central en RL es la función de valor, que estima la recompensa esperada para un estado o una combinación estado-acción. En este trabajo, se utiliza el algoritmo Q-learning, que aproxima la función de valor óptima (𝑄*) sin requerir un modelo explícito del entorno. Este algoritmo utiliza una estructura conocida como Q-table para almacenar los valores Q y actualizarlos mediante la fórmula:

    𝑄(𝑠,𝑎) ← 𝑄(𝑠,𝑎) + 𝛼 [𝑟 + 𝛾max~𝑎′~ 𝑄(𝑠′,𝑎′) − 𝑄(𝑠,𝑎)]

Donde:

* 𝑠 y 𝑠′ son el estado actual y el siguiente.

* 𝑎 y 𝑎′ son las acciones actuales y futuras.

* 𝑟 es la recompensa recibida.

* 𝛼 es la tasa de aprendizaje.

* 𝛾 es el factor de descuento.

#### Aplicación en Quoridor

En el juego de Quoridor, el entorno está representado por un tablero de 9x9 casillas. En este proyecto, se trabajan dos variantes del juego: un tablero estándar de 9x9 casillas y una versión simplificada de 5x5. El uso de un tablero más pequeño facilita la exploración y entrenamiento inicial del agente basado en Q-learning, permitiendo un análisis comparativo del impacto de la complejidad del entorno en el desempeño de los agentes.

Además, se introducen modificaciones como un sistema de puntuación basado en el progreso hacia la meta, la colocación de barreras y la cantidad de turnos disponibles. Estas reglas adaptadas permiten evaluar de forma más granular las estrategias y decisiones tomadas por los agentes.

En este contexto los estados encapsulan información sobre las posiciones de los peones, las barreras colocadas y las barreras restantes de cada jugador. Las acciones disponibles incluyen mover el peón a una casilla válida (horizontal, vertical o mediante saltos) y colocar barreras en ubicaciones permitidas. El objetivo del agente es llegar a la fila opuesta o maximizar su puntaje siguiendo el esquema adaptado.

La recompensa se diseña para reflejar el progreso estratégico:

    1- Movimientos hacia la meta: Otorgan recompensas crecientes (2^𝑛^, según la fila alcanzada).

    2- Movimientos en sentido opuesto: Se penalizan con 2^𝑛^, siguiendo el mismo criterio.

    3- Colocación de barreras: Reciben una recompensa fija positiva para incentivar el uso estratégico de este recurso.

Este diseño recompensa las acciones que acercan al agente a su objetivo, penaliza movimientos regresivos y fomenta el uso eficiente de las barreras.

#### El Agente Determinista

En contraste con el agente basado en Q-learning, el agente determinista sigue un conjunto de reglas predefinidas para tomar decisiones. Estas reglas incluyen avanzar hacia la meta siempre que sea posible, bloquear estratégicamente al oponente mediante la colocación de barreras en forma de "U", y realizar movimientos laterales o retrocesos cuando las opciones anteriores no estén disponibles. Este enfoque ofrece un comportamiento predecible y sirve como referencia para evaluar el desempeño del agente adaptativo.

#### Comparación de Enfoques

El enfrentamiento entre el agente determinista y el agente basado en Q-learning proporciona una base para analizar la eficacia de los enfoques basados en reglas frente a los adaptativos. Mientras que el agente determinista sigue estrategias fijas, el agente de Q-learning tiene la capacidad de ajustar su comportamiento a medida que aprende del entorno, lo que puede resultar en un desempeño superior en situaciones complejas o dinámicas.

#### Comparación con Otros Métodos

Aunque este trabajo emplea Q-learning, otros enfoques, como el **Monte Carlo Tree Search (MCTS)**, han sido explorados previamente en Quoridor debido a su capacidad para evaluar de forma eficiente múltiples secuencias de movimientos. Sin embargo, el MCTS es computacionalmente intensivo y requiere un modelo explícito del juego, lo que lo hace menos adecuado para entrenar agentes adaptativos en un entorno dinámico. En contraste, Q-learning permite a los agentes aprender directamente de la interacción con el entorno, adaptándose al comportamiento del oponente y a reglas modificadas.

#### Relevancia del Aprendizaje por Refuerzo en Quoridor

La naturaleza secuencial y competitiva de Quoridor lo convierte en un entorno ideal para investigar el balance entre exploración y explotación, el diseño de recompensas, y la representación eficiente de estados y acciones. Además, las adaptaciones introducidas en este proyecto, como el sistema de puntuación y los tableros de diferentes tamaños, permiten evaluar cómo la complejidad del entorno afecta el aprendizaje y la estrategia del agente.

## Bibliografía

[1] Russell, S., & Norvig, P. (2010). Artificial Intelligence: A Modern Approach (3rd ed.). Pearson.

[2] Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction (2nd ed.). MIT Press.

[3] Lapan, M. (2018). Deep Reinforcement Learning Hands-On. Packt Publishing.

[4] Massagué Respall, V., Brown, J., & Aslam, H. (2018). Monte Carlo Tree Search for Quoridor. ResearchGate.

[5] Wang, H., Emmerich, M., & Plaat, A. (2019). Assessing the Potential of Classical Q-learning in General Game Playing. In Proceedings of the International Conference on Agents and Artificial Intelligence. ResearchGate.