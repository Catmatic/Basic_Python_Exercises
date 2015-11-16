def largest_element(list):

    """Finds the largest element in a list.
    >>>largest_element([list, of, random, elements])
    
    "elements"
    """
    largest_element_length = 0
    
    for item in list:
        if type(item) == str:
            if len(item) > largest_element_length:
                largest_element = item
                largest_element_length = len(item)
        elif item > largest_element_length:
            largest_element = item
            largest_element_length = item
            
    return(largest_element)

print(largest_element(["list", "of", 9, 10.5, True]))
