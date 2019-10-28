import math
import time
from dataclasses import dataclass
# Consider the divisors of 30: 1,2,3,5,6,10,15,30.
# It can be seen that for every divisor d of 30, d+30/d is prime.
#
# Find the sum of all positive integers n not exceeding 100 000 000
# such that for every divisor d of n, d+n/d is prime.

MAX_PRIME_SEEN = 2
primes_seen = set()

# TODO: try running in reverse order from 100mil to 0
N_RANGE = 100_000_000
# N_RANGE = 1_000_000



# def add_to_sum(divisors, n, blah):
#     # getting uniques here before checking uses more memory but reduced compute time
#     uniques = set([int(d + n/d) for d in divisors])
#     # TODO: math way to get the unique set of (d + n/d) ?
#     for d in uniques:
#         if not is_prime(d):
#             return False
#     return True




# TODO: rearrange function defs to be in order as called

# TODO: maybe store divisors in an ordered dict?



class PE357:

    def __init__(self):
        self.computed_divisors = dict()
        self.primes_seen = set()
        self.non_primes = set()

    def add_to_sum(self, divisors, n):
        # getting uniques here before checking uses more memory but reduced compute time
        uniques = set([int(d + n / d) for d in divisors])
        # TODO: math way to get the unique set of (d + n/d) ?
        for d in uniques:
            if d in self.non_primes:
                return False

            if d in self.primes_seen:
                continue

            if not self.is_prime(d):
                self.non_primes.add(d)
                return False

            self.primes_seen.add(d)
        return True

    @staticmethod
    def is_prime(n):
        # use bitwise and to check if even
        if n <= 1 or not n & 1:
            return False

        i = 3
        while i ** 2 <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    @staticmethod
    def get_divisors(n):
        result = [1]
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                result += [i, int(n / i)]
        result += [n]
        return result

    def solve(self):
        result = 0
        for n in range(1, N_RANGE):
            divisors = self.get_divisors(n)
            if self.add_to_sum(divisors, n):
                print(f'adding: {n}')
                result += n

        print(f'sum: {result}')


if __name__ == '__main__':
    start = time.time()
    pe_357 = PE357()
    pe_357.solve()
    end = time.time()
    MAX_PRIME_SEEN = 2
    print(f'time: {(end - start)} seconds')


