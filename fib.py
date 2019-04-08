def fib(n):
    """
    fibonacci
    """


    if n == 0 or n ==1:
        return 1

    rval = fib(n - 1) + fib(n - 2)

    print(rval)

    return rval
