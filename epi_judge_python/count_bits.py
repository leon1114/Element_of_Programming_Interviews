from test_framework import generic_test


def count_bits(x: int) -> int:
    counts = 0
    while x:
        if x & 0x1:
            counts += 1
        x = x >> 1
    return counts


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
