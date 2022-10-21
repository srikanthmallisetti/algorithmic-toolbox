"""
Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1.

"""

from collections import defaultdict


def largest_unique_num(nums: list[int]) -> int:
    num_map = defaultdict(int)
    ans = -1

    for num in nums:
        num_map[num] += 1

    while len(num_map):
        max_key = max(num_map.keys())
        if num_map[max_key] == 1:
            return max_key
        del num_map[max_key]
    return ans


if __name__ == "__main__":
    print(largest_unique_num([0]))
