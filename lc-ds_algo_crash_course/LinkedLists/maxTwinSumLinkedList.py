"""
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as
the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2.
These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


# def max_pair_wise_sum(head: ListNode) -> int:


if __name__ == "__main__":
    a = ListNode(5)
    b = ListNode(4)
    c = ListNode(2)
    d = ListNode(1)

    a.next = b
    b.next = c
    c.next = d

    # print(max_pair_wise_sum(a))



