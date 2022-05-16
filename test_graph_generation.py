__author__ = 'Antonin et Vico'
__Filename = 'test_graph_generation'
__Creationdate__ = '20/03/2021'

from graph_generation import generate_random_graph, drawCummunityGraph, generate_random_community_graph_compteur
from graph_generation import generate_random_community_graph
import math

#test generate random graph

graph_1 = generate_random_graph(0, 0, False)
graph_2 = generate_random_graph(0, 0, True)

assert len(graph_1) == len(graph_2) ==  0


graph_3 = generate_random_graph(5, 0, False)
graph_4 = generate_random_graph(5, 0, True)

assert len(graph_3) == len(graph_4) == 5 and graph_3.numberOfEdges ==  graph_4.numberOfEdges == 0

graph_5 = generate_random_graph(5, 150, False)
graph_6 = generate_random_graph(5, 150, True)

assert len(graph_5) == len(graph_6) == 5 and graph_5.numberOfEdges == 10 and graph_6.numberOfEdges == 20

graph_7 = generate_random_graph(0,5, False)
graph_8 = generate_random_graph(0,5, True)

assert len(graph_7) == len(graph_8) == 0 and graph_7.numberOfEdges == graph_8.numberOfEdges == 0

#test generate_random_community_graph

community_1 = generate_random_community_graph([0], 0, 0)
community_2 = generate_random_community_graph([1,2,3,4], 0, 0)
community_3 = generate_random_community_graph([1,2,3,4], 1, 1)
community_4 = generate_random_community_graph([1,2,3,4], 1, 0)
community_5 = generate_random_community_graph([1,2,3,4], 0, 1)

assert len(community_1) == community_1.numberOfEdges == community_2.numberOfEdges == 0
assert len(community_2) == len(community_3) == len(community_4) == len(community_5) == 10
assert community_3.numberOfEdges == 45
assert community_4.numberOfEdges == 10
assert community_5.numberOfEdges == 35

def test_community():
    pop, p_in, p_out = [5, 10, 20], .4, .7
    in_edges = sum(p ** 2 for p in pop)
    out_edges = sum(pop) ** 2 - in_edges
    expected, z = in_edges * p_in + out_edges * p_out, 2.58
    pm = z * (math.sqrt(in_edges * p_in * (1 - p_in)) + math.sqrt(out_edges * p_out * (1 - p_out)))
    com_g = generate_random_community_graph(pop, p_in, p_out)
    edges = sum(len(com_g[d]) for d in com_g)
    assert abs(expected - edges) < pm


#test de dijkstra rapide avec tas

graph_9 = generate_random_graph(5, 20)
assert graph_9.dijkstra(0) == graph_9.dijkstraTas(0)
graph_10 = generate_random_graph(20, 500)
assert graph_10.dijkstra(0) == graph_10.dijkstraTas(0)
