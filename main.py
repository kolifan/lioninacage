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

def myrandom():
    import random
    start = 10
    end = 99
    quantity = 10
    i = 0
    random_list = []
    while i<=quantity:
        rnd = random.randint(start, end)
        if (rnd % 2) != 0:
            random_list.append(rnd)
            i = i + 1

    return random_list

def myrandom1():
    import random
    start = 10
    end = 99
    quantity = 10
    i = 0
    random_list = [random.randint(start, end) for _ in range(quantity)]
    random_list = [num for num in random_list if num % 2 != 0]

    return random_list

print(myrandom())
print(myrandom1())

# a = [2,2,3,7,7,11,15,21,21,21,35,43]
# lion = input("inpit number: ")
# ind = cage(a, int(lion))
# print(f"index of {lion} is {ind}")