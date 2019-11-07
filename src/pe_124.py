import math
import numpy as np
import time
from util import is_prime


N_RANGE = 100_000


def get_prime_factors(n):
    result = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if is_prime(i):
                result.add(i)

            upper_divisor = int(n / i)
            if is_prime(upper_divisor):
                result.add(upper_divisor)

    if is_prime(n):
        result.add(n)

    return list(result)


def rad(n):
    prime_factors = get_prime_factors(n)
    return np.prod(prime_factors)


def solve():
    results = []
    for n in range(1, N_RANGE + 1):
        results.append((n, rad(n)))

    # sort by rad(n) and then tie breaker is n
    sorted_results = sorted(results, key=lambda element: (element[1], element[0]))
    print(f'answer: {sorted_results[9_999][0]}')


if __name__ == '__main__':
    start = time.time()
    solve()
    end = time.time()
    print(f'time: {(end - start)}')
