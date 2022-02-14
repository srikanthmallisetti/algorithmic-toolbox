# python3

"""
Implement an Algorithm to
efficiently compute the Least Common Multiple of two input non-zero integers a,b
where 0 <= a,b <= 10 ** 7
"""


def least_common_multiple(a: int, b: int) -> int:
    prod = a * b
    gcd_arr = [(b, a % b)]
    while gcd_arr[-1][-1] != 0:
        gcd_arr.append((gcd_arr[-1][-1], gcd_arr[-1][0] % gcd_arr[-1][-1]))
        gcd_arr.pop(0)
    return int(prod/gcd_arr[-1][0])


if __name__ == '__main__':
    i1, i2 = map(int, input().split())
    print(least_common_multiple(i1, i2))

