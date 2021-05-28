def bubble_sort(L):
    """Sort the items in L in non-descending order"""
    # Repeatedly swap out-of-order pairs
    for i in range(len(L)):
        # Invariant: L[-i:] is finished (end of list)
        # Each time through this loop, the max value is swapped to the end
        for j in range(0, len(L) - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]


def _find_smallest(L, i):
    """Return index of minimum value in L[i:]"""
    smallest = i
    for j in range(i + 1, len(L)):
        if L[j] < L[smallest]:
            smallest = j

    return smallest

def selection_sort(L):
    """Sort the items in L in non-descending order"""
    # In each iteration, move the smallest unsorted element to its
    # proper place.
    for i in range(len(L)):
        # Invariant: L[:i] is finished
        # Find the smallest element in L[i:]
        smallest = _find_smallest(L, i)
        L[i], L[smallest] = L[smallest], L[i]


def _insert(L, i):
    """Shift L[i] forward until L[:i+1] is sorted.
    L[:i] must already be sorted.
    """
    v = L[i]
    while i > 0 and L[i - 1] > v:
        L[i] = L[i - 1]
        i -= 1

    # i is now 0 or L[i - 1] <= v
    L[i] = v

def insertion_sort(L):
    """Sort the items in L in non-descending order"""
    for i in range(1, len(L)):
        # Invariant: L[:i] is sorted
        _insert(L, i)
