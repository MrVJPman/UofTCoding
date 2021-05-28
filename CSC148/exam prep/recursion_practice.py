'''Write the following methods recursively.

They are mostly exercises that were collected from various sources on
the internet:

  http://academics.tjhsst.edu/compsci/CS2C/U3/recurlab.html
  http://www.cs.arizona.edu/classes/cs227/spring06/misc/24RecursionExercises.htm
  http://www.engr.mun.ca/~theo/Courses/ds/recursion_practice.html
  http://www.cs.arizona.edu/classes/cs227/spring06/misc/50RecursionExercises.htm
'''

def rev(n):
    '''Return the result of reversing the digits in integer n. For example,
    rev(512) should return 215.'''
    if n < 10:
        return n
    else:
        power = 1
        while (10 ** power) < n:
            power += 1
        power -= 1
        return ((n % 10) * (10 ** power)) + rev(n/10)

def add_commas(n):
    '''Return a string version of integer n with commas added. For example,
    add_commas(15866321) should return "15,866,321".'''
    if len(str(n)) <= 3 :
        return str(n)
    else:
        return add_commas(n/1000) + ',' + str(n)[-3:]

def index(L, v):
    '''Return the index of v in list L.'''
    if L[0] == v:
        return 0
    else:
        return 1 + index(L[1:], v)

def sum(L):
    '''Return the sum of the numbers in list L.'''
    if L == []:
        return 0
    else:
        return L[0] + sum(L[1:])


def _binary_search(L, v, i, j):
    '''Return the index of v in L[i:j], or j if v is not in L.'''
    index = (i + j) / 2
    if index == j or L[index] == v:
        return index
    elif L[index] < v:
        i = index + 1
        return _binary_search(L, v, i, j)
    elif L[index] > v:
        j = index - 1
        return _binary_search(L, v, i, j)

def a_search(L, v):
    return _binary_search(L, v, 0, len(L))

def power(x, n):
    '''Return x to the power n using this formula:

    http://www.enel.ucalgary.ca/People/Norman/engg335_fall1997/recurs/power_t.gif
    '''
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return (power(x, n/2)) ** 2
    elif n % 2 == 1:
        return x * ((power(x, (n-1)/2)) ** 2)


def num1s(n):
    '''Write a recursive function that, given a nonnegative int n, yields the
    number of 1's in its binary representation. For example, suppose n = 17.
    The binary representation of 17 is 10001, so the function would return 2.

    The following facts may be useful:

    (1) The rightmost bit of the binary representation of n is 1 if and only
    if n is odd.

    (2) For n > 0, the binary representation of n is: (binary representation
    of n/2) followed by (the rightmost bit of the binary representation of
    n).'''
    if n < 2:
        return 1
    else:
        return n % 2 + num1s(n/2)

def flatten(L):
    '''Write a recursive function called flatten that takes a list as a
    parameter and flattens it: if any items are themselves lists their
    contents are retrieved from those nested lists.'''
    new_list = []
    for item in L:
        if type(item) is list:
            new_list = new_list + flatten(item)
        else:
            new_list.append(item)
    return new_list
