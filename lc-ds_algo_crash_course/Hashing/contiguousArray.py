"""
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
"""

from collections import defaultdict


def longest_sub_arr(nums: list[int]) -> int:
    left = ans = 0
    bin_map = defaultdict(int)

    for right in nums:
        bin_map[nums[right]] += 1

        if len(bin_map) == 2 and bin_map[0] == bin_map[1]:
            ans = max(ans, bin_map[0] + bin_map[1])
    return ans


if __name__ == "__main__":
    print(longest_sub_arr([0, 0, 0, 0, 1, 1, 1]))


