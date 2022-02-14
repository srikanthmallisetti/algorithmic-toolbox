# python3

"""
Implement an Algorithm to
efficiently compute the Fibonacci number for input n
where 0 <= n <= 45
"""


def fibonacci_small(n: int) -> int:
    __int, _int = 0, 1
    if n == 0:
        return 0
    for i in range(2, n+1):
        int_ = _int + __int
        __int = _int
        _int = int_
    return _int


if __name__ == '__main__':
    print(fibonacci_small(int(input())))

