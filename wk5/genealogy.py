# Name: Baasil Siddiqui
# Student Number: 23895849

class qNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.len = 0
        self.head = None
        self.tail = None

    def enque(self, value):
        self.len += 1
        node = qNode(value)

        if self.tail is None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = node

    def pop(self):
        if self.len == 0:
            raise KeyError("queue is empty")

        self.len -= 1
        ret = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return ret

    def __len__(self):
        return self.len


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, child_node):
        self.children.append(child_node)


class Genealogy:
    """The genealogy and succession order for Envoy of the Kiktil."""

    def __init__(self, originator_name):
        """Constructs an initial genealogy containing no individuals other than
        the Originator.

        Args:
            originator_name: The name of the Originator of the Kiktil species.
        """
        self.root = Node(originator_name)
        self.nodes = {originator_name: self.root}

    def add_child(self, parent_name, child_name):
        """Adds a new child belonging to a given parent.

        You may assume the parent has previously been added as the child of
        another individual, and that no individual named `child_name` exists.

        Target Complexity: O(1) expected.

        Args:
            parent_name: The name of the parent individual.
            child_name: The name of their new child.
        """
        if parent_name not in self.nodes:
            raise ValueError(f"parent node '{parent_name}' not found")

        child_node = Node(child_name)
        self.nodes[child_name] = child_node
        self.nodes[parent_name].addChild(child_node)

    def get_primogeniture_order(self):
        """Returns the primogeniture succession order for Envoy of the Kiktil.

        By primogeniture, succession flows from parent to eldest child, only
        moving to the next youngest sibling after all their elder sibling's
        descendants.

        Target Complexity: O(N), where N is how many indivduals have been added.

        Returns:
            A list of the names of individuals in primogeniture succession order
            starting with the Originator.
        """
        list = []
        self.primo_dfs(self.root, list)
        return list

    def primo_dfs(self, root, list):
        list.append(root.name)

        for child in root.children:
            self.primo_dfs(child, list)

    def get_seniority_order(self):
        """Returns the seniority succession order for Envoy of the Kiktil.

        Seniority order prioritizes proximity to the Originator, only moving on
        to a younger generation after every individual in the previous
        generations. Within a generation, older siblings come before younger,
        and cousins are prioritized by oldest different ancestor.

        Target Complexity: O(N), where N is how many indivduals have been added.

        Returns:
            A list of the names of individuals in seniority succession order
            starting with the Originator.
        """
        list = []

        q = Queue()
        q.enque(self.root)

        while len(q) != 0:
            current = q.pop()

            list.append(current.name)

            for child in current.children:
                q.enque(child)

        return list

    def get_cousin_dist(self, lhs_name, rhs_name):
        """Determine the degree and removal of two cousins.

        The order of an individual relative to an ancestor is the number of
        generations separating them. So a child is order 0, a grandchild is
        order 1, and so on. For consistency, an individual has order -1 to
        themself.
        Consider the orders of two individuals relative to their most recent
        shared ancestor.
        The degree of the cousin relation of these individuals is the lesser of
        their orders.
        The removal of the cousin relation is the difference in their orders.

        Target Complexity: O(N), where N is how many indivduals have been added.

        Args:
            lhs_name: The name of one cousin.
            rhs_name: The name of the other cousin.

        Returns:
            A pair `(degree, removal)` of the degree and removal of the cousin
            relation between the specified individuals.
        """
        lhs_dist, rhs_dist = self.get_dist(self.root, lhs_name, rhs_name, -1)

        return (min(lhs_dist, rhs_dist), abs(lhs_dist - rhs_dist))

    def get_dist(self, root: Node, lhs_name: str, rhs_name: str, counter: int) -> list[int]:
        dist: list[int] = [-1, -1]
        found: int = 0

        if (root.name == lhs_name):
            dist[0] = counter
            found += 1
        if (root.name == rhs_name):
            dist[1] = counter
            found += 1

        if (dist[0] != -1 and dist[1] != -1):
            return [-1, -1]

        for child in root.children:
            [lhs_cnt, rhs_cnt] = self.get_dist(child, lhs_name, rhs_name, counter + 1)

            if (dist[0] == -1):
                dist[0] = lhs_cnt
            if (dist[1] == -1):
                dist[1] = rhs_cnt

            if (lhs_cnt != -1 or rhs_cnt != -1):
                found += 1

        if found > 1:
            return [dist[0] - counter - 1, dist[1] - counter - 1]

        return dist
