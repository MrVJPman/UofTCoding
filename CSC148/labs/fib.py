def fib(n, prev_answers={0: 1, 1: 1}):
    """
    1 1 2 3 5 8 13 21 34 55 89 144 ...
    fib(0) = 1
    fib(1) = 1
    fib(n) = fib(n - 2) + fib(n - 1)
    """
    #if n in prev_answers:
        #return prev_answers[n]
    #else:
        #answer = fib(n - 2) + fib(n - 1)
        #prev_answers[n] = answer
        #return prev_answers[n]

    if not n in prev_answers:
        prev_answers[n] = fib(n - 2, prev_answers) + \
            fib(n - 1, prev_answers)

    return prev_answers[n]

if __name__ == "__main__":
    print fib(5) # 8
    print fib(8) # 34
    print fib(11) #144
    print fib(20)
    print fib(30)
    print fib(100)