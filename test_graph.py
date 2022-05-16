__author__ = 'Antonin et Vico'
__Filename = 'test_graph'
__Creationdate__ = '20/03/2021'

from graph import DirectedGraph

graph = DirectedGraph()
graph.add_vertex(1)
graph.add_edge(1, 2, 1)
graph.add_edge(2, 1, 1)
graph.add_edge(2, 3, 1)
print(graph.vertices) # affiche dict_keys([1, 2, 3])
print(len(graph)) # affiche 3
print(graph[2]) # affiche {1: 1, 3: 1}
print(graph)
for vertex in graph:
    print(vertex)
    graph.remove_edge(1, 2)
    print(graph)

from graph import UndirectedGraph

ungraph = UndirectedGraph()
ungraph.add_vertex(1)
ungraph.add_edge(1, 2, 1)
ungraph.add_edge(2, 1, 1)
ungraph.add_edge(2, 3, 1)
print(ungraph.vertices) # affiche dict_keys([1, 2, 3])
print(len(ungraph)) # affiche 3
print(ungraph[2]) # affiche {1: 1, 3: 1}
print(ungraph)
for vertex in ungraph:
    print(vertex)
    ungraph.remove_edge(1, 2)
    print(ungraph)

#test dijkstra
from graph_generation import generate_random_graph

graph_d = generate_random_graph(5, 15, True)
assert graph_d.dijkstra(1) == graph_d.dijkstraTas(1)
assert graph_d.dijkstra(3) == graph_d.dijkstraTas(3)

graphee = DirectedGraph()
graphee.add_vertex(1)
graphee.add_edge(1, 2, 1)
graphee.add_edge(2, 3, 1)
graphee.add_edge(3, 4, 1)
graphee.add_edge(4, 5, 1)
graphee.add_edge(5, 6, 1)
graphee.add_edge(6, 2, 1)
graphee.add_edge(4, 3, 1)


print(graphee.bellman_Ford(2))
graphee.draw()


