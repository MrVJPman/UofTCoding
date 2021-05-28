from sorts import insertion_sort, selection_sort, quicksort, builtin_sort
from random import shuffle
from profile import run
from time import clock
from radix import sort

if __name__ == "__main__":
    #sorts = ["selection_sort", "insertion_sort", "quicksort", "builtin_sort"]
    sorts = ["insertion_sort", "quicksort", "builtin_sort", "sort"]
    #sizes = [1000, 2000, 4000]
    sizes = [1000, 2000, 4000]

    for sort_item in sorts:
        for size in sizes:
            print "---------------------------------------------------------------"
            print "  Sorting Algorithm: %s on %s items." % (sort, size)
            print "---------------------------------------------------------------"
            L = range(size)
            shuffle(L)
            run("%s(L)" % sort_item)
            assert L == range(size)
