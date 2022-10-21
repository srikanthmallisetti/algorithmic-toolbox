"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Constraints:

n == nums. Length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
"""


def missing_num(nums: list[int]) -> int:
    return sum(range(len(nums) + 1)) - sum(nums)


if __name__ == "__main__":
    print(missing_num([9, 6, 4, 2, 3, 5, 7, 0, 1]))
