import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A: List[int]) -> None:
    # even_i 는 짝수쪽 cursor odd_i 는 홀수쪽 cursor
    even_i, odd_i = 0, len(A) - 1

    while even_i <= odd_i:
        # num 이 짝수면 pass
        if A[even_i] % 2 == 0:
            even_i += 1
        # num 이 홀수면, 홀수 쪽으로 보내주고 odd_i -= 1
        else:
            A[even_i], A[odd_i] = A[odd_i], A[even_i]
            odd_i -= 1

    return


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
