__author__ = 'Antonin et Vico'

import math
from typing import Tuple, List

from PROJET.graph import DirectedGraph
from PROJET.graph_parser import create_graph

__Filename = 'Subreddit'
__Creationdate__ = '23/03/2021'


def nodeDegre(graph:DirectedGraph) -> Tuple[List[int], int]:
    tenBest = [0 for _ in range(10)]
    nbrNoLinkCommunities = 0

    for sommet in graph:
        deg = graph.degre(sommet)
        if(deg > tenBest[9]):
            tenBest[9] = deg
            tenBest.sort(reverse=True)
        if(deg == 0):
            nbrNoLinkCommunities += 1
    return tenBest, nbrNoLinkCommunities


def activity(graph: DirectedGraph):
    numberOfCommunitty = len(graph)
    top2percent = []
    mini = math.inf
    indexMin = 0
    for vertex in graph:
        if(len(top2percent) < (2/100) * numberOfCommunitty):
            deg = graph.degre(vertex)
            top2percent.append(deg)
            if(deg < mini):
                mini = deg
                indexMin = len(top2percent) - 1
        else:
            deg = graph.degre(vertex)
            if(deg > mini):
                top2percent[indexMin] = deg

            mini = math.inf
            for i in range(len(top2percent)):
                    v = top2percent[i]
                    if(v < mini):
                        mini = v
                        indexMin = i
    return sorted(top2percent,reverse=True)

def chemins(graphe:DirectedGraph):
    print(graphe.dijkstraSommet("disney", "vegan"))
    print(graphe.dijkstraSommet("greenbaypackers", "missouripolitics"))

print("Loading graph")
grapheReddit = create_graph("soc-redditHyperlinks-title.tsv")
print("Graph loaded")

top2p = activity(grapheReddit)
print("activity : " + str(len(top2p)) + "   /   " + str(top2p))
#
# print(nodeDegre(grapheReddit))
chemins(grapheReddit)