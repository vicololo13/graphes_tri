__author__ = 'Antonin et Vico'

import math
from typing import List

__Filename = 'experiences_graphs'
__Creationdate__ = '23/03/2021'


from PROJET.graph_generation import generate_random_graph
from time import process_time
import numpy as np
import matplotlib.pyplot as plt
import random as rand
import networkx as nx



def dijkstra_test_speed(nMin:int, nMax:int, alpha:float, pas:int = 1) -> None:
    tempsNormal = []
    tempsRapide = []
    print("Starting dijkstra test speed")
    for nbreSommets in range(nMin,nMax, pas):
        print("    calculing for " + str(nbreSommets) + " vertices... " + str(round(((nbreSommets - nMin)/ ( (nMax - nMin)) ) * 100, 2)) + " %")
        graph = generate_random_graph(nbreSommets, math.floor(alpha * nbreSommets * nbreSommets))

        t0 = process_time() # début chronométrage
        graph.dijkstra(0)
        t1 = process_time() # fin chronométrage
        tempsNormal.append(t1 - t0)

        t0 = process_time() # début chronométrage
        graph.dijkstraTas(0)
        t1 = process_time() # fin chronométrage
        tempsRapide.append(t1 - t0)

    plt.plot(list(range(nMin, nMax, pas)), tempsNormal, label="Dijkstra")
    plt.plot(list(range(nMin, nMax, pas)), tempsRapide, label="Dijkstra with heap")

    plt.xlabel("number of vertices")
    plt.ylabel("execution time (s)")
    plt.legend()
    plt.show()






def exemple():
    n_range = 2**np.arange(2, 13)
    t = np.empty(n_range.size)
    for i, n in enumerate(n_range):
        a = np.random.randn(n, n)
        b  = np.random.randn(n, n)
        t0 = process_time() # début chronométrage
        np.dot(a, b) # Code à chronométrer
        t1 = process_time() # fin chronométrage
        t[i] = t1 - t0

    # print("Temps pour multiplier 2 matrices {}x{}: {:.6f}s".format(n, n, t[i]))

    plt.plot(n_range, n_range, label="temp")
    plt.plot(n_range, 2 * n_range, label="2* temp")

    plt.xlabel("taille $n$")
    plt.ylabel("temps (s)")
    plt.legend()
    # plt.xscale("log")
    # plt.yscale("log")
    plt.grid(True)
    plt.show()



def dijkstra_test_speed_edges(edgesMin:int, edgesMax:int, nbrNodes: int, pas:int = 1) -> None:

    temps = []

    for nbreEdges in range(edgesMin,edgesMax, pas):
        graph = generate_random_graph(nbrNodes, nbreEdges)
        t0 = process_time() # début chronométrage
        graph.dijkstra(0)
        t1 = process_time() # fin chronométrage
        temps.append(t1 - t0)
    print(temps)
    plt.plot(list(range(edgesMin, edgesMax, pas)), temps, label="Dijkstra")

    plt.xlabel("number of vertices")
    plt.ylabel("execution time (s)")
    plt.legend()
    plt.show()


def statistic(nMin:int, nMax:int, alpha:float, pas:int = 1, nbreGrapheTest:int = 10):
    tempsMin:List[float] = []
    tempsMax:List[float] = []
    tempsMoyen:List[float] = []
    tempsMedian:List[float] = []

    print("Starting dijkstra speed statistics")

    for nbreSommets in range(nMin,nMax, pas):
        results = []
        print("    graphs with " + str(nbreSommets) + " vertices... " + str(round(((nbreSommets - nMin)/ ( (nMax - nMin)) ) * 100, 2)) + " %")
        for i in range(nbreGrapheTest):
            print("        calculing graphe number " + str(i) + "... ")

            graph = generate_random_graph(nbreSommets, math.floor(alpha * nbreSommets * nbreSommets))
            vertices = list(graph.vertices)
            vertexFrom = vertices[rand.randrange(len(vertices))]
            vertexTo = vertices[rand.randrange(len(vertices))]

            t0 = process_time() # début chronométrage
            graph.dijkstraSommet(vertexFrom, vertexTo)
            t1 = process_time() # fin chronométrage
            results.append(t1 - t0)

        results.sort()
        mini = math.inf
        maxi = 0
        for el in results:
            if(el > maxi):
                maxi = el
            if(el < mini):
                mini = el
        tempsMin.append(mini)
        tempsMax.append(maxi)
        tempsMoyen.append(sum(results)/len(results))
        tempsMedian.append(results[int((len(results) - 1)/2)] if len(results) % 2 == 1 else (results[int(len(results)/2)] + results[int(len(results)/2 - 1)])/2)

    plt.plot(list(range(nMin, nMax, pas)), tempsMin, label="minimal value")
    plt.plot(list(range(nMin, nMax, pas)), tempsMax, label="maximal value")
    plt.plot(list(range(nMin, nMax, pas)), tempsMoyen, label="average value")
    plt.plot(list(range(nMin, nMax, pas)), tempsMedian, label="median value")

    plt.xlabel("number of vertices")
    plt.ylabel("execution time (s)")
    plt.legend()
    plt.show()


