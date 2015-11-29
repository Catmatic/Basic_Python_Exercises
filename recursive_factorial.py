def factorial(n):

    """
    Factorial Function.

    >>> fact(5)
    120
    >>> fact(6)
    720
    """

    if n == 1:
        return n
    else:
        return n * factorial(n-1)


print(factorial(5))
