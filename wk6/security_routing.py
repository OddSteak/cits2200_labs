# Name: Baasil Siddiqui
# Student Number: 23895849

from typing import Optional
from adaptable_heap import AdaptableHeapPriorityQueue, Clearance, Node, Edge


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
    d: dict[int, tuple[int | float, Clearance]] = {}  # d[v] is upper bound from s to v
    cloud: dict[int, tuple[int | float, Clearance]] = {}  # map v to it's d[v] value
    pq: AdaptableHeapPriorityQueue = AdaptableHeapPriorityQueue()

    for v in range(len(stations)):
        if v == source:
            d[v] = (0, stations[v])
        else:
            d[v] = (float("inf"), stations[v])

        pq.add(d[v][0], v, stations[v])

    for segment in segments:
        u, v, t, cs = segment

        node_u: Node = pq.getItem(u)
        node_v: Node = pq.getItem(v)
        node_u.addEdge(node_v, t, cs)
        node_v.addEdge(node_u, t, cs)

    while not pq.isEmpty():
        item: Node = pq.min()
        cloud[item.value] = d[item.value]
        key, clearance = cloud[item.value]
        print(f"edges of {item.value}, {clearance}==========================")

        for e in item.incidentEdges(clearance):
            neighbour: Node = e.node
            new_d: tuple[float | int, Clearance] = (
                key + e.time,
                max(clearance, neighbour.clearance),
            )
            if new_d[0] < d[neighbour.value][0] or new_d[1] > d[neighbour.value][1]:
                d[neighbour.value] = new_d
                if neighbour.value in cloud:
                    print(f"removing {neighbour.value} from cloud with t: {new_d[0]} c: {new_d[1]}")
                    pq.add(int(new_d[0]), neighbour.value, new_d[1])
                    del cloud[neighbour.value]
                else:
                    print(f"updating {neighbour.value} to t: {new_d[0]} c: {new_d[1]}")
                    pq.update(neighbour.value, int(new_d[0]))

        pq.restoreHeap()

    return int(cloud[target][0])
