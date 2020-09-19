from test_framework import generic_test


def fibonacci(n: int) -> int:
    # TODO - you fill in here.
    if n <= 1:
        return n

    fib_1, fib_2, fib_3 = 0,1, int()
    for _ in range(2, n+1):
        fib_3 = fib_1 + fib_2
        fib_1, fib_2 = fib_2, fib_3

    return fib_3


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
