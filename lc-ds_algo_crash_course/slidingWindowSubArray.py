"""
Given an Array
Return the length of the longest subarray
with a sum less than or equal to k
"""


def sliding_arr(arr, k):
    i = j = 0
    max_len = 0
    while i < len(arr) and j < len(arr):
        curr_sum = 0
        for e in arr[i: j + 1]:
            curr_sum += e

        if curr_sum > k:
            i += 1
        else:
            if (j - i) + 1 > max_len:
                max_len = (j - i) + 1
            j += 1

    return max_len


if __name__ == "__main__":
    print(sliding_arr([7, 2, 4, 1, 3, 6], 10))
