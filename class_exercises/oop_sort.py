def mysort(targetlist, comp=None, key=None, reverse=False):

    n = 0

    while n <= len(targetlist):
        for i in range(n, len(targetlist)):
            print("checking item at index {}!".format(i))
            if targetlist[n] > targetlist[i]:
                print("popping {} into position {}".format(targetlist[i], n))
                targetlist.insert(n, targetlist.pop(i))
        n += 1

    for i in targetlist:
        if type(i) is str:
            i = i.upper()

    return targetlist

print(mysort([4, 2, "dignity", 76, 34, "cat", 87, 23]))

