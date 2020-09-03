from typing import List

from test_framework import generic_test

import bisect as bi

def h_index(citations: List[int]) -> int:
    # TODO - you fill in here.
    if len(citations) == 0:
        return 0
    # 일단 정렬부터 시킨다.
    citations.sort()
    # 1~max 값 사이를 이진탐색으로 search하며,
    s,e = 1, max(citations)
    # len(citations) - bisect pos 이 이진탐색에 사용된 값보다 크다면 값을 늘리고,
    ans = 0
    while s <= e:
        m = (s+e)//2
        pos = bi.bisect_left(citations, m)
        if len(citations) - pos >= m:
            s = m+1
            ans = m
        else:
            e = m-1
    # 아니라면 값을 줄인다.
    return ans


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
