# Name: Baasil Siddiqui
# Student Number: 23895849

from __future__ import annotations
from datetime import date


class GraphNode:
    def __init__(self, city: str):
        self.city = city
        self.edges: list[GraphEdge] = []

    def addEdge(self, node: GraphNode, date: date) -> None:
        """add an edge to the node."""
        self.edges.append(GraphEdge(node, date))

    def incident_edges(self, date: date | None) -> list[GraphEdge]:
        """return the list of edges incident to this node before a specific date."""
        if not date:
            return self.edges
        return [edge for edge in self.edges if edge.date <= date]


class GraphEdge:
    def __init__(self, node: GraphNode, date: date):
        self.date = date
        self.node = node


class Graph:
    def __init__(self):
        self.nodes: list[GraphNode] = []

    def addNode(self, city: str) -> GraphNode:
        """add a node to the graph with the given city and date."""
        node: GraphNode = GraphNode(city)
        self.nodes.append(node)
        return node

    def getNodes(self) -> list[GraphNode]:
        """return the list of nodes in the graph."""
        return self.nodes

    def getCity(self, city: str) -> GraphNode | None:
        """return the node with the given city, or None if it doesn't exist."""
        for node in self.nodes:
            if node.city == city:
                return node
        return None


def trains_planes(
    trains: list[tuple[date, str, str]], planes: list[tuple[str, date, str, str]]
) -> list[tuple[str, date, str, str]]:
    """Find what flights can be replaced with a rail journey.

    Initially, there are no rail connections between cities. As rail connections
    become available, we are interested in knowing what flights can be replaced
    by a rail journey, no matter how indirect the route. All rail connections
    are bidirectional.

    Target Complexity: O(N lg N) in the size of the input (trains + planes).

    Args:
        trains: A list of `(date, lcity, rcity)` tuples specifying that a rail
            connection between `lcity` and `rcity` became available on `date`.
        planes: A list of `(code, date, depart, arrive)` tuples specifying that
            there is a flight scheduled from `depart` to `arrive` on `date` with
            flight number `code`.

    Returns:
        A list of flights that could be replaced by a train journey.
    """
    def dfs(
        srcNode: GraphNode, destNode: GraphNode, visited: set[GraphNode], date: date
    ) -> bool:
        """Perform a depth-first search to find a path from srcNode to destNode."""
        if srcNode == destNode:
            return True
        visited.add(srcNode)

        for edge in srcNode.incident_edges(date):
            if edge.node not in visited and dfs(edge.node, destNode, visited, date):
                return True

        return False

    g: Graph = Graph()
    replaceable: list[tuple[str, date, str, str]] = []

    for train in trains:
        date, city1, city2 = train
        cityNodes: list[GraphNode] = []

        for city in (city1, city2):
            cityNode = g.getCity(city)
            # add city if it doesn't exist in graph
            if not cityNode:
                cityNode = g.addNode(city)
            cityNodes.append(cityNode)

        for i in range(2):
            cityNodes[i].addEdge(cityNodes[1 - i], date)

    for plane in planes:
        _, date, depart, arrive = plane
        departNode: GraphNode | None = g.getCity(depart)
        arriveNode: GraphNode | None = g.getCity(arrive)

        if not departNode or not arriveNode:
            continue

        if dfs(departNode, arriveNode, set(), date):
            replaceable.append(plane)

    return replaceable


