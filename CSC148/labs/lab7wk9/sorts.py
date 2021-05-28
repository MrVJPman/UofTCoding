def _find_min(L, i):
    '''Return the index of the smallest item in L[i:]'''
    
    smallest = i
    size = len(L)
    for j in range(i + 1, size):
        if L[j] < L[smallest]:
            smallest = j
    return smallest

def selection_sort(L):
    '''Sort the items in L in non-descending order.'''
    
    size = len(L)
    for i in range(size):
        smallest = _find_min(L, i)
        L[smallest], L[i] = L[i], L[smallest]


def _binary_search(L, v, begin, end):
    '''Return the rightmost index in L[begin:end] where v appears, or
    the index where v would be inserted if v is not in L.
    Requires: L[begin:end] is sorted.'''

    # L[:i + 1] <= v, L[j:] > v
    i, j = begin - 1, end
    
    # Done when i == j - 1
    while i != j - 1:
        m = (i + j) / 2
        if L[m] > v:
            j = m
        else:
            i = m
    
    return j

def _insert(L, i):
    '''Move L[i] to where it belongs in L[:i]'''

    v = L[i]
    j = _binary_search(L, v, 0, i)
    del L[i]
    L.insert(j, v)

def insertion_sort(L):
    '''Sort the items in L in non-decreasing order.'''

    i = 1
    num_items = len(L)
    # Insert each item i where it belongs in L[0:i + 1]
    while i != num_items:
        _insert(L, i)
        i = i + 1

def quicksort(L):
    '''(list) -> NoneType
    Sort the items in L in non-decreasing order.'''
    L[:] = _quicksort(L)

def _quicksort(L):
    '''(list) -> list
    Return a new list containing the items from L but in non-decreasing order.
    This implementation taken from here:
        http://en.literateprograms.org/Quicksort_(Python)
    '''
    if L == []: 
        return []
    else:
        pivot = L[0]
        lesser = _quicksort([x for x in L[1:] if x < pivot])
        greater = _quicksort([x for x in L[1:] if x >= pivot])
        return lesser + [pivot] + greater

def builtin_sort(L):
    '''(list) -> NoneType
    Sort the items in L in non-decreasing order.'''
    L[:] = sorted(L)

