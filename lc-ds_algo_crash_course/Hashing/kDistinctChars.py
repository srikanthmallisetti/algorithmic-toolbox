"""
Example 1: You are given a string s and an integer k.
Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
"""

from collections import defaultdict


def get_max_len(s: str, k: int) -> int:
    char_map = defaultdict(int)
    left = ans = 0

    for right in range(len(s)):
        char_map[s[right]] += 1

        while len(char_map) > 2:
            char_map[s[left]] -= 1
            if char_map[s[left]] == 0:
                del char_map[s[left]]
            left += 1
        ans = max(ans, right - left + 1)

    return ans


if __name__ == "__main__":
    print(get_max_len("eceba", 2))
