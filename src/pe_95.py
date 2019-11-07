import math
import numpy as np
import time

N_RANGE = 1_000_000


def get_proper_divisors(n):
    result = {1}
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(int(n / i))

    return list(result)


def solve():
    longest_chain = {}
    for n in range(2, N_RANGE + 1):
        first_sum = np.sum(get_proper_divisors(n))
        next_sum = first_sum
        chain = set()
        while next_sum != first_sum or len(chain) == 0:
            if next_sum == 1 or next_sum > 1_000_000 or next_sum in chain:
                chain = {}
                break
            chain.add(next_sum)
            next_sum = np.sum(get_proper_divisors(next_sum))

        if len(chain) > len(longest_chain):
            longest_chain = chain

    print(f'smallest element of longest chain: {sorted(list(longest_chain))[0]}')


if __name__ == '__main__':
    start = time.time()
    solve()
    end = time.time()
    print(f'time: {(end - start)}')
