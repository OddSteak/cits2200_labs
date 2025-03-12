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


def merge(lhs, rhs, res):
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


def merge_sort(xs):
    """Sorts the given list using merge sort.

    Args:
        xs: The list to be sorted.

    Returns:
        The list in ascending order.
    """
    if (len(xs) == 1):
        return xs

    mid = len(xs) // 2
    s1 = merge_sort(xs[:mid])
    s2 = merge_sort(xs[mid:])

    return merge(s1, s2, xs)
