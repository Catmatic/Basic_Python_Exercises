def odd_elements(targetlist):

    """Returns the odd elements in a list.
    >>>odd_elements([1, 2, 3, 4, 5])
    "1, 3, 5"
    """
    
    currentposition = 1
    output = ""
    
    for i in targetlist:
    #add list item to output string with comma if not last element.
        if i == targetlist[-1]:
        #Argh. This works, but if the same element recurs in the list it will
        #also have a period.
            if currentposition % 2 == 1:
                output += "{}.".format(i)
            currentposition += 1
        else:
        #add list item to output string with period if last element.
        #This code block is pasted from above. How can I do this without repeating?
            if currentposition % 2 == 1:
                output += "{}, ".format(i)
            currentposition += 1
        
    return(output)

print(odd_elements([1, 2, 5, 5, 3, 4, 5]))
