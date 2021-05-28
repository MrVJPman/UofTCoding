from queue import Queue

def merge(a, b):
    """(list, list) -> list
    Return new list of sorted values given two already-sorted lists
    """
    merged = []
    i = 0  # index into a
    j = 0  # index into b
    while not (i == len(a) or j == len(b)):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged

def mergesort_inplace(L, start, end):
    """mergesort L[start:end] (in place?)"""
    # if there are at least two value to sort
    if end - start > 1:
        # split the list into two halves
        # mergesort each half
        mid = (start + end) / 2
        mergesort_inplace(L, start, mid)
        mergesort_inplace(L, mid, end)
        # merge the two sorted halves back together
        combined = merge(L[start:mid], L[mid:end])
        # Exercise: finish this implementation!
        L[:] = combined + L[end+1:]

def mergesort(L):
    """list -> NoneType
    Sort the values in the list in non-decreasing order (modifies list)
    """
    if len(L) <= 1:
        return L
    else:
        # split the list into two halves
        first_half = L[:len(L) / 2]
        second_half = L[len(L) / 2:]
        # mergesort each half
        mergesort(first_half)
        mergesort(second_half)
        # merge the two sorted halves back together
        combined = merge(first_half, second_half)
        print combined, L
      #  assert len(new_list) == len(L)
        for i in range(len(combined)):
            L[i] = combined[i]

        # could also do: L[:] = combined

if __name__ == '__main__':
    L = [1, -53, 12, 4, 6, 2, 0]
    mergesort(L)
    assert L == sorted(L)

    L = []
    mergesort(L)
    assert L == []

    L = [1]
    mergesort(L)
    assert L == [1]


    L = [1, 1,1 ,1 , 1, 1, 1, 1]
    mergesort(L)
    assert L == sorted(L)