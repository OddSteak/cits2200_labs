from __future__ import annotations
import heapq
from enum import IntEnum


class Clearance(IntEnum):
    NONE = 0
    RED = 1
    BLUE = 2
    GREEN = 3


class Edge:
    def __init__(self, station: int, time: int, clearance: Clearance) -> None:
        self.station = station
        self.time = time
        self.clearance = clearance


class Node:
    def __init__(self, time: int | float, count: int, station: int, clearance: Clearance) -> None:
        self.station = station
        self.time = time
        self.clearance = clearance
        self.count = count
        self.edges: list[Edge] = []

    def __lt__(self, other: Node) -> bool:
        """Compare items based on their key and count."""
        return (self.time, -self.clearance, self.count) < (
            other.time,
            -other.clearance,
            other.count,
        )

class Graph:
    """A graph representation with adjacency list."""
    def __init__(self):
        self.adj: list[list[Edge]] = []
        self._counter: int = 0

    def addNode(self, station: int):
        """add a node to the graph."""
        if station != len(self.adj):
            raise ValueError(f"Station {station} does not match the current number of nodes {len(self.adj)}")
        self.adj.append([])

    def addEdge(self, u: int, v: int, time: int, clearance: Clearance):
        """add an edge from u to v with time and clearance."""
        if v >= len(self.adj) or u >= len(self.adj):
            raise ValueError(f"{u} or {v} station not in graph")

        if v not in self.adj[u] or u not in self.adj[v]:
            self.adj[u].append(Edge(v, time, clearance))
            self.adj[v].append(Edge(u, time, clearance))

    def incidentEdges(self, station: int, clearance: Clearance) -> list[Edge]:
        """Return the list of incident edges from station below clearance."""
        if station >= len(self.adj):
            raise ValueError(f"{station} not in graph")

        return [edge for edge in self.adj[station] if edge.clearance <= clearance]


class AdaptableHeapPriorityQueue:
    def __init__(self) -> None:
        self._heap: list[Node] = []
        self._locator: dict[int, dict[Clearance, Node]] = {}  # maps element to it's index
        self._counter: int = 0

    def add(self, time: int | float, station: int, clearance: Clearance) -> int:
        """add an element to the priority queue with a key, a value, and clearance"""
        item: Node = Node(time, self._counter, station, clearance)
        heapq.heappush(self._heap, item)

        if station not in self._locator:
            self._locator[station] = {}

        self._locator[station][clearance] = item
        self._counter += 1
        return station

    def min(self) -> Node:
        """pop and return the minimum element from the pq heap"""
        if len(self._heap) == 0:
            raise KeyError("Priority Queue is empty")

        item: Node = self._heap[0]
        heapq.heappop(self._heap)
        self._locator[item.station].pop(item.clearance)
        return item

    def getItem(self, value: int, clearance: Clearance) -> Node:
        """get the item with the value"""
        if value not in self._locator:
            raise KeyError("value not in priority queue")

        return self._locator[value][clearance]

    def update(self, station: int, clearance: Clearance, new_time: int) -> None:
        """update the key of the element with value"""
        if station not in self._locator:
            raise KeyError(f"key {station} not in priority queue")

        if clearance not in self._locator[station]:
            self.add(new_time, station, clearance)
        else:
            node = self.getItem(station, clearance)
            node.time = new_time

    def restoreHeap(self) -> None:
        """restore heap property after an update"""
        heapq.heapify(self._heap)

    def isEmpty(self) -> bool:
        """Check if the priority queue is empty."""
        return len(self._heap) == 0
