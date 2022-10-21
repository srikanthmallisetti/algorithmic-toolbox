"""
Given an array of positive integers nums and an integer k.
Find the number of subarrays with exactly k odd numbers in them.

For example, given nums = [1, 1, 2, 1, 1], k = 3, the answer is 2.
The subarrays with 3 odd numbers in them are [1, 1, 2, 1,    1] and [1,     1, 2, 1, 1].
"""

from collections import defaultdict


# wrong
def num_sub_arr(nums: list[int], k: int) -> int:
    left = ans = 0
    num_map = defaultdict(int)

    for right in range(len(nums)):
        if nums[right] % 2 > 0:
            k -= 1
            num_map[nums[right]] += 1

        while k == 0:
            ans += 1
            if nums[left] % 2 > 0:
                k += 1
                num_map[nums[left]] -= 1
            left += 1

    return ans


if __name__ == "__main__":
    print(num_sub_arr([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
