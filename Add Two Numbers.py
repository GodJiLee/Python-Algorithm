# 자료형 변환 풀이
class Solution:
    # Reverse Linked List
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
    # from Linked List to Python List
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next
        return list

    # from Python List to Linked List
    def toReversedLinkedList(self, result: str) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    # add two linked list
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        # return result
        return self.toReversedLinkedList(str(resultStr))

# 2. Full Adder
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum = 0
        # calculate sum of two input value
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        # divmod
        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next

# map
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
''.join(str(e) for e in a)
''.join(map(str, a))

resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
resultStr = int(''.join(map(str, a))) + int(''.join(map(str, b)))
resultStr

# functool high-order function
import functools
functools.reduce(lambda x, y: 10 * x + y, a, 0)

# using operator module
from operator import add, mul
functools.reduce(add, [1, 2, 3, 4, 5])
functools.reduce(mul, [1, 2, 3, 4, 5])
