def cage(array, num):
    if not isinstance(array, (list, tuple)):
        print(f"{array} is not an array!")
        return -1

    nindexstart = 0
    retindex = 0
    nindexfin = len(array) - 1
    moreloop = True

    while nindexstart <= nindexfin and moreloop:
        nindex = (nindexfin + nindexstart) // 2
        if array[nindex] == num:
            retindex = nindex
            moreloop = False
        elif array[nindex] < num:
            nindexstart = nindex + 1
        else:
            nindexfin = nindex - 1

    delta = nindexstart - nindexfin
    if delta==1:
        return -1 - nindexstart
    elif delta==-1:
        return retindex
    else:
        while array[retindex]==num and retindex>0:
            retindex = retindex - 1
        return retindex + 1

a = [2,2,3,7,7,11,15,21,21,21,35,43]
lion = input("inpit number: ")
ind = cage(a, int(lion))
print(f"index of {lion} is {ind}")