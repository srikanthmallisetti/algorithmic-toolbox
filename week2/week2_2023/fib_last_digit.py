"""
Week 2 - Programming Challenge 2, Question 2
Implementing Efficient Algoithm for finding the last digit of nth Fibonacci Number
"""

def fib_last_digit(n: int) -> int:
    if n == 0:
        return 0
    
    fib_last_dig_list = [0, 1]
    itr = 2

    while itr <= n:
        fib_last_dig_list.append((fib_last_dig_list[-1] + fib_last_dig_list[-2]) % 10)
        itr += 1
        fib_last_dig_list.pop(0)
    
    return fib_last_dig_list[-1]

if __name__ == "__main__":
    fib_nth_n = int(input())
    print(fib_last_digit(fib_nth_n))

    # for i in range(100):
    #     print("The last digit of {i}th Fibonacci Number: {fn}".format(i=i, fn=fib_last_digit(i)))