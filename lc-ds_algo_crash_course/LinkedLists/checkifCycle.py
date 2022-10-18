"""
Given a Linked List determine if the Linked List has a Cycle
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


if __name__ == "__main__":
    a = ListNode(5)
    b = ListNode(6)
    c = ListNode(7)
    d = ListNode(8)
    e = ListNode(9)
    f = ListNode(10)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # f.next = c
    start = a

    print(has_cycle(start))
