def listcombine(ziplist1, ziplist2):

    """Combines two lists into one by taking alternating elements from each.
    >>>listcombine([1, 2, 3], ["a", "b", "c", "d", "e"])
    [1, "a", 2, "b", 3, "c", "d", "e"]
    """

    zipindex1 = 0
    zipindex2 = 0
    combinedlist = []

    while zipindex1 < len(ziplist1) or zipindex2 < len(ziplist2):
        if zipindex1 < len(ziplist1):
            combinedlist.append(ziplist1[zipindex1])
            zipindex1 += 1
        if zipindex2 < len(ziplist2):
            combinedlist.append(ziplist2[zipindex2])
            zipindex2 += 1

    return(combinedlist)

print(listcombine([1, 2, 3], ["a", "b", "c", "d", "e"]))       
