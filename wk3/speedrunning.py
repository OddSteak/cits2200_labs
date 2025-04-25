# Name: Baasil Siddiqui
# Student Number: 23895849

class Leaderboard:
    """A leaderboard of speedrunning record times.

    Each entry has a time in seconds and a runner name.
    Runners may submit multiple runs.
    The leaderboard is ranked fastest run first.
    Ties receive the same rank as each other, so for example if runners submit
    the times 10, 20, 20, and 30, they will have the ranks 1, 2, 2, and 4.
    """

    def __init__(self, runs=[]):
        """Constructs a leaderboard with the given runs.

        The given list of runs is not required to be in order.

        Args:
            runs: Initial leaderboard entries as list of (time, name) pairs.
        """
        self.data = self.merge_sort(runs)

    def get_runs(self):
        """Returns the current leaderboard.

        Leaderboard is given in rank order, tie-broken by runner name.

        Returns:
            The current leaderboard as a list of (time, name) pairs.
        """
        return self.data

    def submit_run(self, time, name):
        """Adds the given run to the leaderboard

        Args:
            time: The run time in seconds.
            name: The runner's name.
        """
        if (self.data[0] > (time, name)):
            self.data.insert(0, (time, name))
            return
        if (self.data[len(self.data) - 1] < (time, name)):
            self.data.append((time, name))
            return

        low = 0
        high = len(self.data)

        while (low < high):
            mid = (low + high) // 2

            if (self.data[mid] > (time, name)):
                high = mid

            elif (self.data[mid] < (time, name)):
                if self.data[mid + 1] > (time, name):
                    self.data.insert(mid + 1, (time, name))
                    return
                else:
                    low = mid + 1

    def get_rank_time(self, rank):
        """Get the time required to achieve at least a given rank.

        For example, `get_rank_time(5)` will give the maximum possible time
        that would be ranked fifth.

        Args:
            rank: The rank to look up.

        Returns:
            The time required to place `rank`th or better.
        """
        return self.data[rank - 1][0]

    def get_possible_rank(self, time):
        """Determine what rank the run would get if it was submitted.

        Does not actually submit the run.

        Args:
            time: The run time in seconds.

        Returns:
            The rank this run would be if it were to be submitted.
        """
        if (self.data[0][0] >= time):
            return 1
        if (self.data[len(self.data) - 1][0] < time):
            return len(self.data) + 1

        low = 0
        high = len(self.data)

        while (low < high):
            mid = (low + high) // 2

            if (self.data[mid][0] > time):
                high = mid

            elif (self.data[mid][0] < time):
                if self.data[mid + 1][0] >= time:
                    return mid + 2
                else:
                    low = mid + 1

            else:
                rank = mid
                for i in range(mid - 1, -1, -1):
                    if (self.data[i][0] == time):
                        rank = i
                    else:
                        break
                return rank + 1

    def count_time(self, time):
        """Count the number of runs with the given time.

        Args:
            time: The run time to count, in seconds.

        Returns:
            The number of submitted runs with that time.
        """
        low = 0
        high = len(self.data)

        while (low < high):
            mid = (low + high) // 2

            if (self.data[mid][0] < time):
                low = mid + 1

            elif (self.data[mid][0] > time):
                high = mid

            else:
                res = 1
                for i in range(mid + 1, len(self.data)):
                    if (self.data[i][0] == time):
                        res += 1
                    else:
                        break
                for i in range(mid - 1, -1, -1):
                    if (self.data[i][0] == time):
                        res += 1
                    else:
                        break

                return res

        return 0

    def merge(self, lhs, rhs, res):
        """Merges a pair of sorted lists.

        Args:
            lhs: A sorted list to be merged with rhs.
            rhs: A sorted list to be merged with lhs.

        Returns:
            A sorted list containing all the elements of lhs and rhs.
        """
        rp = 0
        lp = 0

        while lp + rp < len(res):
            if rp == len(rhs) or (lp < len(lhs) and lhs[lp] < rhs[rp]):
                res[lp + rp] = lhs[lp]
                lp += 1
            else:
                res[lp + rp] = rhs[rp]
                rp += 1

        return res

    def merge_sort(self, xs):
        """Sorts the given list using merge sort.

        Args:
            xs: The list to be sorted.

        Returns:
            The list in ascending order.
        """
        if (len(xs) == 1 or len(xs) == 0):
            return xs

        mid = len(xs) // 2
        s1 = self.merge_sort(xs[:mid])
        s2 = self.merge_sort(xs[mid:])

        return self.merge(s1, s2, xs)
