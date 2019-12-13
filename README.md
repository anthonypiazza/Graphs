# Graphs

# Intro to Graphs

![Directed Graph](img/graph.png)

## Objectives

* Learn what graphs are
* Learn the components of graphs
* Learn what graphs are useful for

## What Are Graphs?

Graphs are collections of related data. They're like trees, except connections can be made from any node to any other node, even forming loops.

The nodes in a graph are called _vertexes_ (or _vertices_ or _verts_), and the connections between the verts are called _edges_.

And edge denotes a relationship or linkage between the two verts.


## What can they represent?

Graphs can represent any kind of multiway relational data.

This could be a collection of cities and linking roads.

It could be a collection of computers on a network.

It could be a population of people who know each other and [Kevin
Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon).

It could represent trade relationships between nations.

And so on.

![Different ways to represent a graph](img/representations.PNG)

## Definitions

### Directed/Undirected Graphs

If the edges are "one way" (have an arrow), the graph is said to be a
_directed graph_. If there are no arrows, the edges are bidirectional
and the graph is an _undirected_ graph.

![Undirected Graph](img/social_graph_undirected.jpg)

This is an __undirected graph__ which could represent a social network like Facebook. Alice is friends with Bob, Carol and Dave, Bob is friends with Alice and Dave, Carol is only friend with Alice, and Dave is friends with only Alice and Bob. In this example, the nodes represent people and the edges represent friendship.

![Directed Graph](img/social_graph_directed.jpg)

This is an __directed graph__ which could represent a social network like Twitter or Instagram. Since Twitter/Instagram follows are one-way as opposed to always-mutual Facebook friendships, they are represented with arrows. In the above directed graph, Alice and Bob follow each other, Dave follows Alice and Bob, and Carol only follows Alice.

### Cyclic/Acyclic Graphs

If a cycle can be formed (e.g. you can follow the edges and arrive again at an already-visited vert), the graph is _cyclic_. Otherwise it is _acyclic_.

### Dense/Sparse Graphs

