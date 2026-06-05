def cage(array, num):
    if not isinstance(array, (list, tuple)):
        print(f"{array} is not an array!")
        return -1

    nindexstart = 0
    nindexfin = len(array) - 1

    while nindexstart <= nindexfin:
        nindex = (nindexfin + nindexstart) // 2
        if array[nindex] == num:
            return nindex

        if array[nindex] < num:
            nindexstart = nindex + 1
        else:
            nindexfin = nindex - 1

    return -1

a = [2,3,5,7,11,14,19,21,32,41,43]
lion = input("inpit number: ")
ind = cage(a, int(lion))
print(f"index of {lion} is {ind}")