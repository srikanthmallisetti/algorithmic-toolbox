"""
Reversing a Linked List
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def rev_l_list(head: ListNode) -> ListNode:
    ptr = head
    prev = None

    while ptr:
        next_ = ptr.next
        ptr.next = prev
        prev = ptr
        ptr = next_
    return prev
