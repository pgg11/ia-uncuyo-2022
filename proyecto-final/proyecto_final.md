## Introducción
El juego Quoridor se presenta como un desafío estratégico de gran interés en el campo de los juegos de tablero, combinando la planificación a largo plazo con la adaptación a las acciones del oponente. Este proyecto tiene como objetivo desarrollar un agente inteligente capaz de competir de manera eficaz en este entorno, empleando técnicas de aprendizaje por refuerzo.

El aprendizaje por refuerzo ha demostrado ser una herramienta poderosa para diseñar sistemas autónomos que interactúan con entornos complejos, aprendiendo estrategias óptimas mediante prueba y error. Su implementación en Quoridor permite explorar cómo un agente puede aprender a navegar un espacio de estados dinámico, utilizando representaciones eficientes del tablero, estrategias de movimiento y colocación de barreras.

Dado que el diseño y entrenamiento de agentes inteligentes en juegos como Quoridor plantean desafíos significativos, este proyecto se centra en investigar el desempeño del algoritmo Q-learning, un enfoque clásico de aprendizaje por refuerzo. El agente será evaluado en tableros de diferentes tamaños (5x5 y 9x9), adaptando las reglas y objetivos del juego para maximizar la eficiencia del entrenamiento y analizar su impacto en la estrategia del agente.

Además, se introducen algunas modificaciones, como un sistema de puntuación y un límite de turnos, para explorar variantes del juego que ofrezcan un balance entre simplicidad y complejidad estratégica.

Este informe describe el desarrollo del proyecto en cinco secciones principales: el marco teórico, que aborda los fundamentos conceptuales del aprendizaje por refuerzo y su aplicación en Quoridor; el diseño experimental, donde se detalla la implementación del agente y las métricas de evaluación; el análisis y discusión de resultados, que interpreta los hallazgos obtenidos durante las pruebas; y las conclusiones, que sintetizan los aprendizajes y plantean posibles líneas futuras de trabajo.

## Marco Teórico

El desarrollo de agentes inteligentes para juegos estratégicos ha sido un tema central en el campo de la inteligencia artificial. Este trabajo se centra en el uso del aprendizaje por refuerzo (Reinforcement Learning, RL), una rama de aprendizaje automático en la que un agente interactúa con un entorno para maximizar una recompensa acumulada. En este contexto, el juego Quoridor se utiliza como caso de estudio, siendo un entorno ideal para investigar la toma de decisiones secuenciales, la planificación estratégica y la interacción competitiva.

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

En el juego de Quoridor, el entorno está representado por un tablero de 9x9 o 5x5 casillas. Los estados encapsulan información sobre las posiciones de los peones, las barreras colocadas y las barreras restantes de cada jugador. Las acciones disponibles incluyen mover el peón a una casilla válida (horizontal, vertical o mediante saltos) y colocar barreras en ubicaciones permitidas. El objetivo del agente es llegar a la fila opuesta o maximizar su puntaje siguiendo el esquema adaptado.

La recompensa se diseña para reflejar el progreso estratégico:

    1- Movimientos hacia la meta: Otorgan recompensas crecientes (2^𝑛^, según la fila alcanzada).

    2- Movimientos en sentido opuesto: Se penalizan con 2^𝑛^, siguiendo el mismo criterio.

    3- Colocación de barreras: Reciben una recompensa fija positiva para incentivar el uso estratégico de este recurso.

Este diseño recompensa las acciones que acercan al agente a su objetivo, penaliza movimientos regresivos y fomenta el uso eficiente de las barreras.

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