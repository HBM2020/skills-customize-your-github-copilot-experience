"""Starter code: Graph Route Optimization.

Complete each TODO according to the assignment README.
"""

from heapq import heappop, heappush
from itertools import permutations


def build_graph(edges):
    """Build an undirected weighted graph from an edge list.

    Expected output format:
    {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4)],
        ...
    }
    """
    graph = {}

    # TODO 1:
    # - Validate positive integer weights
    # - Ignore self-loops
    # - Add edges in both directions

    return graph


def dijkstra_shortest_path(graph, start, end):
    """Return (distance, path) for the shortest route from start to end.

    If there is no route, return (float("inf"), []).
    """
    # TODO 2:
    # Implement Dijkstra with a priority queue.
    # Keep track of both minimum distance and predecessor nodes.

    return float("inf"), []


def merge_paths(path_a, path_b):
    """Merge two paths, avoiding duplicate join nodes.

    Example:
    ["A", "B", "C"] + ["C", "D"] -> ["A", "B", "C", "D"]
    """
    if not path_a:
        return path_b
    if not path_b:
        return path_a
    if path_a[-1] == path_b[0]:
        return path_a + path_b[1:]
    return path_a + path_b


def best_route_with_checkpoints(graph, start, end, checkpoints):
    """Return (best_distance, best_path) visiting all checkpoints once.

    Suggested strategy:
    1) Generate all permutations of checkpoints.
    2) For each order, create route segments: start -> cp1 -> ... -> end.
    3) Use Dijkstra for each segment and combine partial paths.
    4) Keep the route with the lowest total distance.

    Complexity note:
    - If k = len(checkpoints), there are k! orders.
    - Each order runs multiple shortest-path computations.
    """
    best_distance = float("inf")
    best_path = []

    # TODO 3:
    # Implement the checkpoint-order search and compute the global best route.

    return best_distance, best_path


if __name__ == "__main__":
    edges = [
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "C", 1),
        ("B", "D", 5),
        ("C", "D", 8),
        ("C", "E", 10),
        ("D", "E", 2),
        ("D", "F", 6),
        ("E", "F", 3),
    ]

    start = "A"
    end = "F"
    checkpoints = ["D", "E"]

    graph = build_graph(edges)
    distance, path = best_route_with_checkpoints(graph, start, end, checkpoints)

    print("Best distance:", distance)
    print("Best path:", " -> ".join(path) if path else "No valid route")
