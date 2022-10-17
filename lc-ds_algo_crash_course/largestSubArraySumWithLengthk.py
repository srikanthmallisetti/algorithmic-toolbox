"""
Example 4: Given an integer array nums and an integer k,
find the sum of the subarray with the largest sum whose length is k.
"""


def find_best_aub_arr(arr: list[int], k: int) -> int:
    curr = 0
    for i in range(k):
        curr += arr[i]
    ans = curr

    for i in range(k, len(arr)):
        curr += arr[i] - arr[i - k]
        ans = max(ans, curr)

    return ans


if __name__ == "__main__":
    print(find_best_aub_arr(list(range(100)), 10))
