# python3

"""
The last digit of partial sum of Fibonacci numbers
for two integers m, n (m <= n) is
((the last digit of sum of n Fibonacci numbers) -
(the last digit of sum of m-1 Fibonacci numbers)) % 10
"""


def last_dig_partial_sum_fib(m, n):
    fib_limit_n = (n + 2) % 60
    fib_limit_m = (m + 1) % 60
    fibs, i = [0, 1, 1], 2
    itr = fib_limit_n
    if fib_limit_m > fib_limit_n:
        itr = fib_limit_m
    while i < itr:
        fibs.append((fibs[-1] + fibs[-2]))
        i += 1
    return ((fibs[fib_limit_n] % 10) - (fibs[fib_limit_m] % 10)) % 10


if __name__ == '__main__':
    k1, k2 = map(int, input().split())
    print(last_dig_partial_sum_fib(k1, k2))
