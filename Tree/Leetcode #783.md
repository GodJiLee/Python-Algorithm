# Leetcode #783 이진 탐색 트리(BST) 노드 간 최소 거리


```python
# 중위 순회 뼈대
def f():
    if root.left:
        f(root.left)
    
    result = min()
    
    if root.right:
        f(root.right)
```


```python
import sys

class Solution:
    prev = -sys.maxsize # 클래스 멤버 변수 
    result = sys.maxsize
    
    # 재귀 구조 중위 순회 비교 결과
    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)
            
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        
        if root.right:
            self.minDiffInBST(root.right)
            
        return self.result
```


```python
# 반복 구조로 중위 순회
def minDiffInBST(self, root):
    prev = -sys.maxsize # 클래스 변수 사용하지 않음
    result = sys.maxsize
    
    stack = [] # LIFO
    node = root
    
    # 반복 구조 중위 순회 비교 결과
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        
        node = stack.pop()
        
        result = min(result, node.val - prev)
        prev = node.val
        
        node = node.right
        
    return result
```


```python

```
