from queue import Queue
import math

def sort(L): #REGULAR BASES
    main_bin = []
    #~~~~~~~~~~~~~~~~~~~~~~~~~~START OF ADDITIONAL CODE OF NEGATIVE~~~~~~~~~~~~~~~~~~
    main_bin_neg = []
    #~~~~~~~~~~~~~~~~~~~~~~~~~~END OF ADDITIONAL CODE OF NEGATIVE~~~~~~~~~~~~~~~~~~
        
    for i in range(10):
        main_bin.append(Queue())
        #~~~~~~~~~~~~~~~~~~~~~~~~~~START OF ADDITIONAL CODE OF NEGATIVE~~~~~~~~~~~~~~~~~~
        main_bin_neg.append(Queue())
        #~~~~~~~~~~~~~~~~~~~~~~~~~~END OF ADDITIONAL CODE OF NEGATIVE~~~~~~~~~~~~~~~~~~
    power = 0
    while True:
        for value in L:
            if value >= 0:
                if value / (10 ** power) > 0 :
                    index = (value / (10 ** power)) % 10
                    digit_bin = main_bin[index]
                    digit_bin.enqueue(value)
                else:
                    digit_bin = main_bin[0]
                    digit_bin.enqueue(value)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~START OF ADDITIONAL CODE OF NEGATIVE~~~~~~~~~~~~~~~~~~
            else:
                if (-value) / (10 ** power) > 0 :
                    index = (-value / (10 ** power)) % 10
                    digit_bin = main_bin_neg[-index]
                    _insert(digit_bin, value)
                else:
                    digit_bin = main_bin[0]
                    _insert(digit_bin, value)                    
        #~~~~~~~~~~~~~~~~~~~~~~~~~~END OF ADDITIONAL CODE NEGATIVE~~~~~~~~~~~~~~~~~~            
        power = power + 1
        if main_bin[0].size() == len(L):
            break
        del L[:]
        #~~~~~~~~~~~~~~~~~~~~~~~~~~START OF ADDITIONAL CODE OF NEGATIVE~~~~~~~~~~~~~~~~~~
        for digit_bin in main_bin_neg:
            while not digit_bin.is_empty():
                element = digit_bin.dequeue()
                L.append(element)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~END OF ADDITIONAL CODE NEGATIVE~~~~~~~~~~~~~~~~~~
        for digit_bin in main_bin:
            while not digit_bin.is_empty():
                element = digit_bin.dequeue()
                L.append(element)

def _insert(queue, value):
    L = []
    while not queue.is_empty():
        current_int = queue.dequeue()
        L.append(current_int)
    index = 0
    while len(L) > index and L[index] < value:
        index = index + 1
    L.insert(index, value)
    while L:
        queue.enqueue(L.pop(0))
    

#def _insert(queue, value): <-This is the "original" _insert without using a list.
    #"""(Queue, int) --> NoneType
    #Insert value into queue so that, as items are dequeued from queue, the
    #values that will be returned will be given in the sorted order."""
    #storage_queue = Queue()
    #while not queue.is_empty():
        #current_int = queue.dequeue()
        #if current_int < value :
            #storage_queue.enqueue(current_int)
        #else:
            #storage_queue.enqueue(value)
            #break
    #if queue.is_empty():
        #storage_queue.enqueue(value)
    #else:
        #while not queue.is_empty():
            #storage_queue.enqueue(queue.dequeue())
    #while not storage_queue.is_empty():
        #queue.enqueue(storage_queue.dequeue())
        
def clean_word(word):
    stripped_word = ''
    for letter in word:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            stripped_word += letter
    return stripped_word
            
        
def radix_letter(L):
    main_bin = [] #97=a, 122=z
    for i in range(27):
        main_bin.append(Queue())
    index = -1
    while True:
        first_bin = main_bin[0]
        for word in L:
            word = word.lower()
            if not word.isalpha():
                word = clean_word(word)
            if len(word) >= (-index):
                letter = word[index]
                main_bin_index = ord(letter) - 96
                letter_bin = main_bin[main_bin_index]
                letter_bin.enqueue(word)
            else:
                first_bin.enqueue(word)
        if first_bin.size() == len(L):
            break
        del L[:]
        index = index - 1
        for letter_bin in main_bin:
            while not letter_bin.is_empty():
                element = letter_bin.dequeue()
                L.append(element)


if __name__ == '__main__':
    
    L=['aca', 'abb', 'aac', 'addd']
    radix_letter(L)
    assert L == ['aac', 'abb', 'aca', 'addd']    
    
    L=['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    radix_letter(L)
    assert L == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    L=['aaa', 'aa', 'a']
    radix_letter(L)
    assert L == ['a', 'aa', 'aaa']
    
    L=['A', 'B', 'C']
    radix_letter(L) 
    assert L == ['a', 'b', 'c']

    L=["a's's's", "a's's'", "a's"]
    radix_letter(L) 
    assert L == ["as", "ass", "asss"]