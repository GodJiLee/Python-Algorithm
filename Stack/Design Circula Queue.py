# 1. embody by array
# initiation
def __init__(self, k:int):
    self.q = [None] * k # make array
    self.maxlen = k
    self.p1 = 0 # front pointer
    self.p2 = 0 # rear pointer

# enter # move rear pointer
def enQueue(self, value: int) -> bool:
    if self.q(self.p2) is None:
        self.q[self.p2] = value
        self.p2 = (self.p2 + 1) % self.maxlen
    else:
        return False


# sudo code
def Enqueue(Q, x):
    Q[Q.tail] = x
    if Q.tail == Q.length:
        Q.tail = 1
    else:
        Q.tail = Q.tail + 1

def Dequeue(Q):
    x = Q[Q.head]
    if Q.head = Q.length:
        Q.head = 1
    else:
        Q.head += 1
    return x

# Only delete # move front pointer
def deQueue(self) -> bool:
    if self.q[self.p1] is None:
        return False
    else:
        self.q[self.p1] = None
        self.p1 = (self.p1 + 1) % self.maxlen
        return True

# front peek
def Front(self) -> int:
    return -1 if self.q[self.p1] is None else self.q[self.p1]

# rear peek
def Rear(self) -> int:
    return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

# empty or not
def isEmpty(self) -> bool:
    return self.p1 == self.p2 and self.q[self.p1] is None

# full or not
def isFull(self) -> bool:
    return self.p1 == self.p2 and self.q[self.p] is not None
