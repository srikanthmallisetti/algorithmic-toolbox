# python3

"""
Implementation of Euclidean GCD -

It doesn't matter if a > b or vice-versa -
    It will only result in one more iteration during recursion to set the a and b positions right

Since, a % b = a' (if a > b) and a % b = a (if b > a)
If b > a: it will result in GCD(b, a), since a' is actually a: if b > a
"""


def euclidean_gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return euclidean_gcd(b, a % b)


if __name__ == '__main__':
    i1, i2 = map(int, input().split())
    print(euclidean_gcd(i1, i2))
