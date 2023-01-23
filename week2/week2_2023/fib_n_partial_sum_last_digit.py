"""
Week 2 - Programming Challenge 2, Question 7
Implementing Efficient Algoithm for finding the last digit of the partial sum of n Fibonacci numbers
Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛, find the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 +· · · + 𝐹𝑛
"""


def find_fib_n_sum_mod_10(n: int) -> int:
    fibs = [0, 1, 1]
    itr_limit = (n + 2) % 60
    itr = 2
    while itr < itr_limit:
        fibs.append(fibs[-1] + fibs[-2])
        itr += 1
        fibs.pop(0)
    return ((fibs[-1] % 10) - 1) % 10


def find_fib_n_partial_sum_last_digit(m: int, n: int) -> int:
    return (find_fib_n_sum_mod_10(n) - find_fib_n_sum_mod_10(m-1)) % 10


if __name__ == "__main__":
    num_m, num_n, *_ = map(int, input().split())
    print(find_fib_n_partial_sum_last_digit(num_m, num_n))

    # for i in range(20):
    #     print(find_fib_n_mod_10(i))
