def runningtotal(targetlist):

    """Finds the running total of a list.
    >>>runningtotal([3, 65, 39, 12])
    [3, 68, 107, 119]
    """

    runningtotal = 0
    runningtotallist = [] 

    for number in targetlist:
        #print(number)
        runningtotal += number
        #print(runningtotal)
        runningtotallist.append(runningtotal)
        #print(runningtotallist)

    return(runningtotallist)

print(runningtotal([3, 65, 39, 12]))
