# **트라이 (Trie)**
#### 겁색 트리의 일종, 키가 문자열인 동적 배열 또는 연관 배열을 저장하는데 사용되는 정렬된 트리 자료구조
* 자연어 처리(NLP) 분야에서 문자열 탐색시 자주 쓰임
* 전형적인 다진 트리 형태

## **Leetcode #208 트라이 구현**


```python
# 딕셔너리를 이용해 간결한 트라이 구현
class TrieNode: # 트라이를 저장할 노드
    def __init__(self):
        self.word = False
        self.children = {}
```


```python
class Trie: # 트라이 연산
    def __init__(self):
        self.root = TrieNode()
    
    # insert()
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode() # 다음 문자를 키로하는 자식노드 형태
            node = node.children[char]
        node.word = True
```


```python
# search()
def search(self, word: str) -> bool:
    node = self.root
    for char in word:
        if char not in node.children:
            return False
        
        node = node.children[char]
    
    return node.word
```


```python
# startsWith()
def startsWith(self, prefix: str) -> bool:
    node = self.root
    for char in prefix:
        if char not in node.children:
            return False
        
        node = node.children[char]
    
    return True
```


```python
import collections
```


```python
# 트라이의 노드
class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode) # keyerror 방지
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    # 단어 삽입
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            node = node.children[char]
        
        node.word = True
        
    # 단어 존재 여부 판별
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.word # 마지막 단어까지 있으면 True 반환
    
    # 문자열로 시작 단어 존재 여부 판별
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
            
        return True # prefix가 모두 존재하면 True 반환
```

self.children을 defaultdict() 자료형으로 선언하여 if문으로 확인하는 작업 생략 가능
