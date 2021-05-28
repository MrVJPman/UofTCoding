from radix_compare_bases import sortbase2, sortbase10, sortbase20
from random import shuffle
from profile import run
from time import clock

if __name__ == "__main__":
    #sorts = ["selection_sort", "insertion_sort", "quicksort", "builtin_sort"]
    sorts = ["sortbase2", "sortbase10", "sortbase20"]
    #sizes = [1000, 2000, 4000]
    sizes = [10000, 2000, 4000, 32000, 64000, 128000]

    for sort in sorts:
        for size in sizes:
            print "---------------------------------------------------------------"
            print "  Sorting Algorithm: %s on %s items." % (sort, size)
            print "---------------------------------------------------------------"
            L = range(size)
            shuffle(L)
            run("%s(L)" % sort)
            assert L == range(size)