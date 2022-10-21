"""
Given an integer array arr, count how many elements x there are,
such that x + 1 is also in arr. If there are duplicates in arr, count them separately.
"""


def count_ele(nums: list[int]) -> int:
    ans = 0
    num_map = {}
    for num in nums:
        num_map[num] = num_map.get(num, 0) + 1

    for num in num_map:
        if num + 1 in num_map:
            ans += num_map[num]

    return ans


if __name__ == "__main__":
    print(count_ele([-2, -1]))
