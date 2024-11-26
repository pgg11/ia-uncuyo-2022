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