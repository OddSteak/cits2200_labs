class ArrayList:
    """A simple dynamically-sized list.

    Note: Python lists are already dynamically sized, so while implementing this
    class, you may not use any methods that would cause a list or other built-in
    data structure to change size. If you ever need to change the size of a list
    you must instead construct a new list of the desired size and copy across.
    """

    def __init__(self):
        """Constructs an empty ArrayList."""
        self.length = 0
        self.arr = []

    def __len__(self):
        """Returns the number of elements in the ArrayList."""
        return self.length

    def __getitem__(self, index):
        """Returns the item at position `index` in the ArrayList.

        This implements the `xs[i]` notation you will be familiar with from
        lists, but there is no need to support ranges or negative indices.

        Args:
            index: The index of the desired element.

        Returns:
            The element at position `index`.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if (index < 0 or index >= self.length):
            raise IndexError("index", index, "is out of bounds for array length", self.length)

        return self.arr[index]

    def __setitem__(self, index, value):
        """Sets the `index` position element in the ArrayList to be `value`.

        This implements the `xs[i] = x` notation you will be familiar with from
        lists, but there is no need to support ranges or negative indices.

        Args:
            index: The index of the element to modify.
            value: The value to store at the given index.

        Raises:
            IndexError: If the index is out of bounds.
        """
        if (index < 0 or index >= self.length):
            raise IndexError("index", index, "is out of bounds for array length", self.length)

        self.arr[index] = value

    def reserve(self, n):
        """Ensure ArrayList has capacity at least `n`.

        Grows the ArrayList if required.

        Args:
            n: The desired capacity.
        """
        if (n >= len(self.arr)):
            arr1 = [None] * n

            for i in range(len(self.arr)):
                arr1[i] = self.arr[i]

            self.arr = arr1

    def constrict(self):
        if (self.length * 0.25 >= len(self.arr)):
            arr1 = [None] * int(self.length / 2)

            for i in range(len(self.arr)):
                arr1[i] = self.arr[i]

            self.arr = arr1

    def append(self, x):
        """Appends `x` to the ArrayList.

        Target Complexity: O(1) amortized.

        Args:
            x: The value to append.
        """
        if (len(self.arr) == 0):
            self.reserve(1)
        elif (len(self.arr) + 1 > self.length):
            self.reserve(self.length * 2)

        self.arr[self.length] = x
        self.length += 1

    def extend(self, xs):
        """Extends the ArrayList by appending all the items from ArrayList `xs`.

        Target Complexity: O(len(xs)) amortized.

        Args:
            xs: The ArrayList to be appended.
        """
        self.reserve(len(xs) + self.length)

        for i in range(self.length, len(xs) + self.length):
            self.arr[i] = xs[i - self.length]

        self.length += len(xs)

    def pop(self):
        """Removes and returns the last element of the ArrayList.

        Target Complexity: O(1).

        Returns:
            The last element of the ArrayList.

        Raises:
            IndexError: If the ArrayList is empty.
        """
        if (self.length == 0):
            raise IndexError("Arraylist is empty")

        ret = self.arr[self.length - 1]
        self.arr[self.length - 1] = None
        self.length -= 1
        self.constrict()

        return ret

    def pop_front(self):
        """Removes and returns the first element of the ArrayList.

        Target Complexity: O(N).

        Returns:
            The first element of the ArrayList

        Raises:
            IndexError: If the ArrayList is empty.
        """
        if (self.length == 0):
            raise IndexError("arraylist is empty")

        ret = self.arr[0]

        for i in range(self.length - 1):
            self.arr[i] = self.arr[i + 1]
        self.arr[self.length - 1] = None
        self.length -= 1
        self.constrict()

        return ret

    def pop_idx(self, idx):
        if (idx >= self.length or idx < 0):
            raise IndexError("pop index out of range")

        ret = self.arr[idx]

        for i in range(idx, self.length - 1):
            self.arr[i] = self.arr[i + 1]

        self.arr[self.length - 1] = None
        self.length -= 1
        self.constrict()

        return ret
