def list_reverse(x):

    """Reverses a list in place.
    >>> list_reverse([1, 2, 3, 4, 5])
    "[5, 4, 3, 2, 1]"
    """""
    
    listlength = len(x)
    position = 0
    
    for element in range(0, listlength):
        x.insert(position, x.pop())
        position += 1
    return(x)
        
print(list_reverse([1, 2, 3, 4, 5]))
