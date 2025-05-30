# Name: Baasil Siddiqui
# Student Number: 23895849

from typing import Optional
from adaptable_heap import AdaptableHeapPriorityQueue, Clearance, Node, Edge, Graph


def security_route(
    stations: list[Clearance],
    segments: list[tuple[int, int, int, Clearance]],
    source: int,
    target: int,
) -> Optional[int]:
    """Finds the fastest route from source station to target station.

    You start with no security clearance.
    When at a security station, you may choose to set your clearance to the same
    as that of the station.
    Each segment gives how long it takes to get from one station to another, and
    what clearance is required to be able to take that segment.

    Target Complexity: O(N lg N) in the size of the input (stations + segments).

    Args:
        stations: A list of what clearance is available at each station, or
            `NONE` if that station can not grant any clearance.
        segments: A list of `(u, v, t, c)` tuples, each representing a segment
            from `stations[u]` to `stations[v]` taking time `t` and requiring
            clearance `c` (`c` may be `NONE` if no clearance is required).
        source: The index of the station from which we start.
        target: The index of the station we are trying to reach.

    Returns:
        The minimum length of time required to get from `source` to `target`, or
        `None` if no route exists.
    """
    d: dict[
        int, dict[Clearance, int | float]
    ] = {}  # d[v][clearance] is upper bound from s to v
    cloud: dict[int, dict[Clearance, int | float]] = {}  # map v to it's d[v] value
    g: Graph = Graph()
    pq: AdaptableHeapPriorityQueue = AdaptableHeapPriorityQueue()

    for v in range(len(stations)):
        d[v] = {}

        if v == source:
            d[v][stations[v]] = 0
        else:
            d[v][stations[v]] = float("inf")

        pq.add(d[v][stations[v]], v, stations[v])
        g.addNode(v)

    [g.addEdge(u, v, t, cs) for u, v, t, cs in segments]

    while not pq.isEmpty():
        item: Node = pq.min()
        if item.station not in cloud:
            cloud[item.station] = {}

        cloud[item.station][item.clearance] = d[item.station][item.clearance]
        time, clearance = cloud[item.station][item.clearance], item.clearance
        print(f"edges of {item.station}, {clearance}==========================")

        if item.station == target:
            return int(time)

        for e in g.incidentEdges(item.station, clearance):
            new_d: tuple[float | int, Clearance] = (
                time + e.time,
                max(clearance, stations[e.station]),
            )

            if new_d[0] < d[e.station].get(new_d[1], float("inf")):
                print(f"updating {e.station} to t: {new_d[0]} c: {new_d[1]}")
                d[e.station][new_d[1]] = new_d[0]
                pq.update(e.station, new_d[1], int(new_d[0]))

        pq.restoreHeap()

    return None
