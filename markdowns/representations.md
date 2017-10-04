Ya sabemos qué son los grafos. Ahora, veamos cómo podemos representar grafos de otros modos además de dibujarlos. Ello será útil si queremos trabajar con grafos con un computador.

# Lista de adyacencia

¿Recuerdas nuestro grafo de ciudades?

![Grafo de ejemplo](cities.png "")

Hagamos una lista de los vecinos de cada nodo:

* **CAR:** MED, BUC
* **MED:** CAR, BUC, BUE, ARM, BOG
* **BUC:** CAR, MED, BOG, YOP
* **BUE:** MED, CAL, PAS
* **ARM:** MED, BOG, CAL
* **BOG:** MED, BUC, YOP, ARM, CAL
* **YOP:** BUC, ARM, BOG, LET
* **CAL:** BUE, ARM, BOG, YOP, LET, PAS
* **PAS:** BUE, CAL
* **LET:** CAL, YOP

Esa es la **lista de adyacencia** del grafo: una lista de listas describiendo los vecinos de cada nodo.

Si el grafo es dirigido, un nodo B sólo aparece en la lista de un nodo A si hay una arista desde A hacia B. Por ejemplo, en nuestro grafo dirigido de Twitter:

![Grafo dirigido de ejemplo](twitter.png "")

* **A:** B, C
* **B:** A
* **C:** B

# Matriz de adyacencia

Los grafos también pueden representarse con **matrices de adyacencia**. Aquí está la matriz de adyacencia de nuestro grafo de ciudades:

|	|CAR	|BUC	|YOP	|BOG	|LET	|CAL	|ARM	|MED	|BUE	|PAS    |
|---	|---	|---	|---	|---	|---	|---	|---	|---	|---	|---    |
|**CAR**|0	|1	|0	|0	|0	|0	|0	|1	|0	|0      |
|**BUC**|1	|0	|1	|1	|0	|0	|0	|1	|0	|0      |
|**YOP**|0	|1	|0	|1	|1	|1	|1	|0	|0	|0      |
|**BOG**|0	|1	|1	|0	|0	|1	|1	|1	|0	|0      |
|**LET**|0	|0	|1	|0	|0	|1	|0	|0	|0	|0      |
|**CAL**|0	|0	|1	|1	|1	|0	|1	|0	|1	|1      |
|**ARM**|0	|0	|1	|1	|0	|1	|0	|1	|0	|0      |
|**MED**|1	|1	|0	|1	|0	|0	|1	|0	|1	|0      |
|**BUE**|0	|0	|0	|0	|0	|1	|0	|1	|0	|1      |
|**PAS**|0	|0	|0	|0	|0	|1	|0	|0	|1	|0      |

Una matriz de adyacencia tiene los nodos del grafo listados en sus filas y columnas. El valor en cada celda indica si existe una arista entre el par de nodos correspondiente a la fila y la columna. Por ejemplo, la celda en la fila **BOG** y la columna **BUC** tiene un valor de **1** porque existe una arista entre BOG y BUC, mientras que la celda en la fila **PAS** y la columna **YOP** tiene un **0** porque no hay arista entre esos dos nodos.

Un grafo puede tener varias matrices de adyacencia. En el ejemplo anterior, si pones los nodos en un orden diferente, tendrás una nueva matriz de adyacencia del mismo grafo.

Como puedes ver, si un grafo es no dirigido, las matrices de adyacencia son simétricas. Por otro lado, si el grafo es dirigido, las matrices no son simétricas, pues un 1 sólo aparece en una celda si hay una arista desde el nodo de la fila hasta el nodo de la columna. Por ejemplo, la siguiente es la matriz de adyacencia de nuestro grafo de Twitter.

|   | A | B | C |
|---|---|---|---|
|**A**|0|1|1|
|**B**|1|0|0|
|**C**|0|1|0|

# Ejercicio
La función de Python mostrada se utiliza para obtener información sobre un grafo dado. El grafo se pasa a la función como una lista de adyacencia, y la función retorna el grado máximo de un nodo en el grafo, el número de ciclos en el grafo y un valor de tipo *boolean* indicando si el grafo tiene aristas paralelas o no.

Arregla la función para que devuelva la información deseada. Puese asumir que el grafo tendrá como máximo 5 nodos, numerados del 1 al 5.

@[La función debe devolver alguna información sobre un grafo dado. Corrígela para que lo haga correctamente.]({"stubs": ["graphs.py"], "command": "python3 test_graphs.py"})

# Finalización
¡Felicidades! Ahora conoces algunos conceptos fundamentales de teoría de grafos. Ahora, puedes aprender más conceptos sobre los grafos, o empezar a aprender algoritmos útiles para aplicar. ¡La decisión es tuya!
