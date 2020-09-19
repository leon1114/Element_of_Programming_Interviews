from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    # B[i] -> ith index 에서 끝나는 모든 subarray 합 중에 최고 값
    # B[i] -> MAX( B[i-1] + cur, cur ) => 기존 subarray에 합류 할지 안할지의 문제임
    cur_max, glob_max = 0, 0
    for a in A:
        cur_max = max(cur_max + a, a)
        glob_max = max(glob_max, cur_max)
    return glob_max


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
