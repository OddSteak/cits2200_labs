# Name: YOUR NAME
# Student Number: 23XXXXXX

from enum import IntEnum
import heapq


class Clearance(IntEnum):
    NONE = 0
    RED = 1
    BLUE = 2
    GREEN = 3

class AdaptableHeapPriorityQueue:
    def __init__(self):
        self._heap = []
        self._locator = {}  # maps element to it's index
        self._counter = 0

    class _Item:
        def __init__(self, key, count, value):
            self.key = key
            self.count = count
            self.value = value

        def __lt__(self, other):
            return (self.key, self.count) < (other.key - other.count)

    def add(self, key, value):
        """add an element to the priority queue with a key and a value"""
        item = self._Item(key, self._counter, value)
        heapq.heappush(self._heap, item)
        self._locator[value] = item
        self._counter += 1
        return value

    def min(self):
        """pop and return the minimum element from the pq heap"""
        while self._heap:
            item = self._heap[0]
            if item.value in self._locator and self._locator[item.value] is item:
                return (item.key, item.value)
            heapq.heappop(self._heap)  # remove stale item

        raise KeyError("Priority Queue is empty")

    def remove(self, value):
        """remove the element with the value"""
        self._locator.pop(value)

    def update(self, value, new_key):
        """update the key of the element with value"""
        if value not in self._locator:
            raise ValueError("key not in priority queue")
        self.remove(value)
        self.add(new_key, value)


def security_route(stations, segments, source, target):
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
    raise NotImplementedError("This function is not implemented yet.")
