# 📘 Assignment: Graph Route Optimization

## 🎯 Objective

Practice advanced algorithmic thinking with graphs by modeling routes, finding shortest paths, and solving a constrained optimization problem. You will implement efficient solutions and justify complexity trade-offs.

## 📝 Tasks

### 🛠️ Build the Graph Model

#### Descrição
Implement a function that converts a list of weighted edges into an adjacency-list graph structure.

#### Requisitos
O programa concluído deve:

- Implement `build_graph(edges)` returning `dict[str, list[tuple[str, int]]]`
- Ensure each edge is added in both directions (undirected graph)
- Ignore self-loops where source and destination are equal
- Validate that all weights are positive integers


### 🛠️ Implement Shortest Path with Dijkstra

#### Descrição
Implement Dijkstra's algorithm to compute the shortest route between two nodes in a weighted graph.

#### Requisitos
O programa concluído deve:

- Implement `dijkstra_shortest_path(graph, start, end)`
- Return both total distance and the path as a node list
- Return `(float("inf"), [])` when there is no valid path
- Use a priority queue (`heapq`) for efficient exploration


### 🛠️ Solve Route Optimization with Checkpoints

#### Descrição
Find the best route from a start node to an end node while visiting all required checkpoints exactly once (in the best order).

#### Requisitos
O programa concluído deve:

- Implement `best_route_with_checkpoints(graph, start, end, checkpoints)`
- Try all checkpoint orders and combine shortest-path segments
- Return the global best route and total distance
- Print time complexity notes for your strategy in code comments
- Use this input to validate your solution:

```python
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
```
