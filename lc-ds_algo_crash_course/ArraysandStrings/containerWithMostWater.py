"""
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Hint: Area of the container is length * width
"""


def max_area(height: list[int]) -> int:
    i = 0
    j = len(height) - 1
    area = 0
    while i < j:
        width_w = j - i
        if height[i] < height[j]:
            len_l = height[i]
            i += 1
        else:
            len_l = height[j]
            j -= 1
        curr_area = len_l * width_w

        if curr_area > area:
            area = curr_area
    return area


if __name__ == '__main__':
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
