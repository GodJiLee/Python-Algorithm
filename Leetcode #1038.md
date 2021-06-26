# Leecode #1038 이진탐색트리(BST)를 더 큰 수의 합계 트리로


```python
class Solution:
    val: int = 0 # 클래스 멤버 변수 초기화
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중회 순회 노드 값 누적
        if root: 
            self.bstToGst(root.right)
            self.val += root.val # 누적된 값
            root.val = self.val # 현재 노드
            self.bstToGst(root.left)
            
        return root
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-0e75f1ac7970> in <module>
    ----> 1 class Solution:
          2     val: int = 0 # 클래스 멤버 변수 초기화
          3 
          4     def bstToGst(self, root: TreeNode) -> TreeNode:
          5         # 중회 순회 노드 값 누적
    

    <ipython-input-3-0e75f1ac7970> in Solution()
          2     val: int = 0 # 클래스 멤버 변수 초기화
          3 
    ----> 4     def bstToGst(self, root: TreeNode) -> TreeNode:
          5         # 중회 순회 노드 값 누적
          6         if root:
    

    NameError: name 'TreeNode' is not defined



```python

```
