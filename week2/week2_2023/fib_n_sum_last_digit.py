"""
Week 2 - Programming Challenge 2, Question 6
Implementing Efficient Algoithm for finding the last digit of the sum of n Fibonacci numbers
Given an integer 𝑛, find the last digit of the sum 𝐹0 + 𝐹1 + · · · + 𝐹𝑛..
Intuition: the last digit of sum of n Fibonacci numbers = (F((n + 2) mod 60) - 1) mod 10
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

if __name__ == "__main__":
    num = int(input())
    print(find_fib_n_sum_mod_10(num))


