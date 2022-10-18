"""
Given an array of positive integers nums and an integer k,
return the number of contiguous sub arrays
where the product of all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100,
the answer is 8. The sub arrays with products less than k are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
"""


# moving j iterator for sliding
def sub_arr_prod(arr: list[int], k: int) -> int:
    i = j = 0
    sub_arr_cnt = 0
    while i < len(arr) and j < len(arr):
        curr_prod = 1
        for e in arr[i: j + 1]:
            curr_prod = curr_prod * e

        if curr_prod < k:
            sub_arr_cnt += len(arr[i: j + 1])
            j += 1
        else:
            i += 1
            if i > j:
                j = i
    return sub_arr_cnt


# LC solution
def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    ans = left = 0
    curr = 1
    for right in range(len(nums)):
        print("in-for, left, right", left, right)
        curr *= nums[right]
        print("curr ->", curr)
        while left <= right and curr >= k:
            print("in-while")
            curr //= nums[left]
            left += 1
            print("curr, left", curr, left)
        print("curr, left, right", curr, left, right)
        ans += right - left + 1
        print("ans ->", ans)
    return ans


if __name__ == "__main__":
    print(numSubarrayProductLessThanK([100, 115, 2, 6], 100))
    # print(numSubarrayProductLessThanK([25, 5, 4, 3, 2, 1, 1], 20))
