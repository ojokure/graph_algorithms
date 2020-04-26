from queue import Queue

from graph import *




def breadth_first(graph, start=0):
    queue = Queue()
    queue.put(start)

    visited = np.zeros(graph.numVertices)

    while not queue.empty():
        vertex = queue.get()

        if visited[vertex] == 1:
            continue

        print("visited: ", vertex)

        visited[vertex] = 1 

        for v in graph.get_adjacent_vert(vertex):
            if visited[v] != 1:
                queue.put(v)