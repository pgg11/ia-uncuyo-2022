# Notas
El objetivo de estas notas es apuntar toda la información que pueda ser útil tanto para el desarrollo del proyecto como para la elaboración del informe.

## Conceptos claves de cada libro y articulo seleccionados

### [1] Russell, S., & Norvig, P. (2010). Artificial Intelligence: A Modern Approach

#### Conceptos clave:
* Introducción al Reinforcement Learning como un enfoque central para sistemas inteligentes autónomos.
* Explicación de cómo los estados, acciones, y recompensas definen el marco del aprendizaje por refuerzo.
* Revisión de modelos de decisión y cómo estos influyen en el diseño de políticas.

#### Relevancia para el proyecto:
* Sirve como base conceptual para entender el marco general de los agentes inteligentes que pueden aplicarse en el diseño del agente de Quoridor.
* Proporciona herramientas teóricas para analizar decisiones y estrategias óptimas en un entorno competitivo como Quoridor.

### [2] Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction

#### Conceptos clave:
* Profundización en el aprendizaje basado en pruebas y errores, con énfasis en el equilibrio entre exploración y explotación.
* Desglose del Q-learning como un algoritmo clave de aprendizaje por refuerzo.
* Discusión sobre el diseño de la función de recompensa y su impacto en el aprendizaje del agente.
* Explicación de cómo se modelan las políticas y su relación con los valores de estado y acción.

#### Relevancia para el proyecto:
* Sirve como una guía detallada para implementar Q-learning en el agente para Quoridor.
* Ayuda a estructurar las recompensas y políticas necesarias para entrenar un agente capaz de tomar decisiones estratégicas en el juego.
* Permite entender cómo manejar las transiciones entre estados de un tablero dinámico como el de Quoridor.

### [3] Lapan, M. (2018). Deep Reinforcement Learning Hands-On

#### Conceptos clave:

* Integración de Deep Learning con algoritmos de aprendizaje por refuerzo, como Q-learning y variantes como DQN.
* Aplicaciones prácticas del aprendizaje por refuerzo en entornos complejos.


#### Relevancia para el proyecto:
* Ofrece ejemplos aplicados que pueden inspirar estrategias avanzadas para el agente de Quoridor, como combinar redes neuronales con Q-learning para explorar estados complejos.
* Es útil si es necesario ampliar el enfoque más allá del clásico Q-learning hacia métodos más robustos para manejar múltiples reglas o modificaciones.

### [4] Massagué Respall, V., Brown, J., & Aslam, H. (2018). Monte Carlo Tree Search for Quoridor

#### Conceptos clave:
* Estudio detallado de la representación de estados y acciones en Quoridor.
* Análisis de cómo los métodos basados en Monte Carlo Tree Search (MCTS) pueden usarse para optimizar decisiones en este juego.

#### Relevancia para el proyecto:
* Proporciona una base para representar el tablero de Quoridor, las posiciones de los jugadores y las barreras como estados para el agente.
* Aunque se centra en MCTS, los conceptos de representación de estados y acciones son directamente aplicables para Q-learning.
* Permite comparar Q-learning con enfoques determinísticos como MCTS en términos de efectividad y complejidad computacional.

### [5] Wang, H., Emmerich, M., & Plaat, A. (2019). Assessing the Potential of Classical Q-learning in General Game Playing

#### Conceptos clave:
* Evaluación del desempeño de Q-learning en juegos generales, con énfasis en cómo adaptar el algoritmo a diferentes escenarios.
* Discusión sobre el impacto del diseño de la función de recompensa y la representación de las políticas en el éxito del agente.

#### Relevancia para el proyecto:
* Brinda ejemplos concretos de implementación de Q-learning en juegos, que pueden adaptarse a Quoridor.
* Discute las limitaciones del algoritmo en términos de tiempo de convergencia y la necesidad de diseñar recompensas efectivas, aspectos clave para el proyecto.
* Ayuda a entender cómo modelar estrategias para entornos como Quoridor, donde las reglas y los objetivos son específicos.

## Glosario de conceptos

