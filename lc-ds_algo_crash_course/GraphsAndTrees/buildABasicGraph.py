"""
Building a Basic Graph from Edges asa 2D Array
"""

from collections import defaultdict


def build_graph(edges: list[list[int]], one_dir=True) -> dict[int, int]:
    graph = defaultdict(list)

    for x, y in edges:
        graph[x].append(y)

    return graph
