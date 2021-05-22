# 다이나믹 프로그래밍
### 상향식


```python
def fib(n):
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

### 하향식


```python
def fib(n):
    if n <= 1:
        return n
    
    if dp[n]:
        return dp[n]
    
    dp[n] = fib(n - 1) + fib(n - 2)
    return dp[n]
```

# Leetcode #509 피보나치 수


```python
# 재귀 구조 브루트 포스
def fib(self, N):
    if N <= 1:
        return N
    return self.fib(N - 1) + self.fib(N - 2)
```


```python
import collections

# 메모이제이션 (하향식) 풀이
class Solution:
    dp = collections.defaultdict(int)
    
    def fib(self, N):
        if N <= 1:
            return N
        
        if self.dp[N]: # 이미 계산된 값은 저장해뒀다가 바로 리턴
            return self.dp[N]
        
        self.dp[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.dp[N]
```


```python
# 타뷸레이션 (상향식) 풀이
class Solution:
    dp = collections.defaultdict(int)
    
    def fib(self, N):
        self.dp[1] = 1
        
        for i in range(2, N + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2] # 작은 값부터 차례로 계산
        return self.dp[N]
```


```python
# 두 변수만 이용해 공간 절약
def fib(self, N):
    x, y = 0, 1
    for i in range(0, N):
        x, y = y, x + y
    return x # 공간복잡도 O(n) -> O(1)로 줄어듦 (시간복잡도는 그대로)
```


```python
# 행렬을 이용
def fib(n):
    M = np.matrix([[0, 1], [1, 1]])
    vec = np.array([[0], [1]])
    
    return np.matmul(M ** n, vec)[0]
```

# 0-1 배낭 문제 (분할 불가능)


```python
# input
cargo = [
    (4, 12), 
    (2, 1),
    (10, 4),
    (1, 1),
    (2, 2),
]
```


```python
def zero_one_knapsack(cargo):
    capacity = 15
    pack = []
    
    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
                
            elif cargo[i - 1][1] <= c:
                pack[i].append(max(cargo[i - 1][0] + pack[i - 1][c - cargo[i - 1][1]],
                                  pack[i - 1][c]))
            
            else:
                pack[i].append(pack[i - 1][c])
    return pack[-1][-1]

r = zero_one_knapsack(cargo)
```


```python
r
```




    15




```python

```
