# python3

def euclidean_gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return euclidean_gcd(b, a % b)


if __name__ == '__main__':
    i1, i2 = map(int, input().split())
    print(euclidean_gcd(i1, i2))
