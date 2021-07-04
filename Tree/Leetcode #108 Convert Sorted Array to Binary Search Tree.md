# Leetcode #108 정렬된 배열의 이진 탐색 트리 변환


```python
def sortedArrayToBST():
    if not nums:
        return None
    
    mid = len(nums) // 2 # 내림값 리턴
    
    #분할 정복으로 구현
    node = TreeNode(num[mid]) # 중앙에 있는 값들 차례로 할당
    node.left = self.sortedArraryToBST(nums[:mid]) # 오름차순 정렬이므로 작은 값
    node.right = self.sortedArrayToBST(nums[mid + 1:]) # 오름차순 정렬이므로 큰 값
    
    return node
```


```python

```
