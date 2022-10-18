"""
Example 3: Given the head of a linked list and an integer k, return the k^{th}k
th
  node from the end.

For example, given the linked list that represents 1 -> 2 -> 3 -> 4 -> 5 and k = 2,
return the node with value 4, as it is the 2nd node from the end.
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def get_k_from_end(head, k):
    fast = head
    slow = head

    for _ in range(k):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    return slow.val


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # f.next = c
    start = a

    print(get_k_from_end(start, 3))
