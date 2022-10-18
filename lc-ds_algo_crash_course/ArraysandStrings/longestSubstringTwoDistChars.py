"""
Given a string s, return the length of the longest substring that contains at most two distinct characters.

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.
"""


def longest_substr(s: str) -> int:
    n = len(s)

    if n < 3:
        return n

    left = 0
    max_len = 2
    char_map = {}

    for right in range(n):
        char_map[s[right]] = right

        if len(char_map) == 3:
            del_val = min(char_map.values())
            char_map = {k: v for k, v in char_map.items() if v != del_val}
            left = del_val + 1
        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    print(longest_substr("cdaba"))
    print(longest_substr("ccaabbb"))
