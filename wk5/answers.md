# CITS2200 Lab 2: Genealogy

Name: Baasil Siddiqui

Student Number: 23895849


## Question 1 (1 mark)
Write a simple description of how you are going to represent the problem as a data structure.
Your description should justify how the representation is going to help you solve the problem within the target complexities.

A tree can be used to represent a gene tree
if we store all the nodes in a hashmap, we can add a new child in constant time
a tree can be traversed in O(N) time so we can find the primogeniture and seniority orders in O(N) time


## Question 2 (1 mark)
Write a simple description of the algorithm you have designed for `get_cousin_dist()`.
Your description should justify the correctness of your algorithm, and make an argument as to its time complexity.

- The tree is traversed recursively starting from the root node (originator)

- counter keeps track of the number of generations from the root to the current node.

- get_dist() returns a pair [lhs_dist, rhs_dist] representing the distances of lhs_name and rhs_name from their MRCA.

- If both individuals are found in different subtrees of a node, that node is their the most recent shared ancestor, and the distances are adjusted accordingly.

- If only one is found, the function bubbles up that partial information until the other is found or the tree is exhausted.

### Correctness

- when both names are found in different subtrees of a node then that node is their most recent shared ancestor

- we subtract counter + 1 from the distance to find the distance relatice to the shared ancestor

- Each recursive call increases the counter by 1, which accurately tracks the number of generations from the root to the current node.

### Time complexity

Each node is visited exactly once Therefore the total work done is proportional to the number of nodes in the tree

In the worst-case scenario, both individuals are at the deepest leaves of two opposite subtrees, but even in that case, the traversal still only touches each node once → O(N).

The time complexity is O(N), where N is the total number of individuals in the family tree


## Question 3 (5 marks)
Implement your design by filling out the method stubs in the `Genealogy` class found in `genealogy.py`.
You are **not** allowed to import any modules.
Your implementation must pass the tests given in `test_genealogy.py`, which can be invoked by running `python -m unittest`.

See `genealogy.py`.


## Question 4 (1 mark)
Give an argument for the correctness and complexity of your `get_primogeniture_order()` function.

Recursive Structure Matches Primogeniture:

- Each individual is visited before their children.

- Children are visited in order — so eldest child and their descendants are fully traversed before moving to the next sibling.

- Each node is visited exactly once, and all nodes reachable from self.root are added to the list.

- Therefore, the result list contains all individuals in the correct succession order.

### Time complexity

- The function primo_dfs() visits every node once.

- At each node, it performs constant-time work: appending the name to the list.

- It also makes recursive calls for each child.

Therefore, the time complexity is O(N)


## Question 5 (1 mark)
Give an argument for the correctness and complexity of your `get_seniority_order()` function.

The algorithm builds the succession list by processing individuals generation by generation. It starts with the Originator, then processes all their children, then all grandchildren, and so on. This ensures that:

- The queue is being used to ensure that older generations are prioritized before younger ones.

- Within the same generation, siblings are added in order (assuming children are stored from eldest to youngest).

- Cousins from older branches appear before those from younger branches, as we move level by level from the root.

This matches the described seniority succession rules.

### Time complexity

Each individual is:

- Added to the queue once,

- Processed once when removed from the queue,

- Their children are added in a single step.

With N individuals, the total work done is O(N).

## Question 6 (1 mark)
Give a brief explanation of the function and purpose of any data structures you implemented.

A tree is a hierarchical data structure made up of nodes, where each node can have zero or more children, but only one parent (except the root, which has none).

The purpose of a tree is to represent relationships with a clear parent-child structure, making it ideal for organizing data such as family trees, file systems, or organizational charts. It enables efficient traversal, search, and hierarchical queries.
