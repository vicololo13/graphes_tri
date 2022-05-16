__author__ = 'Antonin et Vico'

import heapq
import math

__Filename = 'graph.py'
__Creationdate__ = '09/03/2021'

from typing import KeysView, List, Dict, Set, Tuple, Any
import networkx as nx
import matplotlib.pyplot as plt


class DirectedGraph:

    def __init__(self: 'DirectedGraph') -> None:
        self.edges:Dict[Any, Dict[Any, float]] = dict()

    @property
    def vertices(self: 'DirectedGraph') -> KeysView[Any]:
        return self.edges.keys()

    @property
    def numberOfEdges(self: 'DirectedGraph') -> int:
        res = 0
        for vertex in self.edges:
            res += len(self.edges[vertex])
        return res


    def add_vertex(self: 'DirectedGraph', vertex:Any) -> None:
        if(not vertex in self.edges):
          self.edges[vertex] = dict()


    def remove_vertex(self: 'DirectedGraph', vertex:Any) -> None:
        self.edges.pop(vertex)


    def add_edge(self : 'DirectedGraph', u:Any, v:Any, weight:float) -> None:
        if(weight < 0):
            return

        if(not u in self.edges):
            self.add_vertex(u)

        if(not v in self.edges):
            self.add_vertex(v)

        self.edges[u][v] = weight


    def remove_edge(self: 'DirectedGraph', u: Any, v:Any) -> None:
        if(u in self.edges and v in self.edges[u]):
            self.edges[u].pop(v)


    def change_weigth(self: 'DirectedGraph', u:Any, v:Any, weight:float) -> None:
        if(weight < 0):
            return

        if(u in self.edges):
            self.edges[u][v] = weight


    def reset(self: 'DirectedGraph') -> None:
        self.edges = dict()


    def induced_subgraph(self: 'DirectedGraph', subset:list):
        res:DirectedGraph = DirectedGraph()

        for u in self.edges:
            for v in self.edges[u]:
                if(u in subset and v in subset):
                    res.add_edge(u, v, self.edges[u][v])

        return res


    def draw(self: 'DirectedGraph', colors: List[int] = None):
        if(colors is None or len(colors) != len(self)):
            nx.draw(nx.from_dict_of_lists(self.edges), with_labels=True)
        else:
            nx.draw(nx.from_dict_of_lists(self.edges), with_labels=True, node_color=colors)
        plt.show()


    def edge_exist(self: 'DirectedGraph', u: Any, v: Any):
        return v in self.edges[u]


    def dijkstra(self: 'DirectedGraph', sommet: Any) -> Tuple[Dict[Any, float], Dict[Any, Any]]:
        dist:Dict[Any, float] = dict()
        pred:Dict[Any, Any] = dict()

        for vertex in self.edges:
            dist[vertex] = math.inf
            pred[vertex] = None

        dist[sommet] = 0
        vertices:Set[Any] = set(self.edges.keys())

        while(len(vertices) > 0):
            u = 0
            minDist = math.inf
            for vertex in vertices:
                if(dist[vertex] <= minDist):
                    u = vertex
                    minDist = dist[vertex]
            distU = dist[u]

            vertices.remove(u)

            for vertex in vertices:
                if(vertex not in self.edges[u]):
                    continue
                distVert = dist[vertex]
                if(distVert > distU + self.edges[u][vertex]):
                    dist[vertex] = distU + self.edges[u][vertex]
                    pred[vertex] = u

        return dist, pred




    def dijkstraTas(self: 'DirectedGraph', sommet: Any) -> Tuple[Dict[Any, float], Dict[Any, Any]]:
        dist:Dict[Any, float] = dict()
        queue:List[Tuple[float, Any]] = []
        pred:Dict[Any, Any] = dict()

        for vertex in self.edges:
            value = math.inf if vertex != sommet else 0
            dist[vertex] = value
            heapq.heappush(queue, (value, vertex))
            pred[vertex] = None

        vertices:Set[Any] = set(self.edges.keys())

        while(len(vertices) > 0):
            distU, u = heapq.heappop(queue)
            if(u not in vertices):
                continue
            vertices.remove(u)

            for vertex in vertices:
                if(vertex not in self.edges[u]):
                    continue
                distVert = dist[vertex]
                if(distVert > distU + self.edges[u][vertex]):
                    dist[vertex] = distU + self.edges[u][vertex]
                    heapq.heappush(queue, (dist[vertex], vertex))
                    pred[vertex] = u

        return dist, pred


    def dijkstraSommet(self: 'DirectedGraph', vertexFrom: Any, vertexTo: Any) -> Tuple[float, List[Any]]:
        dist:Dict[Any, float] = dict()
        pred:Dict[Any, Any] = dict()
        queue:List[Tuple[float, Any]] = []

        for vertex in self.edges:
            value = math.inf if vertex != vertexFrom else 0
            dist[vertex] = value
            heapq.heappush(queue, (value, vertex))
            pred[vertex] = None

        vertices:Set[Any] = set(self.edges.keys())

        while(len(vertices) > 0):
            distU, u = heapq.heappop(queue)
            if(u not in vertices):
                continue
            vertices.remove(u)

            for vertex in vertices:
                if(vertex not in self.edges[u]):
                    continue
                distVert = dist[vertex]
                if(distVert > distU + self.edges[u][vertex]):
                    dist[vertex] = distU + self.edges[u][vertex]
                    heapq.heappush(queue, (dist[vertex], vertex))
                    pred[vertex] = u

            if(u == vertexTo):
                predRes:List[Any] = []
                vertPred = vertexTo
                while(vertPred != vertexFrom):
                    predRes.append(vertPred)
                    vertPred = pred[vertPred]
                predRes.reverse()
                return dist[vertexTo], predRes



    def degre(self: 'DirectedGraph', sommet:Any) -> int:
        return len(self.edges[sommet])


    def to_networkx(self: 'DirectedGraph') -> nx.DiGraph:
        return nx.from_dict_of_lists(self.edges)



    def bellman_Ford(self: 'DirectedGraph', sommet:Any) -> Dict[Any, float]:
        distance:Dict[int, Dict[Any, float]] = dict()

        distance[0] = dict()
        for vertex in self.edges:
            distance[0][vertex] = math.inf
        distance[0][sommet] = 0

        for k in range(1, len(self.edges)):
            distance[k] = dict()
            for vertex in self.edges:
                d = distance[k-1][vertex]
                for u in self.edges:
                    if(self.edge_exist(u, vertex)):
                        d = min(d, distance[k-1][u] + self.edges[u][vertex])
                    distance[k][vertex] = d

        return distance[len(self.edges) - 1]



    def __len__(self: 'DirectedGraph') -> int:
        return len(self.edges)


    def __getitem__(self: 'DirectedGraph', item: Any) -> dict:
        return self.edges.get(item, dict())


    def __iter__(self: 'DirectedGraph'):
        for u in self.edges:
            yield u

    def __str__(self: 'DirectedGraph'):
        st = "Vertices : \n"

        for u in self.edges:
            st += "    " + str(u) + "\n"

        st += "Edges: \n"

        for u in self.edges:
            for v in self.edges[u]:
                st += "    " + str(u)  + " -> " + str(v) + "\n"

        return st


class UndirectedGraph(DirectedGraph):
    def __init__(self):
        super().__init__()

    def add_edge(self : 'UndirectedGraph', u:Any, v:Any, weight:float) -> None:
        super().add_edge(u, v, weight)
        super().add_edge(v, u, weight)

    def remove_edge(self: 'UndirectedGraph', u: Any, v:Any) -> None:
        super().remove_edge(u, v)
        super().remove_edge(v, u)

    def change_weigth(self: 'UndirectedGraph', u:Any, v:Any, weight:float) -> None:
        super().change_weigth(u, v, weight)
        super().change_weigth(v, u, weight)

    @property
    def numberOfEdges(self: 'DirectedGraph') -> int:
        return int(super().numberOfEdges / 2)




