def f(i):
    """(int) -> int
    Return 1 less than i; raise an IndexError if i is 0.
    """
    if i == 0:
        x =  IndexError("Hey, i was zero.")
        raise x
    else:
        return i - 1

if __name__ == '__main__':
    print f(3)
    print f(27)

    try:
        print f(0) # Does this print happen?
        print "Do we get to this print statement?"
    except IndexError:
        print "There was an error here!"
    finally:
        print "This will ALWAYS get printed"


