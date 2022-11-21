# Parte B

## Preprocesamiento

    1- Se cargó el dataset completo.
    2- Se convirtió la columna inclinación peligrosa a factor.
    3- Se agregaron features porcentaje de arboles con inclinación peligrosa por especie y se agregó una variable categorica según la circunferencia en centimetros del tronco.
    4- Se tomó del dataset todos los arboles con inclinación peligrosa y se eligió aleatoriamente 1.5 veces esa cantidad de arboles para los arboles que no tenian inclinación peligrosa.
    5- Se mezclaron ambos conjuntos y luego dividió en un dataset para el entrenamiento y otro para la validación
    6- Finalmente del dataset de entrenamiento se quitó aquellos arboles cuya especie tenia menos de 3 ocurrencias.

## Resultados de la validación

| n= 1790 | Predicted Positive | Predicted Negative |     |
 | :----:  | :----------------: | :----------------: | :-: |
 | Actual Positive | 615 | 6 | 0.99 | 
 | Actual Negative | 97 | 1072 | 0.92 |
 |  | 0.86 | 0.99 | 0.94 |

## Resultados en Kaggle

| Submission | Score |
| :--------: | :---: |
| report_4.csv | 0.50304 |
| report_5.csv | 0.5 |
| report_6.csv | 0.64098 |
| report_7.csv | 0.60754 |
| report_8.csv | 0.62365 |
| report_9.csv | 0.66597 |
| report_10.csv | 0.59516 |
| report_12.csv | 0.53203 |
| report_13.csv | 0.59569 |
| report_14.csv | 0.59585 |

## Descripción de la solución propuesta

Luego del procesamiento, se seleccionaron algunos de los features iniciales para la formula de entrenamiento:

    - altura
    - diametro_tronco
    - circ_tronco_cm
    - lat
    - long
    - seccion
    - especie

e inicialmente no se había balanceado el dataset en relación a la cantidad de arboles con inclinación peligrosa. Luego se aplicó un algoritmo de random forest para el modelo del arbol y luego se procedió a realizar la validación de la predicción. Luego de la primer iteración decidí eliminar las especies que no tenian muchas ocurrencias en el dataset de entrenamiento y agregar la variable categorica "circ_tronco_cm_cat" a partir de la circunferencia de los troncos. Al no haber mejora en los resultados, se analizó de nuevo el dataset y se tomó la decisión de balancearlo de la manera que se explicó anteriormente en el preprocesamiento. Hubo mejoras en los resultados, pero al no ser suficientes, se procedió a ajustar los parametros del balance del dataset y el limite de ocurrencias para que se tome en cuenta una especie. Luego de un par de ajustes se llegó al mejor resultado obtenido que fue **0.66597**.

A partir de ahí se agregó un nuevo feature, el porcentaje de arboles peligrosos que tenía cada especie en relación a la cantidad de arboles peligrosos totales, eso disminuyó la precisión del modelo, así que se intentó modificar parametros para buscar alguna mejoría, que finalmente no ocurrió.