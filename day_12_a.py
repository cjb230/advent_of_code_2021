#  https://adventofcode.com/2021/day/12
from dataclasses import dataclass

SOURCE_FILE = 'day_12_input.txt'


@dataclass
class Edge:
    u: str
    v: str

    def reversed(self) -> Edge:
        return Edge(self.v, self.u)

    def __str__(self) -> str:
        return f"{self.u} -> {self.v}"


@dataclass
class Vertex:
    name: str
    size: str


class Graph:
    def __init__(self, vertices: list[Vertex] = []) -> None:
        self._vertices: list[Vertex] = vertices
        self._edges: list[list[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)

    @property
    def edge_count(self) -> int:
        return sum(map(len, self._edges))

    def add_vertex(self, vertex: Vertex) -> int:
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count - 1

    def add_edge(self, edge: Edge) -> None:
        self._edges







def main():
    # read the file
    with open(SOURCE_FILE) as f:
        edge_strings = f.read().splitlines()

    print(edge_strings)


if __name__ == "__main__":
    main()
