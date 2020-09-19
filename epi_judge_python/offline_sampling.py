import functools
from typing import List
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def random_sampling(k: int, A: List[int]) -> None:
    # Array A 에서 크기 k 짜리 subset을 골라 return 하기
    # Subset 을 array A의 앞쪽에 배치하여 return 하면 된다.
    # Approach 1 : A 의 모든 요소를 iter 하면서 k/n 확률로 선택하기 -> k 개가 선택 안될 수 있다.
    # Approach 2 : A 의 모든 크기 k 짜리 subset을 만들고 그중에 하나를 뽑기 -> 너무 오래 걸린다.
    # Approach 3 : 크기 k-1 짜리 subset이 이미 존재한다고 가정하고, 나머지 요소 중에서 하나를 뽑아 크기 k 짜리 subset을 만든다.

    for i in range(k):
        r = random.randint(i, len(A)-1)
        A[i], A[r] = A[r], A[i]

    return


@enable_executor_hook
def random_sampling_wrapper(executor, k, A):
    def random_sampling_runner(executor, k, A):
        result = []

        def populate_random_sampling_result():
            for _ in range(100000):
                random_sampling(k, A)
                result.append(A[:k])

        executor.run(populate_random_sampling_result)

        total_possible_outcomes = binomial_coefficient(len(A), k)
        A = sorted(A)
        comb_to_idx = {
            tuple(compute_combination_idx(A, len(A), k, i)): i
            for i in range(binomial_coefficient(len(A), k))
        }

        return check_sequence_is_uniformly_random(
            [comb_to_idx[tuple(sorted(a))] for a in result],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_sampling_runner, executor, k, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('offline_sampling.py',
                                       'offline_sampling.tsv',
                                       random_sampling_wrapper))
