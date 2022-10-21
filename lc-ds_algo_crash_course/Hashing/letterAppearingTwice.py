"""
Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:
A letter 'a' appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
s will contain at least one letter that appears twice.
"""


def get_rep_char(s: str) -> str:
    s = list(s)
    ctr = 0
    str_map = {}
    ans = ""

    while ctr < len(s):
        if s[ctr] in str_map:
            return s[ctr]

        str_map[s[ctr]] = ctr
        ctr += 1

    return ans


if __name__ == "__main__":
    print(get_rep_char("acabab"))
