def flatten(lst):

    """take a deeply nested list and flatten it to a single level.

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> flatten([[1], [2, 3], [4, 5, 6]])
    [1, 2, 3, 4, 5, 6]
    >>> flatten([1, [2, 3], [[4], [5, [6]]]])
    [1, 2, 3, 4, 5, 6]
    """

    if lst == []:
        return lst
    elif isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    else:
        return lst[:1] + flatten(lst[1:])

print(flatten([1, [2, 3], [[4], [5, [6]]]]))
