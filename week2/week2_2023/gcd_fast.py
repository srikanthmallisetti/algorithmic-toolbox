"""
Week 2 - Programming Challenge 2, Question 3
Implementing Efficient Algoithm for finding the Greatest Common Divisor of the given two numbers
"""

def get_gcd(num_1: int, num_2:int) -> int:
    if num_2 == 0:
        return num_1

    return get_gcd(num_2, num_1 % num_2)


if __name__ == "__main__":
    a, b, *_ = map(int, input().split())
    print(get_gcd(a, b))
