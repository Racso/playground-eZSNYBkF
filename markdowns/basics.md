# ¡Te doy la bienvenida!

Este *playground* corto te dará algunas bases de teoría de grafos: qué son los grafos, nodos y aristas, y cómo pueden usarse para modelar información y resolver problemas.

¿Te gustaría añadir añadiendo contenido o corrigiendo errores? [¡Encuentra este *playground* en Github!](https://github.com/Racso/playground-eZSNYBkF)

# Prerrequisitos
* Ninguno.

# Grafos, nodos y aristas

Mira la siguiente imagen:

![Ejemplo de grafo](cities.png "")

La imagen representa algunas ciudades colombianas: Cartagena, Bucaramanga, Medellín, Bogotá y otras. Cada círculo es una ciudad. Las líneas conectando los círculos representan vuelos comerciales que puedes tomar entre ciudades. Por ejemplo, puedes volar de Bucaramanga (BUC) a Bogotá (BOG), pues esas ciudades están conectadas con una línea, pero no puedes volar de Pasto (PAS) a Leticia (LET) porque no están conectadas.

Sencillo, ¿no? Pues buen, ese es un grafo, y los grafos son fáciles de entender. Los **grafos** son estructuras que nos permiten modelar relaciones entre elementos. En este caso, usamos un grafo para modelar conexiones aéreas entre ciudades.

Los grafos se componen de dos tipos de elemento:
1. **Vértices o nodos**, que representan elementos. En la imagen, los círculos son los nodos, y cada nodo representa una ciudad.
2. **Aristas**, que representan relaciones entre elementos. En la imagen, las líneas son las aristas, cada una representando una conexión aérea entre dos ciudades.

Cada arista conecta exactamente dos nodos. Esto significa que nunca encontrarás una arista con un lado apuntando hacia la nada.

Se dice que dos nodos son vecinos si hay una arista conectándolos. En el ejemplo, Bucaramanga (BUC) y Bogotá (BOG) son vecinos, pero Pasto (PAS) y Leticia (LET) no lo son.

?[¿Cuántos vecinos tiene el nodo BUC?]
-[ ] 3
-[ ] 6
-[x] 4
-[ ] 5

Un grafo puede dibujarse de diferentes formas sin cambiarlo. Dónde y cómo se dibujen los nodos y las aristas de un grafo no importa; lo que importa es qué nodos contiene el grafo y cómo están conectados entre ellos. Por ejemplo, podemos redibujar nuestro grafo de ciudades de la siguiente forma, sin cambiarlo:

![Ejemplo de grafo, dibujado de otro modo](cities-2.png "")

Con base en un grafo, puedes calcular fácilmente cosas acerca de la situación que estás modelando. Para grafos pequeños, puedes hacerlo a mano. Para grafos mayores, puedes crear programas simples o utilizar algoritmos conocidos para abordar el problema. Intenta resolver las siguientes preguntas acerca de nuestro grafo de ciudades:

?[¿Cuántas ciudades hay?]
-[x] 10
-[ ] 9
-[ ] 8
-[ ] 11

?[Si quisiera ir desde Cartagena (CAR) hasta Pasto (PAS), ¿cuál es la cantidad MÍNIMA de vuelos que tendría que tomar?]
-[x] 3
-[ ] 2
-[ ] 4
-[ ] 5

# Ciclos y aristas paralelas

Our cities graph is a **simple graph**, as it doesn't have **"loops"** or **"parallel edges"**. Let's see what those are. The following graph is **non-simple**:

![Non simple graph](nosimple.png "")

In this graph, there's an edge connecting node 2 with itself. That edge is a loop. In other words, a **loop** is an edge that starts and finishes in the same node. That node is connected to itself, and therefore is its own neighbor.

You can also see that nodes 1 and 3 are connected by two edges. Those edges are "parallel edges", or "multiple edges". In other words, several edges are **parallel edges** if they connect the same pair of nodes.

Loops and parallel edges are useful for certain, specific applications. However, for lots of real life applications (probably most of them), you don't want to have loops or parallel edges in your graphs. Graphs without loops or parallel edges are called **simple graphs**.

# The degree of a node
The **degree** of a node is the amount of edges incident on it. "Edges incident on a node" are edges that connect that node with another one (or itself, in the case of a loop), or edges that "touch" that node.

In a simple graph, the degree of a node is equal to the amount of neighbors it has. On the other hand, when a node has a loop, the loop adds 2 to the degree of the node.

In our non-simple graph example above, the degrees of the nodes are the following:
* deg(**1**) = 3
* deg(**2**) = 3 (remember: the loop adds 2)
* deg(**3**) = 2

# Directed graphs

Let's suppose we want to model some Twitter users with a graph. This is the information about the users:

- Alice (A) follows Bob and Carol.
- Bob (B) follows Alice.
- Carol (C) follows Bob.

OK, cool. We can model people as nodes and "follows" as edges. However, this time we have an extra ingredient: direction.

In Twitter, following a person goes in one direction: you may follow one person, but that person may or may not follow you back. In our example, Carol follows Bob, but Bob doesn't follow Carol back. Something similar happens with personal relationships in real life: you may like a person, but that person may or may not like you back.

Is because of this asymmetry that our graph needs a way to convey who follows whom. This is done with **directed edges**:

![Directed graph example](twitter.png "")

Directed edges look like arrows. They have a starting node and an ending node.

Our directed graph easily shows us some information about our users. For example, it's clear that Alice and Bob follow each other, and that Bob is the person with the most followers (because two arrows point to B).
