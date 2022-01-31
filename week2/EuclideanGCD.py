# python3

def euclidean_gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return euclidean_gcd(b, a % b)


if __name__ == '__main__':
    print(euclidean_gcd(357, 234))
