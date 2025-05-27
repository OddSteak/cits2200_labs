from __future__ import annotations
import heapq
from enum import IntEnum


class Clearance(IntEnum):
    NONE = 0
    RED = 1
    BLUE = 2
    GREEN = 3


class Edge:
    def __init__(self, node: Node, time: int, clearance: Clearance) -> None:
        self.node = node
        self.time = time
        self.clearance = clearance


class Node:
    def __init__(self, key: int | float, count: int, value: int, clearance: Clearance) -> None:
        self.key = key
        self.count = count
        self.value = value
        self.clearance = clearance
        self.edges: list[Edge] = []

    def addEdge(self, node: Node, time: int, clearance: Clearance) -> None:
        """Add an edge to another node."""
        self.edges.append(Edge(node, time, clearance))

    def incidentEdges(self, clearance: Clearance) -> list[Edge]:
        """Return the list lof incident edges."""
        return [edge for edge in self.edges if edge.clearance <= clearance]

    def __lt__(self, other: Node) -> bool:
        """Compare items based on their key and count."""
        return (self.key, -self.clearance, self.count) < (
            other.key,
            -other.clearance,
            other.count,
        )


class AdaptableHeapPriorityQueue:
    def __init__(self) -> None:
        self._heap: list[Node] = []
        self._locator: dict[int, Node] = {}  # maps element to it's index
        self._counter: int = 0

    def add(self, key: int | float, value: int, clearance: Clearance) -> int:
        """add an element to the priority queue with a key, a value, and clearance"""
        item: Node = Node(key, self._counter, value, clearance)
        heapq.heappush(self._heap, item)
        self._locator[value] = item
        self._counter += 1
        return value

    def min(self) -> Node:
        """pop and return the minimum element from the pq heap"""
        while self._heap:
            item: Node = self._heap[0]
            if item.value in self._locator and self._locator[item.value] is item:
                heapq.heappop(self._heap)
                self._locator.pop(item.value)
                return item
            heapq.heappop(self._heap)  # remove stale item

        raise KeyError("Priority Queue is empty")

    def remove(self, value: int) -> None:
        """remove the element with the value"""
        self._locator.pop(value)

    def getItem(self, value: int) -> Node:
        """get the item with the value"""
        if value not in self._locator:
            raise KeyError("value not in priority queue")

        return self._locator[value]

    def update(self, value: int, new_key: int) -> None:
        """update the key of the element with value"""
        if value not in self._locator:
            raise KeyError(f"key {value} not in priority queue")
        node = self.getItem(value)
        node.key = new_key

    def restoreHeap(self) -> None:
        """restore heap property after an update"""
        heapq.heapify(self._heap)

    def isEmpty(self) -> bool:
        """Check if the priority queue is empty."""
        while self._heap:
            item: Node = self._heap[0]
            if item.value in self._locator and self._locator[item.value] is item:
                return False
            heapq.heappop(self._heap)  # remove stale item

        return True
