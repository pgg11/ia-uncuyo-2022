2.10 Considere una versión modificada del entorno de aspiradora en el ejercicio 2.8, en el que se penaliza al agente con un punto por cada movimiento.

    a. ¿Puede un agente reflexivo simple ser perfectamente racional para este entorno? Explique.
    b. ¿Qué pasa en el caso de un agente reflexivo con estado? Diseñe tal agente.
    c. ¿Cómo cambian sus respuestas a **a** y **b** si las percepciones del agente le dan el estado limpio/sucio de cada cuadrado del entorno?

2.11 Considere una versión modificada del entorno de aspiradora del ejercicio 2.8, en el que se desconoce la geografía del entorno (su extensión, límites y obstáculos), al igual que la configuración inicial de la basura. (El agente puede ir hacia arriba y hacia abajo, así como hacia la izquierda y hacia la derecha).
    a. ¿Puede un agente reflexivo simple ser perfectamente racional para este entorno? Explique.
    b. ¿Puede un agente reflexivo simple con una función de agente aleatorio superar a un agente reflexivo simple? Diseñe un agente de este tipo y mida su rendimiento en varios entornos.
    c. ¿Puede diseñar un entorno en el que su agente aleatorio tenga un desempeño deficiente? Muestra tus resultados.
    d. ¿Puede un agente reflexivo con estado superar a un agente reflejo simple? Diseñe un agente de este tipo y mida su rendimiento en varios entornos. ¿Puedes diseñar un agente racional de este tipo?

### **Respuestas**

2.10 
    a. No, dentro de esa versión modificada de entorno el agente reflexivo simple no es perfectamente racional. Solo sigue una serie de instrucciones dadas, y solo se detiene cuando se le terminan los movimientos. El agente presentado en este trabajo sigue moviendose hasta llegar a la última posición de la grilla, como no tiene percepción de cuanta basura queda, es muy probable que siga moviendose incluso cuando no le conviene, por lo que la mayoría de las veces terminaría con una performance negativa.

    b. En entornos pequeños, dadas ciertas circunstancias el agente aleatorio es capaz de igualar o incluso superar al agente reflexivo simple. Pero a medida que los entornos son más grandes, el agente reflexivo simple tiene mejor performance.

    c. Si se le diera la información del estado limpio/sucio de cada celda al agente reflexivo simple, mejoraría su performance, pero al ser que el estado inicial del agente es aleatorio y solo puede seguir una serie de movimientos condicionados, aún no sería perfecto. Aunque la performance en comparación al agente aleatorio se incrementaría.

2.11
    a. El agente reflexivo simple no sería perfectamente racional para este entorno, ya que al tener movimientos atados solo a condiciones sencillas(por la falta de información del entorno) y al no tener ningun tipo de memoria, no podría recorrer toda la grilla.

    b. El agente aleatorio es capaz de igualar o incluso superar al agente reflexivo simple solo en entornos pequeños, ya que al compararlos en entornos más grandes hay mayor probabilidad de que la performance del agente reflexivo simple sea mejor por el hecho de que recorre la grilla de manera secuencial a partir del punto donde es ubicado, pero limpia de manera más eficiente que el agente aleatorio que si bien puede llegar a lugares donde el otro agente no, tambien puede no limpiar cuadrillas sucias por su aleatoriedad.

    c. Como se muestra en los resultados, a partir de entornos de 16x16 es muy notoria la deficiencia del agente aleatorio, que está más marcada cuando el porcentaje de suciedad aumenta.

    d. Si, un agente con estado superaría al agente reflexivo simple sin estado, ya que tiene un panorama del entorno, lo que le permite saber de antemano cual va a ser el nuevo panorama dependiendo la acción que tome y eso le permite recorrer el entorno de mejor manera.