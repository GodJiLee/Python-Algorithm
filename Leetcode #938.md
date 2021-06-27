# Leetcode #938 이진 탐색 트리(BST) 합의 범위


```python
# 재귀구조 DFS로 브루트 포스 탐색
def rangeSumGST(self, root, L, R):
    if not root:
        return 0
    
    return (root.val if L <= root.val <= R else 0) + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)
```


```python
# DFS 가지치기로 필요한 노드 탐색 (최적화)
def rangeSumBST(self, root, L, R):
    def dfs(node: TreeNode):
        if not node:
            return 0
        
        if node.val < L: # 최솟값보다 작으면 오른쪽,
            return dfs(node.right)
        elif node.val > R: # 최댓값보다 크면 왼쪽으로
            return dfs(node.left)
        
        return node.val + dfs(node.left) + dfs(node.right)
```


```python
# 재귀구조를 반복구조로 변환
def rangeSumBST(self, root, L, R):
    stack, sum = [root], 0
    # 스택 이용 필요한 노드 DFS 반복
    while stack:
        node = stack.pop()
        if node:
            if node.val > L:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
            if L <= node.val <= R:
                sum += node.val
    
    return sum
```


```python
# 반복 구조 BFS로 필요한 노드 탐색
def rangeSumBST(self, root, L, R):
    stack, sum = [root], 0
    # 큐 연산을 이용해 반복 구조 BFS로 필요한 노드 탐색
    while stack:
        node = stack.pop(0) # Queue 연산
        if node:
            if node.val > L:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
            if L <= node.val <= R:
                sum += node.val
    
    return sum
```


```python

```
