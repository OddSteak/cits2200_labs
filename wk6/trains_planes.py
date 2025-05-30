# Name: Baasil Siddiqui
# Student Number: 23895849

from __future__ import annotations
from datetime import date


class Transport:
    def __init__(self, city1: str, city2: str, date: date):
        self.city1 = city1
        self.city2 = city2
        self.date = date


class Train(Transport):
    def __init__(self, city1: str, city2: str, date: date):
        super().__init__(city1, city2, date)


class Plane(Transport):
    def __init__(self, city1, city2, date, code):
        super().__init__(city1, city2, date)
        self.code = code


class GraphNode:
    def __init__(self, city: str, set: list[GraphNode]):
        self.city = city
        self.set = set


class Partition:
    def make_group(self, city: str) -> GraphNode:
        """make a new group with a single city"""
        new_set: list[GraphNode] = []
        node: GraphNode = GraphNode(city, new_set)
        new_set.append(node)
        return node

    def find(self, node: GraphNode) -> list[GraphNode]:
        """find the representative of the group that contains the node"""
        return node.set

    def union(self, set1: list[GraphNode], set2: list[GraphNode]) -> list[GraphNode]:
        """merge two groups into one"""
        smaller: list[GraphNode] = set1
        larger: list[GraphNode] = set2
        if len(set2) < len(set1):
            smaller = set2
            larger = set1

        for node in smaller:
            node.set = larger
            larger.append(node)

        return larger


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
    # Create a list of all transport events, with trains and planes
    list: list[Transport] = []
    replaceable: list[tuple[str, date, str, str]] = []

    for train in trains:
        date, city1, city2 = train
        list.append(Train(city1, city2, date))

    for plane in planes:
        code, date, city1, city2 = plane
        list.append(Plane(city1, city2, date, code))

    # Sort the list by date, with trains before planes on the same date
    list.sort(key=lambda x: (x.date, 0 if isinstance(x, Train) else 1))

    positions: dict[str, GraphNode] = {}  # map city to it's partition entry
    forest: Partition = Partition()  # a forest of disjoint sets

    for event in list:
        if isinstance(event, Train):
            for city in (event.city1, event.city2):
                # If the city is not in positions, create a new group for it and add it to positions
                if city not in positions:
                    positions[city] = forest.make_group(city)

            # Find the partitions of the two cities
            a: list[GraphNode] = forest.find(positions[event.city1])
            b: list[GraphNode] = forest.find(positions[event.city2])

            # If the cities are not in the same partition, union them
            if a != b:
                forest.union(a, b)

        elif isinstance(event, Plane):
            # If either city is not in positions, skip this event
            if event.city1 not in positions or event.city2 not in positions:
                continue

            # If both cities are in the same partition, add to replaceable
            if forest.find(positions[event.city1]) == forest.find(
                positions[event.city2]
            ):
                replaceable.append((event.code, event.date, event.city1, event.city2))

    return replaceable
