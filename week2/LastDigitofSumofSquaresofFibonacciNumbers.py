# python3

"""
The last digit of the sum of squares of n Fibonacci numbers
is the (last digit of the nth Fibonacci number *
last digit of the (n+1)th Fibonacci number) % 10
"""


def last_dig_sum_squares_fib(n):
    if n == 0:
        return 0
    fib_limit = (n % 60) + 1
    fibs, i = [0, 1, 1], 2
    while i < fib_limit:
        fibs.append((fibs[-1] + fibs[-2]))
        i += 1
    return ((fibs[fib_limit] % 10) * (fibs[fib_limit - 1] % 10)) % 10


if __name__ == "__main__":
    k = int(input())
    print(last_dig_sum_squares_fib(k))