def dijkstra_with_networkxx(nMin:int, nMax:int, alpha:float, pas:int = 1, nbreGrapheTest:int = 10):
    tempsMin:List[float] = []
    tempsMax:List[float] = []
    tempsMoyen:List[float] = []
    tempsMedian:List[float] = []

    print("Starting dijkstra speed statistics")

    for nbreSommets in range(nMin,nMax, pas):
        results = []
        print("    graphs with " + str(nbreSommets) + " vertices... " + str(round(((nbreSommets - nMin)/ ( (nMax - nMin)) ) * 100, 2)) + " %")
        for i in range(nbreGrapheTest):
            print("        calculing graphe number " + str(i) + "... ")

            graph = generate_random_graph(nbreSommets, math.floor(alpha * nbreSommets * nbreSommets)).to_networkx()
            vertices = list(graph.nodes)
            vertexFrom = vertices[rand.randrange(len(vertices))]
            vertexTo = vertices[rand.randrange(len(vertices))]

            t0 = process_time() # début chronométrage
            nx.shortest_path(graph,source=vertexFrom,target=vertexTo, weight='weight')
            t1 = process_time() # fin chronométrage
            results.append(t1 - t0)

        results.sort()
        mini = math.inf
        maxi = 0
        for el in results:
            if(el > maxi):
                maxi = el
            if(el < mini):
                mini = el
        tempsMin.append(mini)
        tempsMax.append(maxi)
        tempsMoyen.append(sum(results)/len(results))
        tempsMedian.append(results[int((len(results) - 1)/2)] if len(results) % 2 == 1 else (results[int(len(results)/2)] + results[int(len(results)/2 - 1)])/2)

    plt.plot(list(range(nMin, nMax, pas)), tempsMin, label="minimal value")
    plt.plot(list(range(nMin, nMax, pas)), tempsMax, label="maximal value")
    plt.plot(list(range(nMin, nMax, pas)), tempsMoyen, label="average value")
    plt.plot(list(range(nMin, nMax, pas)), tempsMedian, label="median value")

    plt.xlabel("number of vertices")
    plt.ylabel("execution time (s)")
    plt.legend()
    plt.show()


def dijkstra_comparaisons(nMin:int, nMax:int, alpha:float, pas:int = 1) -> None:
    tempsNormal = []
    tempsRapide = []
    tempsNetworkxx = []
    print("Starting dijkstra test speed")
    for nbreSommets in range(nMin,nMax, pas):
        print("    calculing for " + str(nbreSommets) + " vertices... " + str(round(((nbreSommets - nMin)/ ( (nMax - nMin)) ) * 100, 2)) + " %")
        graph = generate_random_graph(nbreSommets, math.floor(alpha * nbreSommets * nbreSommets))

        t0 = process_time() # début chronométrage
        graph.dijkstra(0)
        t1 = process_time() # fin chronométrage
        tempsNormal.append(t1 - t0)

        t0 = process_time() # début chronométrage
        graph.dijkstraTas(0)
        t1 = process_time() # fin chronométrage
        tempsRapide.append(t1 - t0)

        gNetw = graph.to_networkx()
        t0 = process_time() # début chronométrage
        nx.single_source_dijkstra_path(gNetw,0)
        t1 = process_time() # fin chronométrage
        tempsNetworkxx.append(t1 - t0)



    plt.plot(list(range(nMin, nMax, pas)), tempsNormal, label="Dijkstra")
    plt.plot(list(range(nMin, nMax, pas)), tempsRapide, label="Dijkstra with heap")
    plt.plot(list(range(nMin, nMax, pas)), tempsNetworkxx, label="Dijkstra with Networkxx")

    plt.xlabel("number of vertices")
    plt.ylabel("execution time (s)")
    plt.legend()
    plt.show()


# dijkstra_test_speed(1, 2500, 0.4, 100)
# statistic(1, 2500, 0.4, 100)
# exemple()

# dijkstra_with_networkxx(1, 2500, 0.4, 100)
dijkstra_comparaisons(1, 2500, 0.4, 100)
