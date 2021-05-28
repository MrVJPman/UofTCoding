class EmptyHeapErorr(Exception):
    pass

class Heap(object):
    def __init__(self, L=None):
        """(Heap, list of pair-wise comparable objects) -> NoneType
        Treating L as a complete binary tree, reorder the elements in L
        so that they are a valid heap. This is known as the heapify operation.
        If L is None, this initializes a new, empty Heap.
        """
        if L is None:
            self._data = []
        else:
            # If we percolate down the first 1/2 of the elements,
            # the second half will already be heapfified
            for i in reversed(range(0, (len(L) - 1) / 2)):
                _percolate_down(L, i)
            
            self._data = L
            
    def insert(self, element):
        """(Heap, object) -> NoneType
        Insert the element into the heap
        """
        self._data.append(element)
        # Percolate up the last element
        _percolate_up(self._data, self._data[-1])

    def delete(self):
        """Heap -> object
        Remove and return the maximum-valued element in the heap
        """
        if not self:
            raise EmptyHeapError()

        # Return the first element and replace it with the last element
        root = self._data[0]
        self._data[0] = self._data[-1]
        # Percolate the root down
        _percolate_down(self._data, 0)

        return root

    def __len__(self):
        return len(self._data)

def _parent(i):
    """Return the parent index of the item at index i (-1 if at root)"""
    return i / 2

def _left(i):
    """Return the left child index of the item at index i"""
    return 2 * i + 1

def _right(i):
    """Return the right child index of the item at index i"""
    return 2 * i + 2

def _percolate_down(L, i):
    """(list, int) -> NoneType
    Given a list and the index of an item (where each child of the item is a
    valid heap), bubble down the item, swapping with the larger child until
    the heap property is satisfied.
    """
    left = _left(i)
    right = _right(i)
    # While there are children that are greater
    while ((left <= len(L) and L[left] > L[i]) or 
           (right <= len(L) and L[right] > L[i])):
        # Swap with the greater child
        if right <= len(L) and L[right] > L[left]:
            child = right
        else:
            child = left

        L[i], L[child] = L[child], L[i]
        i = child
        left = _left(i)
        right = _right(i)

def _percolate_up(L, i):
    """(list, int) -> NoneType
    Given a list and the index of an item, bubble up the item, 
    swapping with the parent until the heap property is satisfied.
    """
    parent = _parent(i)
    # While we have a parent that is less, swap up
    while parent > 0 and L[i] > L[parent]:
        L[i], L[parent] = L[i], L[parent]
        i = parent
        parent = _parent(i)


if __name__ == '__main__':
    L = range(21)
    h = Heap(L)
    for i in reversed(range(21)):
        assert h.delete() == i
    
