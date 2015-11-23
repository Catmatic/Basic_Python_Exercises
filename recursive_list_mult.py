def list_mult(l, n):

    """
    Repeat the list l as many times as n.

    >>> list_mult([1, 2, 3], 2)
    [1, 2, 3, 1, 2, 3]
    >>> list_mult([1, 2], 3)
    [1, 2, 1, 2, 1, 2]
    """

    if n == 1:
        return l
    else:
        return l + list_mult(l, n-1)

print(list_mult([1, 2], 3))
