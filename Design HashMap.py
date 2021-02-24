class ListNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None

import collections

class MyHashMap:
    # initialization
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # insert
    def put(self, key: int, value: int) -> None:
        index = key % self.size # modulo calculation
        # insert key & value into the empty table
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

    # explanation
    # 조건을 self.table[index]가 아닌 value 값으로 조회한 이유는, self.table이 defaultdict 자료형
    # 이기 때문에 없는 인덱스를 조회해도 key, value값이 각각 None인 ListNode를  자동생성한다.

        # when node exists in the index, process using linked list
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value # update value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # inquiry
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is Nonde:
            return -1
        # when node exists
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # delete
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        # 1. remove first node
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 2. remove linked list node
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next