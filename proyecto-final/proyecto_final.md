## Introducción
El juego Quoridor se presenta como un desafío estratégico de gran interés en el campo de los juegos de tablero, combinando la planificación a largo plazo con la adaptación a las acciones del oponente. Este proyecto tiene como objetivo desarrollar un agente inteligente capaz de competir de manera eficaz en este entorno, empleando técnicas de aprendizaje por refuerzo.

El aprendizaje por refuerzo ha demostrado ser una herramienta poderosa para diseñar sistemas autónomos que interactúan con entornos complejos, aprendiendo estrategias óptimas mediante prueba y error. Su implementación en Quoridor permite explorar cómo un agente puede aprender a navegar un espacio de estados dinámico, utilizando representaciones eficientes del tablero, estrategias de movimiento y colocación de barreras.

Dado que el diseño y entrenamiento de agentes inteligentes en juegos como Quoridor plantean desafíos significativos, este proyecto se centra en investigar el desempeño del algoritmo Q-learning, un enfoque clásico de aprendizaje por refuerzo. El agente será evaluado en tableros de diferentes tamaños (5x5 y 9x9), adaptando las reglas y objetivos del juego para maximizar la eficiencia del entrenamiento y analizar su impacto en la estrategia del agente.

Además, se introducen algunas modificaciones, como un sistema de puntuación y un límite de turnos, para explorar variantes del juego que ofrezcan un balance entre simplicidad y complejidad estratégica.

Este informe describe el desarrollo del proyecto en cinco secciones principales: el marco teórico, que aborda los fundamentos conceptuales del aprendizaje por refuerzo y su aplicación en Quoridor; el diseño experimental, donde se detalla la implementación del agente y las métricas de evaluación; el análisis y discusión de resultados, que interpreta los hallazgos obtenidos durante las pruebas; y las conclusiones, que sintetizan los aprendizajes y plantean posibles líneas futuras de trabajo.

## Bibliografía

[1] Russell, S., & Norvig, P. (2010). Artificial Intelligence: A Modern Approach (3rd ed.). Pearson.

[2] Sutton, R. S., & Barto, A. G. (2018). Reinforcement Learning: An Introduction (2nd ed.). MIT Press.

[3] Lapan, M. (2018). Deep Reinforcement Learning Hands-On. Packt Publishing.

[4] Massagué Respall, V., Brown, J., & Aslam, H. (2018). Monte Carlo Tree Search for Quoridor. ResearchGate.

[5] Wang, H., Emmerich, M., & Plaat, A. (2019). Assessing the Potential of Classical Q-learning in General Game Playing. In Proceedings of the International Conference on Agents and Artificial Intelligence. ResearchGate.