import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'w', 'h'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    def is_intercept(r1: Rect, r2: Rect) -> bool:
        return (r1.x <= r2.x + r2.w) and \
        (r1.x + r1.w >= r2.x) and \
        (r1.y <= r2.y + r2.h) and \
        (r1.y + r1.h >= r2.y)
    # TODO - you fill in here.
    if not is_intercept(r1,r2):
        return Rect(0,0,-1,-1)
    return Rect(max(r1.x, r2.x), \
			max(r1.y, r2.y), \
			min(r1.x + r1.w, r2.x + r2.w) - max(r1.x, r2.x),\
			min(r1.y + r1.h, r2.y + r2.h) - max(r1.y, r2.y))


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
