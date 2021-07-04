# Leetcode #226 이진 트리 반전


```python
# 파이썬 다운 방식
def invertTree(self, root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root, left)
        return root
    return None
```


```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```


```python
root = [4,2,7,1,3,6,9]
```


```python
# 반복 구조로 BFS
def invertTree(self, root: TreeNode) -> TreeNode:
    queue = collections.deque([root])
    
    while queue:
        node = queue.popleft()
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left
            
            queue.append(node.left)
            queue.append(node.right)
        
    return root
```


```python
import collections
```


```python
a = collections.deque([root])
```


```python
print(a)
```

    deque([[4, 2, 7, 1, 3, 6, 9]])
    


```python
node = a.popleft()
```


```python
TreeNode(node).left, TreeNode(node).right = TreeNode(node).right, TreeNode(node).left
```


```python
a.append(7)
```


```python
a.append(2)
```


```python
print(a)
```

    deque([7, 2])
    


```python
# 반복 구조로 DFS
def invertTree(self, root: TreeNode) -> TreeNode:
    stack = collections.deque([root])
    
    while stack:
        node = stack.pop()
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left
            
            stack.append(node.left)
            stack.append(node.right)
            
    return root
```


```python
# 반복 구조로 DFS 후위 순회
def invertTree(self, root: TreeNode) -> TreeNode:
    stack = collections.deque([root])
    
    while stack:
        node = stack.pop()
        
        if node:
            stack.append(node.left)
            stack.append(node.right)
            
            node.left, node.right = node.right, node.left # 후위 순회
    
    return root
```


```python

```
