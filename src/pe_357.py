import math
import time


N_RANGE = 100_000_000


def get_prime_sieve(n_range):
    sieve = [True] * (n_range + 1)

    i = 2
    while i * i <= n_range:
        if sieve[i]:
            for multiple in range(i * 2, n_range+1, i):
                sieve[multiple] = False
        i += 1

    sieve[0] = False
    sieve[1] = False
    return sieve


def add_to_sum(n, prime_sieve):
    if not prime_sieve[int(1 + n)]:
        return False

    # iterate through divisors and return early if there is a non prime
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:

            if not prime_sieve[int(i + n / i)]:
                return False
            upper_d = int(n / i)
            if not prime_sieve[int(upper_d + n / upper_d)]:
                return False
    return True


def solve():
    result = 0
    prime_sieve = get_prime_sieve(N_RANGE)
    for n in range(1, N_RANGE):
        if add_to_sum(n, prime_sieve):
            result += n

    print(f'sum: {result}')


if __name__ == '__main__':
    start = time.time()
    solve()
    end = time.time()
    print(f'time: {(end - start)} seconds')


