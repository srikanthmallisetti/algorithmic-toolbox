"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
"""


def max_avg_sub_arr(nums: list[int], k):
    curr = 0
    for i in range(k):
        curr += nums[i]
    ans = curr / k
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr / k)
    return ans


if __name__ == "__main__":
    print(max_avg_sub_arr([1, 12, -5, -6, 50, 3], 4))
