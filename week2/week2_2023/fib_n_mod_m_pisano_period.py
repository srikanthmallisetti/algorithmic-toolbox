"""
Week 2 - Programming Challenge 2, Question 5
Implementing Efficient Algoithm for finding the Pisano Period
Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚).
"""

def get_fib_n_mod_m_pisano_period(n: int, m: int) -> int:
    fibs = [0, 1, 1]
    mods = [0, 1, 1]
    cont = True

    while cont:
        fibs.append(fibs[-1] + fibs[-2])
        mods.append(fibs[-1] % m)
        cont = mods[-3:] != [0, 1, 1]
    
    return mods[n % len(mods[:-3])]


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(get_fib_n_mod_m_pisano_period(n, m))
