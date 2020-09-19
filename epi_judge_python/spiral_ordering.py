from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
#     answer = []
#     dd = [
#         (0,1),
#         (1,0),
#         (0,-1),
#         (-1,0)
#     ]
#     dist, d, x, y = len(square_matrix), 0, -1, 0
#     while dist != 0:
#         dy, dx = dd[d]
#         for i in range(dist):
#             x,y = x + dx, y + dy
#             answer.append(square_matrix[y][x])
#         if d % 2 == 0:
#             dist -= 1
#         d = (d + 1) % 4
#     return answer



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
