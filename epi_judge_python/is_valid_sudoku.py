from typing import List

from test_framework import generic_test
from collections import defaultdict


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    r_dict, c_dict, s_dict = defaultdict(set), defaultdict(set), defaultdict(set)
    rows, cols = len(partial_assignment), len(partial_assignment[0])
    mul_ = 0
    for row in range(rows):
        if row % 3 == 0:
            mul_ = row
        for col in range(cols):
            value = partial_assignment[row][col]
            if value != 0:
                if (value in r_dict[row]) or (value in c_dict[col]) or (value in s_dict[mul_ + col // 3]):
                    return False
                r_dict[row].add(value)
                c_dict[col].add(value)
                s_dict[mul_ + col // 3].add(value)

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
