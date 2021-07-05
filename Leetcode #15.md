# **Leetcode #336 팰린드롬 페어**
### **팰린드롬이란?**
* 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장
* ex) '소주 만 병만 주소'


```python
# 팰린드롬을 브루트 포스로 계산
# 타임 아웃 발생
def palindromePairs(self, words):
    def is_palindrome(word):
        return word == word[::-1]
    
    output = []
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1 + word2):
                output.append([i, j])
        
        return output
```

슬라이싱 기능을 활용해 반대로 뒤집은 단어가 원래 단어와 일치하는지 확인하는 is_palindrome 함수로 모든 단어 조합을 확인하며, 팰린드롬을 만족하는 단어 순서쌍을 output에 append 한다.   
하지만, 이 풀이는 리트코드에서 타임아웃됨


```python
# 트라이 구현

# 트라이를 저장할 노드
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
        
        return node.word
```

이전 예제에서 구현해두었던 트라이 뼈대   
팰린드롬 판별을 위해 구조를 약간 바꿀 것이다.


```python
# 팰린드롬을 트라이 구조로 판별
def insert(self, index: int, word: str) -> None:
    node = self.root
    for i, char in enumerate(reversed(word)):
        ...
        node = node.children[char]
    node.word_id = index
```


```python
# 단어 존재 여부 찾기
result = []
...
while word:
    if node.word_id >= 0:
        ...
        result.append([index, node.word_id])
```
