# Leetcode #136 싱글넘버


```python
0 ^ 0
```




    0




```python
4 ^ 0
```




    4




```python
4 ^ 4
```




    0




```python
nums = [2, 2, 1]
```


```python
# 비트 연산을 이용한 풀이
def singleNumber(self, nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```


```python
singleNumber(nums)
```




    1


