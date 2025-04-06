from arraylist import ArrayList


class HashMap:
    """A basic key-value HashMap.

    Note: You may not use a python dictionary at any point in this class.

    You should just use Python's built in `hash()` function for hashing keys.
    """

    def __init__(self):
        """Constructs an empty HashMap."""
        # More advanced implemenations exist, but here we will simply use a list
        # for each bucket. Investigate "open addressing" for smarter strategies.
        self.list = ArrayList()
        self.list.reserve(16)

        for i in range(16):
            self.list.append(None)

    def __len__(self):
        """Returns the number of elements in the HashMap."""
        c = 0

        for i in range(len(self.list)):
            if (self.list[i] is not None):
                c += len(self.list[i])

        return c

    def __getitem__(self, key):
        """Returns the value corresponding to the given key in the HashMap.

        Target Complexity: O(1) expected.

        Args:
            key: The key of the desired value.

        Returns:
            The value associated with `key`.

        Raises:
            KeyError: If the key is not in the HashMap.
        """
        ret = self.list[hash(key) % len(self.list)]

        if (ret is None):
            raise KeyError("key doesn't exist in hashmap")

        for i, (k, v) in enumerate(ret):
            if k == key:
                return v

        raise KeyError("key doesn't exist in hashmap")

    def __setitem__(self, key, value):
        """Associates `value` with the given `key` in the HashMap.

        Target Complexity: O(1) amortized.

        Any previous associated value is replaced.

        Args:
            key: The key to which to associate `value`.
            value: The value to be associated with `key`.
        """
        idx = hash(key) % len(self.list)

        if (self.list[idx] is None):
            self.list[idx] = ArrayList()

        for i in range(len(self.list[idx])):
            if (self.list[idx][i] is None):
                continue
            if (self.list[idx][i][0] == key):
                self.list[idx][i][1] = value
                return

        self.list[idx].append((key, value))

    def __contains__(self, key):
        """Check whether `key` appears in the HashMap.

        Target Complexity: O(1) expected.

        Args:
            key: The key for which to check.

        Returns:
            True if `key` appears in the HashMap, False otherwise.
        """
        idx = hash(key) % len(self.list)

        if (self.list[idx] is None):
            return False

        for i in range(len(self.list[idx])):
            if (self.list[idx][i] is None):
                continue
            if self.list[idx][i][0] == key:
                return True

        return False

    def remove(self, key):
        """Removes and returns the value associated with `key` in the HashMap.

        Target Complexity: O(1) expected.

        Args:
            key: The key of the entry to remove.

        Returns:
            The value associated with `key`.

        Raises:
            KeyError: If the HashMap does not contain `key`.
        """
        idx = hash(key) % len(self.list)

        if (self.list[idx] is None):
            raise KeyError("hashmap does not contain the key")

        for i in range(len(self.list[idx])):
            if (self.list[idx][i] is None):
                continue
            if (self.list[idx][i][0] == key):
                ret = self.list[idx][i][1]
                self.list[idx][i] = None
                return ret

        raise KeyError("hashmap does not contain the key")

    def delete(self, key):
        """Deletes `key` from the HashMap, if present.

        Does nothing if key is not already present.

        Target Complexity: O(1) expected.

        Args:
            key: The key to be deleted.

        Returns:
            True if `key` was deleted, False if it was not present.
        """
        idx = hash(key) % len(self.list)

        if (self.list[idx] is None):
            return False

        for i in range(len(self.list[idx])):
            if (self.list[idx][i] is None):
                continue
            if (self.list[idx][i][0] == key):
                self.list[idx][i] = None
                return True

        return False

    def items(self):
        """Gets a list of all (key, value) pairs from the HashMap.

        No specific order is guaranteed.

        Returns:
            A list of all (key, value) pairs.
        """
        ret = []

        for i in range(len(self.list)):
            for j in range(len(self.list[i])):
                ret.append(self.list[i][j])

        return ret