### Aprendizaje por Refuerzo (Reinforcement Learning, RL)
El aprendizaje por refuerzo es un paradigma del aprendizaje automático donde un agente aprende a interactuar con un entorno tomando decisiones secuenciales para maximizar una recompensa acumulada a lo largo del tiempo. Basado en prueba y error, el agente debe equilibrar la exploración de nuevas acciones con la explotación de estrategias ya conocidas. En el contexto de Quoridor, este enfoque permite desarrollar un agente que aprenda a moverse estratégicamente en el tablero, adaptándose a la dinámica del juego y a las decisiones del oponente.

### Estado (State)
Un estado representa una configuración del entorno en un momento dado, descrita por un conjunto de características relevantes para el agente. En Quoridor, el estado se define por la posición de los peones en el tablero, la distribución de las barreras y los movimientos disponibles. Capturar esta información en un formato adecuado es esencial para que el agente pueda evaluar sus opciones y tomar decisiones informadas.

### Acción (Action)
Una acción es la decisión que el agente toma en un estado particular para interactuar con el entorno, lo que genera una transición hacia un nuevo estado. En Quoridor, las acciones incluyen mover el peón a una casilla adyacente o colocar una barrera en una posición válida. Estas decisiones impactan directamente en el progreso hacia la meta del agente y en las posibilidades del oponente, lo que las convierte en un componente crítico del aprendizaje.

### Política (Policy)
La política es la estrategia que guía al agente en la selección de acciones según el estado en el que se encuentra. Puede ser determinística, indicando una única acción por estado, o estocástica, asignando probabilidades a diferentes acciones. En Quoridor, diseñar una política óptima implica priorizar movimientos que acerquen al agente a su objetivo mientras se obstaculiza el progreso del adversario, maximizando las posibilidades de ganar.

### Función de Recompensa (Reward Function)
La función de recompensa asigna un valor numérico al agente como retroalimentación por realizar una acción en un estado específico. En Quoridor, esta función puede diseñarse para otorgar recompensas positivas por movimientos que acerquen al peón del agente a la meta, o penalizaciones por acciones que no contribuyan al progreso, como colocar barreras que dificulten su propio camino. Este diseño es crucial para guiar el aprendizaje hacia estrategias efectivas.

### Q-learning
El Q-learning es un algoritmo de aprendizaje por refuerzo que actualiza valores de calidad (Q-values) para cada combinación de estado y acción, aproximando una política óptima sin requerir un modelo explícito del entorno. En Quoridor, el Q-learning permite al agente evaluar las posibles decisiones en cada turno, identificando movimientos que maximicen las recompensas acumuladas. Su capacidad para adaptarse a las transiciones dinámicas del tablero lo hace especialmente adecuado para este juego.

### Tabla Q (Q-table)
La Q-table es una estructura de datos utilizada en Q-learning para almacenar los valores Q asociados a cada par estado-acción. En Quoridor, esta tabla es fundamental para evaluar qué acciones son más ventajosas en un estado dado. Sin embargo, dado el gran espacio de estados posibles en el tablero, podría ser necesario utilizar técnicas de aproximación para manejar la complejidad.

### Exploración vs Explotación
El dilema de exploración y explotación equilibra la necesidad de probar nuevas acciones para descubrir mejores recompensas y de aprovechar acciones previamente identificadas como beneficiosas. En Quoridor, un agente que explore demasiado podría perder oportunidades claras de progreso, mientras que uno que solo explote estrategias conocidas podría quedar atrapado en soluciones subóptimas. Un buen balance entre ambos es clave para desarrollar estrategias adaptativas y efectivas.

### Factor de Descuento (𝛾)
El factor de descuento controla cuánto valora el agente las recompensas futuras en comparación con las inmediatas.

### Función de Valor (Value Function)
La función de valor estima la recompensa acumulada esperada para un estado o un par estado-acción bajo una política específica. En el contexto de Quoridor, esta función ayuda al agente a identificar estados ventajosos y a priorizar movimientos que maximicen su progreso hacia la meta.

### Entorno (Environment)
El entorno es el sistema con el que interactúa el agente, respondiendo a sus acciones con nuevos estados y recompensas. En Quoridor, el entorno se define por el tablero, las posiciones de los jugadores, las barreras y las reglas del juego. Diseñar este entorno de manera precisa es esencial para que el agente comprenda y actúe de manera efectiva en el juego.