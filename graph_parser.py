__author__ = 'Antonin et Vico'

from typing import Tuple, List, Set

__Filename = 'graph_parser'
__Creationdate__ = '23/03/2021'

from graph import DirectedGraph


def read_file(file_name: str) -> List[Tuple[str, str]]:
    subreddit_file = open(file_name)
    lines = subreddit_file.readlines()[1:]
    subreddit_file.close()
    subreddit_links_list = []

    for i in range(len(lines)):
        split = lines[i].split('\t')
        subreddit_links_list.append((split[0], split[1]))
    return subreddit_links_list


def create_graph_from_edges(links_list:Set[Tuple[str, str]]) -> DirectedGraph:
    graph = DirectedGraph()
    for sub1, sub2 in links_list:
        if sub1 not in graph.edges:
            graph.add_vertex(sub1)
        if sub2 not in graph.edges:
            graph.add_vertex(sub2)
        graph.add_edge(sub1, sub2, 1)
    return graph


def create_graph(file_name:str) -> DirectedGraph:
    # Creates graph with no duplicate edge
    return create_graph_from_edges(set(read_file(file_name)))