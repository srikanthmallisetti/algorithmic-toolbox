# python3

"""
For a very large value n, find Fn modulo m
Fn modulo m is known as Pisano period, and always start with 011
"""


def fib_again(n, m):
    res = 1
    mods = [0, 1, 1]
    fibs = [0, 1, 1]
    while res <= 2:
        fibs.append(fibs[-1] + fibs[-2])
        mods.append(fibs[-1] % m)
        if mods[-3:] == [0, 1, 1]:
            res += 2
    return mods[n % len(mods[:-3])]


if __name__ == '__main__':
    i1, i2 = map(int, input().split())
    print(fib_again(i1, i2))