A graph where most vertices are connected to each other is considered _dense_. A graph with less connections is _sparse_. There is no exact cutoff for this specification, but you could say that a [Flight map](https://news.delta.com/route-map-us-canada) is more dense than a [Subway map](http://web.mta.info/maps/submap.html).

### Weighted Graphs

Graphs with values (_weights_) associated with the edges are called _weighted graphs_.

The meaning of the weight is dependent on the type of graph. A graph of road network segments might have weight represent the length of the road. The higher the total weight of a route on the graph, the longer the trip is. The weights can be used to help decide if a particular route should be chosen over another.

![Directed Graph](img/GoogleMaps.jpg)

Weights can be further modified. For example, if one were building a bicycle map, roads with bad car traffic or very steep uphills could be given unnaturally large weights so a routing algorithm would be unlikely to take them. (This is how Google Maps avoids freeways when you ask it for walking directions.)

### Directed Acyclic Graphs (DAGs)

A _directed acyclic graph_ (_DAG_) has a number of applications. From [Wikipedia](https://en.wikipedia.org/wiki/Directed_acyclic_graph):

> DAGs can model many different kinds of information. A spreadsheet can
> be modeled as a DAG, with a vertex for each cell and an edge whenever
> the formula in one cell uses the value from another; a topological
> ordering of this DAG can be used to update all cell values when the
> spreadsheet is changed. Similarly, topological orderings of DAGs can
> be used to order the compilation operations in a makefile. The program
> evaluation and review technique uses DAGs to model the milestones and
> activities of large human projects, and schedule these projects to use
> as little total time as possible. Combinational logic blocks in
> electronic circuit design, and the operations in dataflow programming
> languages, involve acyclic networks of processing elements. DAGs can
> also represent collections of events and their influence on each
> other, either in a probabilistic structure such as a Bayesian network
> or as a record of historical data such as family trees or the version
> histories of distributed revision control systems. DAGs can also be
> used as a compact representation of sequence data, such as the
> directed acyclic word graph representation of a collection of strings,
> or the binary decision diagram representation of sequences of binary
> choices.

It's notable that git uses a DAG to represent commits. A commit can have a child
commit, or more than one child commit (in the case of a branch). A child could
come from one parent commit, or from two (in the case of a merge). But there's
no way to go back and form a repeating loop in the git commit hierarchy.

## Exercises

Draw examples of the following:

* Undirected graph of 4 verts.
* Directed graph of 5 verts.
* Cyclic directed graph of 6 verts.
* DAG of 7 verts.

# Intro to Graphs

## Objectives

* Learn how to represent a graph as an adjacency list
* Learn how to represent a graph as an adjacency matrix
* Learn the tradeoffs of the respective representations

## Graph Representations


![Different ways to represent a graph](img/representations.PNG)


The two most common ways to represent graphs in code are adjacency lists and adjacency matrices, each with its own strengths and weaknesses. When deciding on a graph implementation, it's important to understand the type of data and operations you will be using.

## Adjacency List

In an adjacency list, the graph stores a list of vertices and for each vertex, a list of each vertex to which it's connected. So, for the following graph...

![Different ways to represent a graph](img/sample-graph.PNG)

...an adjacency list in Python could look something like this:

```python
class Graph:
    def __init__(self):
        self.vertices = {
                          "A": {"B"},
                          "B": {"C", "D"},
                          "C": {"E"},
                          "D": {"F", "G"},
                          "E": {"C"},
                          "F": {"C"},
                          "G": {"A", "F"}
                        }
```

Note that this adjacency list doesn't actually use any lists. The `vertices` collection is a `dictionary` which lets us access each collection of edges in O(1) constant time while the edges are contained in a `set` which lets us check for the existence of edges in O(1) constant time.

## Adjacency Matrix

Now, let's see what this graph might look like as an adjacency matrix:

```python
class Graph:
    def __init__(self):
        self.edges = [[0,1,0,0,0,0,0],
                      [0,0,1,1,0,0,0],
                      [0,0,0,0,1,0,0],
                      [0,0,0,0,0,1,1],
                      [0,0,1,0,0,0,0],
                      [0,0,1,0,0,0,0],
                      [1,0,0,0,0,1,0]]
```

We represent this matrix as a two-dimensional array, or a list of lists. With this implementation, we get the benefit of built-in edge weights but do not have an association between the values of our vertices and their index.

In practice, both of these would probably contain more information by including Vertex or Edge classes.


## Tradeoffs

Both adjacency matrices and adjacency lists have their own strengths and weaknesses. Let's explore their tradeoffs.

For the following:

```
V: Total number of vertices in the graph
E: Total number of edges in the graph
e: Average number of edges per vertex
```

### Space Complexity

* **Adjacency Matrix**: O(V ^ 2)

* **Adjacency List**: O(V + E)

Consider a sparse graph with 100 vertices and only one edge. An adjacency list would have to store all 100 vertices but only needs to keep track of that single edge. The adjacency matrix would need to store 100x100=10,000 possible connections, even though all but one would be 0.

Now consider a dense graph where each vertex points to each other vertex. In this case, the total number of edges will approach V^2 so the space complexities of each are comparable. However, dictionaries and sets are less space efficient than lists so for dense graphs, the adjacency matrix is more efficient.

Takeaway: Adjacency lists are more space efficient for __sparse__ graphs while adjacency matrices become efficient for __dense__ graphs.


### Add Vertex

* **Adjacency Matrix**: O(V)

* **Adjacency List**: O(1)

Adding a vertex is extremely simple in an adjacency list:

```Python
self.vertices["H"] = set()
```

Adding a new key to a dictionary is a constant-time operation.

For an adjacency matrix, we would need to add a new value to the end of each existing row, then add a new row at the end.

```Python
for v in self.edges:
  self.edges[v].append(0)
v.append([0] * len(self.edges + 1))
```

Remember that with Python lists, appending to the end of a list is usually O(1) due to over-allocation of memory but can be O(n) when the over-allocated memory fills up. When this occurs, adding the vertex can be O(V^2).

Takeaway: Adding vertices is very efficient in adjacency lists but very inefficient for adjacency matrices.


### Remove Vertex

* **Adjacency Matrix**: O(V ^ 2)

* **Adjacency List**: O(V)

Removing vertices is pretty inefficient in both representations. In an adjacency matrix, we need to remove the removed vertex's row, then remove that column from each other row. Removing an element from a list requires moving everything after that element over by one slot which takes an average of V/2 operations. Since we need to do that for every single row in our matrix, that results in a V^2 time complexity. On top of that, we need to reduce the index of each vertex after our removed index by 1 as well which doesn't add to our quadratic time complexity, but does add extra operations.

For an adjacency list, we need to visit each vertex and remove all edges pointing to our removed vertex. Removing elements from sets and dictionaries is a O(1) operation, so this results in an overall O(V) time complexity.

Takeaway: Removing vertices is inefficient in both adjacency matrices and lists but more inefficient in matrices.


### Add Edge

* **Adjacency Matrix**: O(1)

* **Adjacency List**: O(1)

Adding an edge in an adjacency matrix is quite simple:

```Python
self.edges[v1][v2] = 1
```

Adding an edge in an adjacency list is similarly simple:

```Python
self.vertices[v1].add(v2)
```

Both are constant-time operations.

Takeaway: Adding edges to both adjacency lists and matrices is very efficient.


### Remove Edge

* **Adjacency Matrix**: O(1)

* **Adjacency List**: O(1)

Removing an edge from an adjacency matrix is quite simple:

```Python
self.edges[v1][v2] = 0
```

Removing an edge from an adjacency list is similarly simple:

```Python
self.vertices[v1].remove(v2)
```

Both are constant-time operations.

Takeaway: Removing edges from both adjacency lists and matrices is very efficient.


### Find Edge

* **Adjacency Matrix**: O(1)

* **Adjacency List**: O(1)

Finding an edge in an adjacency matrix is quite simple:

```Python
return self.edges[v1][v2] > 0
```

Finding an edge in an adjacency list is similarly simple:

```
return v2 in self.vertices[v1]
```

Both are constant-time operations.

Takeaway: Finding edges from both adjacency lists and matrices is very efficient.


### Get All Edges from Vertex

* **Adjacency Matrix**: O(V)

* **Adjacency List**: O(1)

Say you want to know all the edges originating from a particular vertex. With an adjacency list, this is as simple as returning the value from the vertex dictionary:

```Python
return self.vertex[v]
```

In an adjacency matrix, however, it's a bit more complicated. You would need to iterate through the entire row and populate a list based on the results:

```Python
v_edges = []
for v2 in self.edges[v]:
    if self.edges[v][v2] > 0:
        v_edges.append(v2)
return v_edges
```

Takeaway: Fetching all edges is more efficient in an adjacency list than an adjacency matrix.











## Objectives

* [Graph Intro](objectives/graph-intro)
* [Graph Representations](objectives/graph-representations)
* [Breadth First Search](objectives/breadth-first-search)
* [Depth First Search](objectives/depth-first-search)
* [Randomness](objectives/randomness)
* [Connected Components](objectives/connected-components)

## Projects

### Day 1
* [Graph Traversal and Search](projects/graph)

### Day 2
* [Earliest Ancestor](projects/ancestor)

### Day 3
* [Random Social Network](projects/social)

### Day 4
* [Adventure Map Traversal](projects/adventure)
