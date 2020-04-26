from queue import Queue

from graph import *



def build_distance_table(graph, source):

    distance_table = {}

    for i in range(graph.numVertices):
        distance_table[i] = (None, None)

    distance_table[source] = (0, source)

    queue = Queue()
    queue.put(source)

    while not queue.empty():
        current_vertex = queue.get()


        current_distance = distance_table[current_vertex][0]

        for neighbour in graph.get_adjacent_vert(current_vertex):

            if distance_table[neighbour][0] is None:
                distance_table[neighbour] = (1 + current_distance, current_vertex)


                if len(graph.get_adjacent_vert(neighbour)) > 0:
                    queue.put(neighbour)

        return distance_table



def shortest_path(graph, source, destination):
    distance_table = build_distance_table(graph, source)

    path = [destination]

    previous_vertex = distance_table[destination][1]

    while previous_vertex is not None and previous_vertex is not source:

        path = [previous_vertex] + path

        previous_vertex = distance_table[previous_vertex][1]


    if previous_vertex is None :
        print("There is no path ")

    else:
        path = [source] + path

        print("shortest path is : ", path)


gr = AdjacencyMatrixGraph(8, directed=False)
gr.add(0, 1)
gr.add(1, 2)
gr.add(0, 1)
gr.add(1, 3)
gr.add(2, 3)
gr.add(1, 4)
gr.add(3, 5)
gr.add(5, 4)
gr.add(3, 6)
gr.add(6, 7)
gr.add(0, 7)




shortest_path(g, 0, 5)
shortest_path(g, 0, 6)
shortest_path(g, 7, 4)