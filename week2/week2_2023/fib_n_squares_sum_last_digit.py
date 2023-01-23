"""
Week 2 - Programming Challenge 2, Question 8
Implementing Efficient Algoithm for finding the last digit of the sum of squares of n Fibonacci numbers
Compute the last digit of 𝐹0 ** 2 + 𝐹1 ** 2 + · · · + 𝐹𝑛 ** 2.
"""

def find_fib_n_squares_sum_last_digit(n: int) -> int:
    if n == 0:
        return 0
    fib_limit = (n % 60) + 1
    fibs, i = [0, 1, 1], 2
    while i < fib_limit:
        fibs.append((fibs[-1] + fibs[-2]))
        i += 1
    return ((fibs[fib_limit] % 10) * (fibs[fib_limit - 1] % 10)) % 10


if __name__ == "__main__":
    num_n = int(input())
    print(find_fib_n_squares_sum_last_digit(num_n))
