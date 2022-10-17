"""
Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit,
return a boolean array that represents the answer to each query.
A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2] and queries = [[0, 3], [2, 5], [2, 4]] and limit = 13,
the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].
"""


def prefix_sum(nums: list[int], queries: list[list[int, int]], limit: int) -> list[bool]:
    sum_arr = []
    running_sum = 0
    for i in nums:
        running_sum += i
        sum_arr.append(running_sum)

    return [True if (sum_arr[x[-1]] - sum_arr[x[0]] + nums[x[0]]) < limit else False for x in queries]


if __name__ == "__main__":
    print(prefix_sum([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13))
