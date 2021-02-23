# 1. using linked likst
# initiation
def __init__(self, k: int):
    self.head, self.tail = ListNode(None), ListNode(None) # left, right index
    self.k, self.len = k, 0 # maxlen, current length
    self.head.right, self.tail.left = self.tail, self.head

# internal function
def _add(self, node: ListNode, new: ListNode):
    n = node.right
    node.right = new
    new.left, new.right = node, n
    n.left = new

def _del(self, node: ListNode):
    n = node.right.right
    node.right = n
    n.left = node

# insert front
def insertFront(self, value: int) -> bool:
    if self.len == self.k: # current length == maxlen
        return False
    self.len += 1
    self._add(self.head, ListNode(value)) # insert node into head (left)
    return True

# insert last
def insertLast(self, value: int) -> bool:
    if self.len == self.k:
        return False
    self.len += 1
    self._add(self.tail.left, ListNode(value))
    return True

# delete
def deleteFront(self) -> bool:
    if self.len == 0:
        return False
    self.len -= 1 # delete
    self._del(self.head)

# explanation
# _del 함수를 사용해서 데크의 맨 앞(head)을 왼쪽으로 한 칸 밀고
# 전체 길이를 1 줄여줌

def deleteLast(self) -> bool:
    if self.len == 0:
        return False
    self.len -= 1
    self._del(self.tail.left.left)
    return True

# explanation
# 맨 마지막 값의 2 index 전 값을 _del 함수에 넣어
# 마지막 값을 빈 값으로 만들어주고 전체 길이를 1 줄여줌

def getFront(self) -> int:
    return self.head.right.val if self.len else -1

def getRear(self) -> int:
    return self.tail.left.val if self.len else -1

def isEmpty(self) -> bool:
    return self.len == 0

def isFull(self) -> bool:
    return self.len == self.k