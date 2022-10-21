"""
Given an array of integers nums and an integer target,

return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


def get_target_sum(nums: list[int], target: int) -> list[int]:
    num_hash = {}
    ctr = 0
    ans = []

    while ctr < len(nums):
        comp = target - nums[ctr]

        if comp in num_hash:
            return [ctr, num_hash[comp]]

        num_hash[nums[ctr]] = ctr
        ctr += 1
    return ans


if __name__ == "__main__":
    print(get_target_sum([-1, 0], -1))
