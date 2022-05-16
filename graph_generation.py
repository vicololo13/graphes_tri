__author__ = 'Antonin et Vico'


__Filename = 'graph_generation'
__Creationdate__ = '09/03/2021'

from PROJET.graph import *
import random as rand

def generate_random_graph(nombreSommets:int, nombreArrete:int, directed:bool = False) -> 'DirectedGraph':
    graphe = DirectedGraph() if directed else UndirectedGraph()

    if(nombreSommets <= 0):
        return graphe

    for i in range(nombreSommets):
        graphe.add_vertex(i)

    if(nombreArrete < nombreSommets - 1):
        return graphe


    nombreArrete = min(nombreArrete, nombreSommets * (nombreSommets - 1))

    premierSommet = rand.randrange(nombreSommets)
    dejaReliee = {premierSommet}

    pasEncoreRelie = set(range(nombreSommets))
    pasEncoreRelie.remove(premierSommet)

    for i in range(nombreSommets - 1):
        aRelier1 = rand.choice(list(pasEncoreRelie))
        aRelier2 = rand.choice(list(dejaReliee))

        graphe.add_edge(aRelier1, aRelier2, rand.random())

        pasEncoreRelie.remove(aRelier1)
        dejaReliee.add((aRelier1))


    nombreArreteRestante = nombreArrete - (nombreSommets-1) * (1 if directed else 2)

    while(nombreArreteRestante > 0):
        aRelier1 = 0
        aRelier2 = 0

        while(aRelier2 == aRelier1 or graphe.edge_exist(aRelier1, aRelier2)):
            aRelier1 = rand.randrange(nombreSommets)
            aRelier2 = rand.randrange(nombreSommets)

        graphe.add_edge(aRelier1, aRelier2, rand.random())

        nombreArreteRestante -= 1 if directed else 2
    return graphe



def generate_random_community_graph(nNodesPerCommunity: List[int], p_intra:float, p_inter:float) -> UndirectedGraph:
    graphe = UndirectedGraph()
    rng = rand.Random()
    numberOfVertex = 0
    for nodesNbm in  nNodesPerCommunity:
        for i in range(nodesNbm):
            graphe.add_vertex(numberOfVertex)
            numberOfVertex += 1


    currentCommunityOffset=0
    currentCommunity = 0
    for vertex in range(numberOfVertex):
        if(vertex >= nNodesPerCommunity[currentCommunity] + currentCommunityOffset):
            currentCommunityOffset = nNodesPerCommunity[currentCommunity] + currentCommunityOffset
            currentCommunity += 1


        for vertex2 in range(numberOfVertex):
            if(graphe.edge_exist(vertex, vertex2) or vertex == vertex2):
                continue

            isInCommunity = currentCommunityOffset <= vertex2 < currentCommunityOffset + nNodesPerCommunity[currentCommunity]


            prob = rng.random()
            if(isInCommunity and prob < p_intra):
                graphe.add_edge(vertex, vertex2, rng.random())
            if(not isInCommunity and prob < p_inter):
                graphe.add_edge(vertex, vertex2, rng.random())

    return graphe


def generate_random_community_graph_compteur(nNodesPerCommunity: List[int], p_intra:float, p_inter:float) -> Tuple[
    UndirectedGraph, int, int]:
    graphe = UndirectedGraph()
    rng = rand.Random()
    numberOfVertex = 0
    compteur_intra, compteur_inter = 0, 0
    for nodesNbm in  nNodesPerCommunity:
        for i in range(nodesNbm):
            graphe.add_vertex(numberOfVertex)
            numberOfVertex += 1


    currentCommunityOffset=0
    currentCommunity = 0
    for vertex in range(numberOfVertex):
        if(vertex >= nNodesPerCommunity[currentCommunity] + currentCommunityOffset):
            currentCommunityOffset = nNodesPerCommunity[currentCommunity] + currentCommunityOffset
            currentCommunity += 1


        for vertex2 in range(numberOfVertex):
            if(graphe.edge_exist(vertex, vertex2) or vertex == vertex2):
                continue

            isInCommunity = currentCommunityOffset <= vertex2 < currentCommunityOffset + nNodesPerCommunity[currentCommunity]


            prob = rng.random()
            if(isInCommunity and prob < p_intra):
                graphe.add_edge(vertex, vertex2, rng.random())
                compteur_intra += 1
            if(not isInCommunity and prob < p_inter):
                graphe.add_edge(vertex, vertex2, rng.random())
                compteur_inter += 1

    return graphe, compteur_intra, compteur_inter


def drawCummunityGraph(graph:UndirectedGraph, inputListe:List[int]):
    listColors = []
    currentColor = 0
    for i in inputListe:
        for j in range(i):
            listColors.append(currentColor)
        currentColor += 1
    graph.draw(listColors)



