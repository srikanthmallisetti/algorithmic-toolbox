# python3

"""
The last digit of sum of first n Fibonacci numbers
is the (last digit of (n + 2)th Fibonacci number) - 1
=> last digit of nth Fibonacci number is (((n + 2) mod 60)th Fibonacci number %10 )
"""


def last_dig_sum_fib(n):
    fib_limit = (n + 2) % 60
    fibs = [0, 1, 1]
    i = 2
    while i < fib_limit:
        fibs.append((fibs[-1] + fibs[-2]))
        i += 1
        fibs.pop(0)
    return ((fibs[-1] % 10) - 1) % 10


if __name__ == '__main__':
    k = int(input())
    print(last_dig_sum_fib(k))
