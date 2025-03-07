def insertion_sort(xs):
    """Sorts the given list using insertion sort.

    Args:
        xs: The list to be sorted.

    Returns:
        The list in ascending order.
    """
    for i in range(1, len(xs)):
        key = xs[i]
        j = i - 1

        while j >= 0 and xs[j] > key:
            xs[j + 1] = xs[j]
            j -= 1

        xs[j + 1] = key

    return xs


def merge(lhs, rhs):
    """Merges a pair of sorted lists.

    Args:
        lhs: A sorted list to be merged with rhs.
        rhs: A sorted list to be merged with lhs.

    Returns:
        A sorted list containing all the elements of lhs and rhs.
    """
    rp = 0
    lp = 0
    nl = []

    while lp != len(lhs) and rp != len(rhs):
        if (lhs[lp] < rhs[rp]):
            nl.append(lhs[lp])
            lp += 1
        elif (rhs[rp] <= lhs[lp]):
            nl.append(rhs[rp])
            rp += 1

    if (lp == len(lhs) and rp != len(rhs)):
        for i in range(rp, len(rhs)):
            nl.append(rhs[i])
    if (rp == len(rhs) and lp != len(lhs)):
        for i in range(lp, len(lhs)):
            nl.append(lhs[i])

    return nl


def merge_sort(xs):
    """Sorts the given list using merge sort.

    Args:
        xs: The list to be sorted.

    Returns:
        The list in ascending order.
    """
    if (len(xs) == 1):
        return [xs[0]]

    mid = len(xs) // 2
    return merge(merge_sort(xs[:mid]), merge_sort(xs[mid:]))
