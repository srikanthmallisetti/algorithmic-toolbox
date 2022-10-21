"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes

(i.e., only nodes themselves may be changed.)
"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def swap_nodes_in_pairs(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    prev = None
    ptr = head
    dummy = ptr.next

    while ptr and ptr.next:
        if prev:
            prev.next = ptr.next

        next_ = ptr.next
        prev = ptr
        next_ = next_.next

        ptr = ptr.next
        prev.next = next_
        ptr.next = prev

        ptr = next_

    return dummy
