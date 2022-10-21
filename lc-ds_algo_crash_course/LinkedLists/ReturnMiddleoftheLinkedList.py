"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.


"""


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def get_middle_node(head: ListNode) -> ListNode:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if not fast:
        slow = slow.next

    return slow


