"""
Given two sorted arrays: return an array
that combines both arrays and is sorted
"""


def combine_arrays(arr_1, arr_2):
    i = j = 0
    ans = []
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] < arr_2[j]:
            ans.append(arr_1[i])
            i += 1
        else:
            ans.append(arr_2[j])
            j += 1

    while i < len(arr_1):
        ans.append(arr_1[i])
        i += 1

    while j < len(arr_2):
        ans.append(arr_2[j])
        j += 1

    return ans


if __name__ == '__main__':
    first_arr = list(range(-5, 5))
    second_arr = list(range(-10, 0))

    print(combine_arrays(first_arr, second_arr))
