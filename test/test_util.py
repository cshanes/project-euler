import pytest
from util import is_prime


def test_is_prime_under_100():
    primes_under_100 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    all_ints_under_100 = range(1, 100)
    for n in all_ints_under_100:
        if n in primes_under_100:
            assert(is_prime(n) is True)
        else:
            assert(is_prime(n) is False)
