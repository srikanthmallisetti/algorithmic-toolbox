"""
You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.

Input: nums = [10,4,-8,7]
Output: 2
Explanation:
There are three ways of splitting nums into two non-empty parts:
- Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7],
    and its sum is 3. Since 10 >= 3, i = 0 is a valid split.
- Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7],
    and its sum is -1. Since 14 >= -1, i = 1 is a valid split.
- Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7],
    and its sum is 7. Since 6 < 7, i = 2 is not a valid split.
Thus, the number of valid splits in nums is 2.

Input: nums = [2,3,1,0]
Output: 2
Explanation:
There are two valid splits in nums:
- Split nums at index 1. Then, the first part is [2,3], and its sum is 5. The second part is [1,0],
    and its sum is 1. Since 5 >= 1, i = 1 is a valid split.
- Split nums at index 2. Then, the first part is [2,3,1], and its sum is 6. The second part is [0],
    and its sum is 0. Since 6 >= 0, i = 2 is a valid split.
"""


def num_ways_to_split(nums: list[int]) -> int:
    prefix_sum = []
    curr_sum = 0
    valid_split = 0
    for num in nums:
        curr_sum += num
        prefix_sum.append(curr_sum)

    for s in range(len(prefix_sum) - 1):
        if prefix_sum[s] >= prefix_sum[-1] - prefix_sum[s]:
            valid_split += 1
    return valid_split


if __name__ == "__main__":
    print(num_ways_to_split([6, -1, 9]))

    print(num_ways_to_split([10, 4, -8, 7]))
