"""
Given two strings: s, t
return True if s is subsequence of t
else False
"""


def is_sub_seq(s, t):
    i = j = 0
    while i < len(s) and j < len(t):
        if t[j] == s[i]:
            i += 1
        else:
            i = 0
        j += 1

    return i == len(s)


if __name__ == '__main__':
    sub_str = "ca"
    big_str = "racecar"

    print(is_sub_seq(sub_str, big_str))

