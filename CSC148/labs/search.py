import time
import random

def binary_search(L, e):
    """(list, object) -> bool
    Return True if e is in the (ascending) sorted list L, else False
    """
    # Call our helper with the appropriate low and high
    return _binary_search(L, e, 0, len(L) - 1)

def _binary_search(L, e, low, high):
    # Do a binary search between L[low] and L[high] (inclusive)

    # base cases
    if low > high:
        return False
    elif low == high:
        return L[low] == e
    else:
        # recurse
        # Get the middle value, halway between our bounds
        i = int((high + low) / 2)
        midpoint = L[i]
        if e < midpoint:
            # everything in L[:i] <= midpoint
            return _binary_search(L, e, low, i - 1)
        elif e > midpoint:
            return _binary_search(L, e, i + 1, high)
        else:
            # e == midpoint
            return True


def normal_search(L, e):
    """(list, object) -> bool
    Return True if e is in the list L, else False
    """
    return e in L


def time_one(n, L, fxn):
    """(int, int, function) -> float
    Return number of seconds to do given n searches in a list L using fxn
    """
    start = time.clock()
    for i in xrange(n):
        e = random.randrange(len(L))
        fxn(L, e)

    return time.clock() - start

if __name__ == "__main__":
    L = [1, 2, 3, 4, 5, 7]
    assert binary_search(L, 5)
    assert binary_search(L, 7)
    assert binary_search(L, 1)
    assert binary_search(L, 2)
    assert not binary_search(L, 6)

    for size in [1000, 10000, 100000]:
        print "size:", size
        L1 = range(size)
        random.shuffle(L1)
        L2 = L1[:]

        print "  binary:", time_one(1000, L1, binary_search)
        print "  normal:", time_one(1000, L2, normal_search)
