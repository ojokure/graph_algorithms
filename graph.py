import abc
import numpy as np


class Graph(abc.ABC):
    def init(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed
