# python3

def FibonacciFast(n: int) -> int:
    if n == 0:
        return 0
    f_list = [0, 1]
    itr = 2
    while itr <= n:
        f_list.append((f_list[itr - 1] + f_list[itr - 2]))
        itr += 1
    return f_list[n]


if __name__ == '__main__':
    for x in range(46):
        print("{} -> {}".format(x, FibonacciFast(x)))
