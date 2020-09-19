from test_framework import generic_test
from math import floor, log10

def is_palindrome_number(x: int) -> bool:
    # TODO - you fill in here.
    if x <= 0:
        # log10(0) 이 들어가면 exception 이므로
        return x == 0
    num_digits = floor(log10(x)) + 1
    divisor = 10 ** (num_digits - 1)
    for _ in range(num_digits // 2):
        if x % 10 != x // divisor:
            return False
        x = x % divisor # MSB 제거
        x //= 10 # LSB 제거
        divisor //= 100 # 두 자리 뒤로 돌아감
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
