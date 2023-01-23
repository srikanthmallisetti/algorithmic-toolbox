"""
Week 2 - Programming Challenge 2, Question 4
Implementing Efficient Algoithm for finding the Least Common Multiple of the given two numbers
Intuition: The LCM of two numbers is the quotient_of(their_product / GCD(those_num))
Ex: LCM(4, 8) = (4 * 8) // 2 (where 2 = GCD(4, 8))
"""


def get_gcd(num_1: int, num_2: int) -> int:
    if num_2 == 0:
        return num_1

    return get_gcd(num_2, num_1 % num_2)


def get_lcm(num_1: int, num_2: int) -> int:
    if 0 in [num_1, num_1]:
        return 0
    
    return (num_1 * num_2) // get_gcd(num_1, num_2)

if __name__ == "__main__":
    a, b, *_ = map(int, input().split())
    print(get_lcm(a, b))
