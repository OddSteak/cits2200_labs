def cube_root(x):
    """Find the cube root of `x` using binary search.

    Does not use exponentiation operator (**).

    Args:
        x: The value for which to find the square root.

    Returns:
        The cube root of `x`, accurate to 7 decimal places.
    """
    neg = False
    if (x < 0):
        neg = True
        x = abs(x)
    low = 0
    high = max(1, x)
    mid = high / 2
    margin = 1e-8

    while (high - low > margin):
        mid = (high + low) / 2
        cube = mid ** 3

        if (abs(cube - x) <= margin):
            break
        if (cube < x):
            low = mid
            continue
        if (cube > x):
            high = mid
            continue

    return mid if neg is False else - mid


def lower_bound(xs, x):
    """Find the number of elements less than a value in a sorted list.

    Args:
        xs: A list sorted in ascending order.
        x: The value to search for.

    Returns:
        The number of elements less than `x` in `xs`.
    """
    if (xs[0] >= x):
        return 0
    if (xs[len(xs) - 1] <= x):
        return len(xs)

    low = 0
    high = len(xs)

    while (low < high):
        mid = (low + high) // 2

        if (xs[mid] >= x):
            high = mid

        elif (xs[mid] < x):
            if xs[mid + 1] >= x:
                return mid + 1
            else:
                low = mid + 1


def upper_bound(xs, x):
    """Find the number of elements less than or equal to a value in a sorted list.

    Args:
        xs: A list sorted in ascending order.
        x: The value to search for.

    Returns:
        The number of elements less than or equal to `x` in `xs`.
    """
    if (xs[0] > x):
        return 0
    if (xs[len(xs) - 1] < x):
        return len(xs)

    low = 0
    high = len(xs)

    while (low < high):
        mid = (low + high) // 2

        if (xs[mid] > x):
            high = mid

        elif (xs[mid] <= x):
            if xs[mid + 1] > x:
                return mid + 1
            else:
                low = mid + 1
