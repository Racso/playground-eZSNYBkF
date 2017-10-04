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

Each edge connects exactly two nodes. This means that you'll never find and edge with one side pointing to nowhere.

We say that two nodes are neighbors if there is an edge connecting them. In the example, Bucaramanga (BUC) and Bogotá (BOG) are neighbors, but Pasto (PAS) and Leticia (LET) are not neighbors.

?[How many neighbors does node BUC have?]
-[ ] 3
-[ ] 6
-[x] 4
-[ ] 5

A graph can be drawn in different ways without changing it at all. How and where you draw the nodes and edges of a graph doesn't matter; what matters is what nodes does the graph contain and how are they connected. For example, our cities graph can be redrawn in the following way, without changing it:

![Graph example, drawn in another way](cities-2.png "")

Based on a graph, you can easily calculate things about the situation you're modelling. For small graphs, you can make it by hand. For bigger graphs, you can code simple programs or use well-known algorithms to tackle the problem. Try solving the following questions about our cities graph:

?[How many cities are there?]
-[x] 10
-[ ] 9
-[ ] 8
-[ ] 11

?[If I want to fly from Cartagena (CAR) to Pasto (PAS), What's the MINIMUM amount of flights that I need to take?]
-[x] 3
-[ ] 2
-[ ] 4
-[ ] 5

# Loops and parallel edges

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