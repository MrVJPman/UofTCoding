def _quicksort(L):
    """Return new list of sorted elements from L"""
    if len(L) == 0:
        return []
    else:
        # choose "random" pivot (a la: http://xkcd.com/221/)
        pivot = L[0]

        # collect all of the value less than our pivot
        # could do:
        #   less = [value for value in L[1:] if value < pivot]
        less = []
        # collect all of the value greater than our pivot
        greater = []
        for value in L[1:]:
            if value < pivot:
                less.append(value)
            else:  # value >= pivot:
                greater.append(value)

        # stick them all together
        combined = _quicksort(less) + [pivot] + _quicksort(greater)
        return combined


def quicksort(L):
    """list -> NoneType
    Sort the values in the list in non-decreasing order (modifying L)
    """
    L[:] = _quicksort(L)


if __name__ == '__main__':
    L = [1, -53, 12, 4, 6, 2, 0]
    quicksort(L)
    assert L == sorted(L)
    # As a side note, since quicksort changes the list, it's better to do this
    # to make sure that L still contains all the original numbers:
    # L = [1, -53, 12, 4, 6, 2, 0]
    # L2 = L[:]  # copy of L
    # quicksort(L2)
    # assert L2 == sorted(L)

    L = []
    quicksort(L)
    assert L == []

    L = [1]
    quicksort(L)
    assert L == [1]


    L = [1, 1,1 ,1 , 1, 1, 1, 1]
    quicksort(L)
    assert L == sorted(L)