import abc
import numpy as np


"""
The base class representation
of a graph with all the interface methids
"""


class Graph(abc.ABC):
    def init(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        pass

    @abc.abstractmethod
    def get_adjacent_vert(self, v):
        pass

    @abc.abstractmethod
    def get_degree(self, v):
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractmethod
    def display(self):
        pass

    """ Represent a graph as an adjacency matrix. A cell in the matrix has
         a value when there existan edge betweenthe vertex represent by the
        row and colomn numbers.
        Weighted graphs can hold values > 1 in the matrix cell
        A value of 0 in the celL indicates  that there is no edge """

# Adjacency Matrix

class AdjacencyMatrixGraph(Graph):
    def __init__(self, numVertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(numVertices, directed)
        self.matrix = np.zeros((numVertices, numVertices))

    def add_edge(self, v1, v2, weight=1):
        if v1 >= self.numVertices or v2 >= self.numVertices or v1 < 0 or v2 < 0:
            raise ValueError("vertices are out of bound")

        if weight < 1:
            raise ValueError("An edge cannot have weight < 1")

        self.matrix[v1][v2] = weight

        if self.directed == False:
            self.matrix[v2][v1] = weight

    def get_adjacent_vert(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("cannot access vertex")

        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)

        return adjacent_vertices

    def get_degree(self, v):
        if v < 0 or v >= self.numVertices:
            raise ValueError("cannot access vertex")

        degree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                degree += 1

        return degree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]

    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vert(i):
                print(i, "-->", v)


g = AdjacencyMatrixGraph(4)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)


""" a representation of d undirected graph above
0 ------------1
 -
  -
   -
     -2---------------3
                       """


for i in range(4):
    print("ädjacent to : ", i, g.get_adjacent_vert(1))


for i in range(4):
    print("degree : ", i, g.get_degree(1))


for i in range(4):
    for j in g.get_adjacent_vert(i):
        print("edge weight: ", i, "", j, "weight: ", g.get_edge_weight(i, j))

g.display()


" For a directed Graph"

g = AdjacencyMatrixGraph(4, directed=True)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)


""" a representation of d directed graph above
0 ------------> 1
 -
  -
   -
     - > 2---------------> 3
                       """


for i in range(4):
    print("ädjacent to : ", i, g.get_adjacent_vert(1))


for i in range(4):
    print("degree : ", i, g.get_degree(1))


for i in range(4):
    for j in g.get_adjacent_vert(i):
        print("edge weight: ", i, "", j, "weight: ", g.get_edge_weight(i, j))

g.display()
