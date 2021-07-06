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
# 트라이 구현 (이전 예제 코드)

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
        
        return node.word # 마지막 글자가 마지막 노드인지 확인 (맞으면 True 반환)
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
    if node.word_id >= 0: # -1이 아니면 
        ...
        result.append([index, node.word_id])
```


```python
def insert(self, index: int, word: str) -> None:
    node = self.root
    for i, char in enumerate(reversed(word)):
        if self.is_palindrome(word[0:len(word) - i]): # python slicing 기능으로 뒤집은 단어와 동일한지 확인
            node.palindrome_word_ids.append(index) # palindrome일 때만 word_id에 index(p) append
        node = node.children[char]
    node.word_id = index
```

기존 Trie 연산 중 insert에 palindrome일 때 index를 추가하는 연산을 추가함


```python
# TrieNode 클래스도 수정
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []
```

word_id, palindrome_word_ids를 TrieNode 클래스의 속성값으로 추가함


```python
# 단어 자체가 palindrome인 경우
for palindrome_word_id in node.palindrome_word_ids:
    result.append([index, palindrome_word_id])
```


```python
# 3번째 판별 로직
while word:
    if node.word_id >= 0:
        if self.is_palindrome(word):
            result.append([index, node.word_id])
        ...
    node = node.children[word[0]]
    word = word[1:]
```

위의 세 가지 경우는 입력값을 각각 한 번씩만 대입해 풀 수 있으므로 시간복잡도 O(n) 안에 풀 수 있다. (정확히는 단어의 최대 길이 (k)에 대해, O(k^2*n))
- 앞서 풀이한 브루트 포스보다 훨씬 효율적


```python
# 전체 코드
import collections
# 트라이를 저장할 노드
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word_id = -1
        self.palindrome_word_ids = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    @staticmethod # 클래스와 독립적인 함수
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]
    
    # 단어 삽입
    def insert(self, index, word) -> None:
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[0:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
        node.word_id = index
        
    # 단어 판별
    def search(self, index, word):
        result = []
        node = self.root
        
        while word:
            # 판별 로직 3) 탐색 중간에 word_id가 있고, 나머지 문자가 팰린드롬인 경우
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    result.append([index, node.word_id])
            if not word[0] in node.children:
                return result
            node = node.children[word[0]]
            word = word[1:]
            
        # 판별 로직 1) 끝까지 탐색했을 때 word_id가 있는 경우 
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])
            
        # 판별 로직 2) 끝까지 탐색했을 때 palindrome word_ids가 있는 경우
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])
            
        return result

class Solution:
    def palindromePairs(self, words):
        trie = Trie()
        
        for i, word in enumerate(words):
            trie.insert(i, word)
            
        results = []
        for i, word in enumerate(words):
            results.extend(trie.search(i, word))
            
        return results
```

### **@staticmethod 데코레이터**
* 자바의 Annotation, 파이썬에서는 '데코레이터'라고 부름
* @staticmethod는 클래스와 독립적인 함수
  + self가 빠져있고, 함수 자체가 별도의 자료형으로 선언됨


```python
class CLASS:
    def a(self):
        pass
    
    @staticmethod
    def b():
        pass
```


```python
type(CLASS.a), type(CLASS.b)
```




    (function, function)




```python
cls = CLASS()
type(cls.a), type(cls.b)
```




    (method, function)



클래스 선언 후에 타입 확인시, 클래스 내 함수는 메소드로, @staticmethod로 선언한 함수는 여전히 함수로 확인됨.


```python

```
