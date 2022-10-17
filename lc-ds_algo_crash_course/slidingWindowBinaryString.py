"""
You are given a binary substring s (a string containing only "0" and "1").
An operation involves flipping a "0" into a "1".
What is the length of the longest substring containing only "1" after performing at most one operation?

For example, given s = "1101100111", the answer is 5. If you perform the operation at index 2,
the string becomes 1111100111
"""


def longest_sub_str(b: str) -> int:
    i = j = 0
    max_len = 0
    while i < len(b) and j < len(b):
        cnt = 0
        for e in b[i: j + 1]:
            if e == '0':
                cnt += 1

        if cnt > 1:
            i += 1
        else:
            if (j - i) + 1 > max_len:
                max_len = (j - i) + 1
            j += 1
    return max_len


if __name__ == "__main__":
    print(longest_sub_str("1101100111"))
