from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    # Sieve of Eratosthenes Implementations
    primes = []
    is_prime = [1] * (n+1)
    for i in range(2, n+1):
        if is_prime[i] == 0:
            continue
        primes.append(i)
        for j in range(i + i, n+1, i):
            is_prime[j] = 0

    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
