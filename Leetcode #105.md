# Leetcode #105 전위, 중위 순회 결과로 이진 트리 구축


```python
def buildTree(self, preorder, inorder):
    if inorder:
        # 전위 순회 결과는 중위 순회 분할의 인덱스
        index = inorder.index(preorder.pop(0)) # pop(0)는 왼쪽부터 pop (Queue)

        # 전위 순회의 첫 번째 노드를 트리의 분할 기점 노드로 잡아 left, right구성
        node = TreeNode(inorder[index])
        node.left = self.buildTree(preorder, inorder[0:index])
        node.right = self.buildTree(preorder, inorder[index + 1:])
        
        return node
```


```python

```
