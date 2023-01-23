"""
Week 2 - Programming Challenge 2, Question 1
Implementing Efficient Algoithm for finding the nth Fibonacci Number
"""


def fast_fib(n: int) -> int:
    if n == 0:
        return 0

    fib_list = [0, 1]
    itr = 2

    while itr <= n:
        fib_list.append(fib_list[itr - 1] + fib_list[itr - 2])
        itr += 1

    return fib_list[n]


if __name__ == "__main__":
    fib_n = int(input())
    print(fast_fib(fib_n))

    # for i in range(100):
    #     print("{i}th Fibonacci Number: {fib_res}".format(i=i, fib_res=fast_fib(i)))
