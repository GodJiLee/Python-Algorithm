# 1
def swapPairs(self, head: ListNode) -> ListNode:
    cur = head

    while cur and cur.next:
        # exchange only value
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head

# 2 Using iterative structure
b = a.next
a.next = b.next
b.next = a

prev.next = b
a = a.next
prev = prev.next.next

def swapPairs(self, head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head

    while head and head.next:
        # append for b to point out a(head)
        b = head.next
        head.next = b.next
        b.next = head

        # append for prev to point out b
        prev.next = b

        # move for the next comparison
        head = head.next
        prev = prev.next.next

    return root.next

# Using recursive structure for swap
def swapPairs(self, head: ListNode) -> ListNode:
    if head and head.next:
        p = head.next
        # return swapped value
        head.next = self.swapPairs(p.next)
        p.next = head
        return p
    return head
