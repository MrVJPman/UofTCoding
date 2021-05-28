from queue import Queue 
def sortbase10(L): #REGULAR BASES
    main_bin = []
    main_bin_neg = []
    for i in range(10):
        main_bin.append(Queue())
    power = 0
    while True:
        for value in L:
            if value / (10 ** power) > 0 :
                index = (value / (10 ** power)) % 10
                digit_bin = main_bin[index]
                digit_bin.enqueue(value)
            else:
                digit_bin = main_bin[0]
                digit_bin.enqueue(value)
        power = power + 1
        if main_bin[0].size() == len(L):
            break
        del L[:]
        for digit_bin in main_bin:
            while not digit_bin.is_empty():
                element = digit_bin.dequeue()
                L.append(element)
                
def sortbase2(L): #REGULAR BASES
    main_bin = []
    main_bin_neg = []
    for i in range(2):
        main_bin.append(Queue())
    power = 0
    while True:
        for value in L:
            if value / (2 ** power) > 0 :
                index = (value / (2 ** power)) % 2
                digit_bin = main_bin[index]
                digit_bin.enqueue(value)
            else:
                digit_bin = main_bin[0]
                digit_bin.enqueue(value)
        power = power + 1
        if main_bin[0].size() == len(L):
            break
        del L[:]
        for digit_bin in main_bin:
            while not digit_bin.is_empty():
                element = digit_bin.dequeue()
                L.append(element)
                
def sortbase20(L): #REGULAR BASES
    main_bin = []
    main_bin_neg = []
    for i in range(20):
        main_bin.append(Queue())
    power = 0
    while True:
        for value in L:
            if value / (20 ** power) > 0 :
                index = (value / (20 ** power)) % 20
                digit_bin = main_bin[index]
                digit_bin.enqueue(value)
            else:
                digit_bin = main_bin[0]
                digit_bin.enqueue(value)
        power = power + 1
        if main_bin[0].size() == len(L):
            break
        del L[:]
        for digit_bin in main_bin:
            while not digit_bin.is_empty():
                element = digit_bin.dequeue()
                L.append(element)
