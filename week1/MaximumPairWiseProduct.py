# python3


def max_pair_wise_product_fast(nums: list) -> int:
    n = len(nums)

    max_index = -1
    i = 0
    while i < n:
        if (max_index == -1) or (nums[i] > nums[max_index]):
            max_index = i
        i += 1

    max_index2 = -1
    j = 0
    while j < n:
        if (j != max_index) and ((max_index2 == -1) or (nums[j] > nums[max_index2])):
            max_index2 = j
        j += 1

    return nums[max_index] * nums[max_index2]


if __name__ == '__main__':
    num_len = int(input())
    nums_list = map(int, input().split())
    print(max_pair_wise_product_fast(list(nums_list)))

    # stress testing
    # import random
    # while True:
    #     test_data = random.sample(range(2, 100000), 9999)
    #     print(max_pair_wise_product_fast(test_data))
