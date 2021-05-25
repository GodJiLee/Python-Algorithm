# Leetcode #617 두 이진트리 병합


```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```


```python
# 재귀 탐색
def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        
        return node # 후위 순회
    else:
        return t1 or t2
```


```python

```
