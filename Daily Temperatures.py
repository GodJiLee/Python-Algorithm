# stack
while stack and cur > T[stack[-1]]:
    last = stack.pop()
    answer[last] = i - last
stack.append(i)

T = [1, 2, 3, 4, 5]
T[1] = 2
T[0] = 2
T

def dailyTemperatres(self, T: List[int]) -> List[int]:
    answer = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        # compare current T and stack
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer

#---------풀이-----------
# 디폴트 값은 문제에서 요구하는 0으로 처리한다.
# T에서 인덱스와 값을 각각 i, cur로 받아와서 반복문을 도는 동안 stack에는 인덱스를 할당하고,
# cur이 기존 stack에 저장되어 있던 인덱스에 해당하는 값보다 큰 경우,
# 그 인덱스를 뽑아 last로 저장한다.
# 기존 값보다 높은 온도를 찾았으므로, answer라는 정답 리스트에 인덱스 간의 차이를 저장한다.
