# Leetcode #687 가장 긴 동일 값의 경로


```python
# 상태값 거리 계산 DFS
class Solution:
    result: int = 0
    
    def longestUnivaluePath(self, root):
        def dfs(node):
            if node is None:
                return 0
            
            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 동일값 판별 (부모노드 - 자식노드)
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽, 오른쪽 노드의 거리의 합
            self.result = max(self.result, left + right)
            
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)
        
        dfs(root)
        return self.result
```


```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
         self.right = right
```


```python
root = TreeNode([5, 4, 5, 1, 1, 5])
```


```python
type(root)
```




    __main__.TreeNode


