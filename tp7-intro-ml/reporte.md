# Introducción a Machine Learning

## Respuestas a las preguntas indicadas del libro Introduction to Statistical Learning.

1-

    a-  En este caso sería mejor, un enfoque más flexible ajustará los datos más cerca y con el tamaño de muestra grande se obtendría un mejor ajuste que un enfoque inflexible.

    b-  Sería peor, un método flexible sobreajustaría el pequeño número de observaciones.

    c-  Sería mejor, con más grados de libertad, un modelo flexible obtendría una mejor ajuste
    
    d-  Peor, los métodos flexibles se ajustan al ruido en los términos de error y aumentan la varianza

2-

    a-  Se trata de un problema de regresión donde interesa más la inferencia.
        n <- 500
        p <- 5
    
    b-  Se trata de un problema de clasificación donde se busca predecir el éxito o el fracaso de un nuevo producto.
        n <- 20
        p <- 14
    
    c-  Se trata de un problema de regresión donde interesa más la predicción         
        n <- 48
        p <- % 4
    
5-  
    
    Las ventajas de un enfoque muy flexible para la regresión o la clasificación son la obtención de un mejor ajuste para los modelos no lineales, lo que reduce el sesgo.

    Las desventajas de un enfoque muy flexible para la regresión o la clasificación son la necesidad de estimar un mayor número de parámetros, seguir el ruido demasiado de cerca (sobreajuste), aumentando la varianza.

    Se preferiría un enfoque más flexible a un enfoque menos flexible cuando estamos interesados en la predicción y no en la interpretabilidad de los resultados.

    Se preferiría un enfoque menos flexible a un enfoque más flexible cuando estamos interesados en la inferencia y la interpretabilidad de los resultados.

6-

    Un enfoque paramétrico reduce el problema de estimar f a uno de estimar un conjunto de parámetros porque asume una forma para f.

    Un enfoque no paramétrico no asume una forma funcional para f y, por lo tanto, requiere una gran cantidad de observaciones para estimar f con precisión.

    Las ventajas de un enfoque paramétrico de regresión o clasificación son la simplificación del modelado f a unos pocos parámetros y no se requieren tantas observaciones en comparación con un enfoque no paramétrico.

    Las desventajas de un enfoque paramétrico para la regresión o la clasificación son la posibilidad de estimar de manera imprecisa f si la forma de f asumida es incorrecta o sobreajustar las observaciones si se utilizan modelos más flexibles.

7-
    
    a-  

| Obs | X1 | X2 | X3 | Distancia(0, 0, 0) | Y |
| :---: | :---: | :---: | :---: | :---: | :---: |
|  1 |  0 | 3 |0 |  3   | Rojo  |
|   2   | 2 | 0 | 0 | 2 | Rojo  |
|3 |0 |1 |3 | 3.2| Rojo|
|4 |0 |1 |2 | 2.2 |Verde|
|5 |-1 |0 |1 | 1.4 |Verde|
|6 |1 |1 |1 |   1.7 |Rojo|
    
    b-  Verde. La observación #5 es el vecino más cercano para K = 1.

    c-  Rojo. Las observaciones #2, 5, 6 son los vecinos más cercanos para K = 3. 2 es rojo, 5 es verde y 6 es rojo.

    d-  Pequeño, una K pequeña sería flexible para un límite de decisión no lineal, mientras que una K grande intentaría ajustarse a un límite más lineal porque tiene en cuenta más puntos.