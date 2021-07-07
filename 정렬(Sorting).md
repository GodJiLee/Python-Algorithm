# **정렬**
* 목록의 요소를 특정 순서대로 넣는 알고리즘
* 대개 숫자식 순서(numeric order)와 사전식 순서(lexigraphical order)로 정렬함

### **버블 정렬**
* 복잡도 O(n^2)으로 비효율적인 편


```python
# 버블 정렬 수도코드
Bubblesort(A)
    for i from 1 to A.length
        for j from 0 to A.length - 1
            if A[j] > A[j + 1]
                swap a[j] with a[j + 1]
```


```python
def bubblesort(A):
    for i in range(1, len(A)):
        for j in range(1, len(A) - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j] # swap
```

### **병합 정렬**
* 최선과 최악 모두 O(n log n)으로 일정
* 퀵 정렬보다는 느리지만, 안전한 정렬이라는 점에서 많이 쓰임
* 원본 정렬을 더 이상 쪼갤 수 없을 정도로 분할한 후, 분할이 끝나면 정렬하며 정복

![Alt text](정렬_병합.jpg)
<img src='정렬_병합.jpg' width = '40%', height = '30%' title = '병합 정렬 구조' alt = 'Merge Sort'></img>


```python
import os
os.getcwd()
```




    'C:\\Users\\jiwon.DESKTOP-J6K6P2J\\알고리즘'



### **퀵 정렬**
* 피벗을 기준으로 좌우로 나누는 특징 (=파티션 교환정렬) 
* 로무토 파티션: 항상 맨 오른쪽 피벗을 선택하는 방식 


```python
# 퀵 정렬 수도 코드
Quicksort(A, lo, hi)
    if lo < hi then 
        pivot := partition(A, lo, hi) # partition scheme
        Quicksort(A, lo, pivot - 1)
        Quicksort(A, pivot + 1, hi)
```


```python
def quicksort(A, lo, hi):
    ...
    if lo < hi:
        pivot = partition(lo, hi)
        quicksort(A, lo, pivot - 1)
        quicksort(A, pivot + 1, hi)
```


```python
# 퀵 정렬 로무토 파티션 함수 수도코드
partition(A, lo, hi)
    pivot := A[hi] # 맨 오른쪽을 피벗으로 설정
    i := lo
    for j:= lo to hi do 
        if A[j] < pivot then
            swap A[i] with A[j] # A[i]는 low로 고정 
            i := i + 1 # 하나씩 옮겨가며 정복
        swap A[i] with A[hi]
        return i
```

로무토 파티션은 맨 오른쪽을 피벗으로 정하는 단순한 방식


```python
# two-pointer
def partition(lo, hi):
    pivot = A[hi] # 맨 오른쪽으로 pivot 고정
    left = lo # 맨 첫번째 노드로 고정
    for right in range(lo, hi):
        if A[right] < pivot:
            # swap
            A[left], A[right] = A[right], A[left] # 가장 큰 값 오른쪽으로 보내기
            left += 1
        A[left], A[hi] = A[hi], A[left] # swap
        
        return left
```


```python
# 전체코드
def quicksort(A, lo, hi): # 중첩함수
    def partition(lo, hi):
        pivot = A[hi] # 맨 오른쪽 
        left = lo
        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left] # swap
                left += 1
        
        A[left], A[hi] = A[hi], A[left] # swap
        return left
    
    if lo < hi: 
        pivot = partition(lo, hi)
        quicksort(A, lo, pivot - 1)
        quicksort(A, pivot + 1, hi) 
```

![Alt text](정렬_퀵.jpg)

for문을 모두 돈 후에는 pivot 값을 기준으로 왼쪽에는 작은 값이, 오른쪽에는 큰 값이 할당된다. 이러한 분할 및 재조정 과정은 left < hi를 만족할 때까지 반복되며 정렬이 완료된다.
* 퀵 정렬은 최악의 경우 O(n^2)의 복잡도를 갖음. (맨 오른쪽부터 시작하므로 이미 정렬된 배열의 경우 파티셔닝 없이 작업이 계속된다.)
* 병합 정렬보다 성능 편차가 심한 편
