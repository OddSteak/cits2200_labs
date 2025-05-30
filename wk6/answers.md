# CITS2200 Lab 6: Tranes and Planes, Security Routing

Name: Baasil Siddiqui
Student Number: 23895849


## Question 1 (3 marks)
Implement your solution by filling out the method stub in `trains_planes.py`.
Your implementation must pass the tests given in `test_trains_planes.py`, which can be invoked by running `python -m unittest test_trains_planes`.

See `trains_planes.py`.


## Question 2 (1 mark)
Give an argument for the correctness of your `trains_planes()` function.

My solution correctly identifies replaceable flights using a graph-based approach similar to Kruskal's algorithm for finding connected components.

The core idea is to track which cities are connected by rail at any given time:

I process all transportation events in chronological order, handling trains before planes on the same date
For each train connection, I update my data structure to record that the two cities are now connected, either directly or transitively
When processing a flight, I check if there's already a path between its departure and arrival cities using the current rail network
My implementation uses a modified forest structure where each city belongs to a connected component. When a new rail connection is added between cities from different components, I merge those components - this is exactly what Kruskal's algorithm does when building a minimum spanning tree.

This approach correctly handles transitive connections: if trains connect A to B and B to C, my algorithm will recognize that A and C are in the same connected component, even though there's no direct rail line between them.

By maintaining these connected components as the rail network evolves over time, my solution accurately identifies all flights that can be replaced by rail journeys, no matter how indirect the route might be.


## Question 3 (1 mark)
Give an argument for the complexity of your `trains_planes()` function.

My solution achieves the target complexity of O(N log N) where N = len(trains) + len(planes):

- Creating transport events: O(N) time to convert input lists to Transport objects

- Sorting events: O(N log N) using Python's timsort algorithm

- Processing events: O(N) total operations where each operation is:

    - For trains: Creating nodes (O(1)) and merging sets O(N) where N is the length of the smaller set
    - For planes: Checking if cities are connected (O(1))
    - The merging of sets is efficient because:

I always merge the smaller set into the larger set
This ensures each node changes its set at most log N times
Total time for all merges is O(N log N)
All other operations (dictionary lookups, list operations) are O(1), making the overall complexity O(N log N), which meets the target complexity requirement.

## Question 1 (3 marks)
Implement your solution by filling out the method stub in `security_routing.py`.
Your implementation must pass the tests given in `test_security_routing.py`, which can be invoked by running `python -m unittest test_security_routing`.

See `security_routing.py`.


## Question 2 (1 mark)
Give an argument for the correctness of your `security_route()` function.

YOUR ANSWER HERE


## Question 3 (1 mark)
Give an argument for the complexity of your `security_route()` function.

YOUR ANSWER HERE
