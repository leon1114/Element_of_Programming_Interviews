from test_framework import generic_test
from test_framework.test_failure import TestFailure
import functools, string


def int_to_string(x: int) -> str:
    is_neg = False
    if x < 0:
        x, is_neg = -x, True

    result = ""
    while True:
        result += chr(ord('0') + x % 10)
        x //= 10
        if x == 0:
            break
    if is_neg:
        result += '-'

    return result[::-1]


def string_to_int(s: str) -> int:
    return functools.reduce(lambda runningsum, c : runningsum * 10 + string.digits.index(c),
                            s[s[0].isnumeric() == False:],0) * (-1 if s[0] == '-' else 1)


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
