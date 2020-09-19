from test_framework import generic_test


def reverse(x: int) -> int:
    lookup = list()
    for i in range(65536):
        reversed_bin = str(bin(i))[2:].zfill(16)[::-1]
        lookup.append(int('0b'+reversed_bin, 2))

    CACHE_LEN = 16
    MASK = 0xFFFF
    result = 0
    print(bin(x))
    for i in range(64//CACHE_LEN):
        result <<= CACHE_LEN
        shift = i * CACHE_LEN
        part = (x & (MASK << shift)) >> shift
        result += lookup[part]

    result_str = str(bin(result))[2:].strip("0")
    print("0b" + result_str)
    print(str(bin(1753863861)))
    return int("0b"+result_str, 2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))