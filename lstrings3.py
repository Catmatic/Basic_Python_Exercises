#Is some sort of argument check called for here? ie, issue some warning
#if targetlist is not a list?

def element_check(target, targetlist):

    """Tests whether an element is in a list.
    element_check(x, ["a", "b", "x"])
    True
    element_check(x, ["a", "b", "c"])
    False
    """
    
    found = False
    
    for e in targetlist:
        if e == target:
            found = True
                
    return(found)
    
print(element_check("x", ["a", "b", "x"]))
print(element_check("x", ["a", "b", "c"]))
