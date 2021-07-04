# Leetcode #122 주식을 사고팔기 가장 좋은 시점 2


```python
# 그리디
def maxProfit(self, prices):
    result = 0
    # 값이 오르는 경우 매번 그리디 계산
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            result += prices[i + 1] - prices[i]
    return result
```


```python
# 파이썬다운 방식
def maxProfit(self, prices):
    # 0보다 크면 무조건 합산
    return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))
```
