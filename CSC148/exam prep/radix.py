from math import log
from queue import Queue

def sort(L, radix=10):
    if not L:
        return

    main = Queue()
    # Find out number of digits in longest (positive or negative) number
    biggest = max(abs(min(L)), abs(max(L)), 1)  # 1 in case all are 0
    n_digits = int(log(biggest, radix)) + 1
    # To handle negative numbers, subtract largest negative number from
    # all values to make them positive before radix
    offset = min(min(L), 0)
    for i in L:
        main.enqueue(i - offset)

    bins = [Queue() for i in range(radix)]

    for i in range(n_digits):
        # Place values in main bin into digit bins
        while not main.is_empty():
            val = main.dequeue()
            digit = get_digit(val, i, base=radix)
            bins[digit].enqueue(val)

        # Place values from digit inbs back into main bin
        for bin in bins:
            while not bin.is_empty():
                main.enqueue(bin.dequeue())
    
    for i in range(len(L)):
        L[i] = main.dequeue() + offset

def get_digit(number, i, base=10):
    """Return digit i in from the end of integer number (last digit is 0 in)"""
    assert i >= 0
    return (number / base ** i) % base


def sort_bin_by_letter(bin, i):
    """Sort words in bin by the letter at position i"""
    if bin.size() > 1:
        sub_bins = [Queue() for x in range(26)]
        shorter = Queue()  # bin for words with no more letters
        while not bin.is_empty():
            word = bin.dequeue()
            if i < len(word):
                sub_bin_index = ord(word[i]) - ord('a')
                sub_bins[sub_bin_index].enqueue(word)
            else:
                shorter.enqueue(word)
            
        while not shorter.is_empty():
            bin.enqueue(shorter.dequeue())

        for sub_bin in sub_bins:
            sort_bin_by_letter(sub_bin, i + 1)
            while not sub_bin.is_empty():
                bin.enqueue(sub_bin.dequeue())
            
def sort_lc(L):
    words = [''.join([c for c in word.lower() if c.isalnum()])
             for word in L]
    
    main = Queue()
    for word in words:
        main.enqueue(word)
        
    sort_bin_by_letter(main, 0)
    
    for i in range(len(L)):
        L[i] = main.dequeue()
