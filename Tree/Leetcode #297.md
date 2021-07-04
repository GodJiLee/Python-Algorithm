# Leetcode #297 이진트리 직렬화 & 역직렬화


```python
# 직렬화
def serialize(self, root: TreeNode) -> str:
    queue = collections.deque([(root)])
    result = ['#']
    
    while queue:
        node = queue.popleft()
        if node:
            queue.append(node.left)
            queue.append(node.right)
            
            result.append(str(node.val))
            
        else:
            result.append('#')
            
    return result
```


```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
```


```python
import collections
```


```python
root = TreeNode(['#', 'A', 'B', 'C', '#', '#', 'D', 'E'])
queue = collections.deque([(root)])
```


```python
node = queue.popleft()
```


```python
node.left, node.right = node.right, node.left
```


```python
queue.append(node.left)
queue.append(node.right)
```


```python
root
```




    <__main__.TreeNode at 0x1acedae0490>




```python
queue
```




    deque([None, None])




```python
# 역직렬화
def deserialize(self, data: str) -> TreeNode:
    nodes = data.split()
    
    root = TreeNode(int(node[1]))
    queue = collections.deque([root])
    ...
```


```python
# 전체
class Codec:
    # 직렬화
    def serialize(self, root: TreeNode) -> str:
        queue = collections.deque([root])
        result = ['#']
        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                
                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)
    
    # 역직렬화
    def deserialize(self, data: str) -> TreeNode:
        # 예외 처리
        if data == '# #':
            return None
        
        nodes = data.split()
        
        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        # 빠른 런너처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1
            
            if nodes[index] is not '#':
                node.right = Treenode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root
```
