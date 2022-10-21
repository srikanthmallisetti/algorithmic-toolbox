"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def dedup(head: ListNode) -> ListNode:
    ptr = head

    while ptr and ptr.next:
        prev = ptr
        ptr = ptr.next

        if ptr.val == prev.val:
            prev.next = ptr.next
            ptr = prev

    return head

