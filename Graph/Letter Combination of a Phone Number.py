digits = '23'
path = ''
dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

# 1. explore every combination
def letterCombinations(self, digits: str) -> List[str]:
    def dfs(index, path):
        # back tracking when exploring to the end
        if len(path) == len(digits):
            result.append(path)
            return

        for i in range(index, len(digits)):
            # iterate every string
            for j in dic[digits[i]]:
                dfs(i + 1, path + j)

    # exception
    if not digits:
        return []

    dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    result = []
    dfs(0, '')

    return result

path = []
path + ['abc']

# explanation
# 다이얼의 숫자와 문자를 딕셔너리 형태로 저장해두고, 깊이 우선 탐색으로 전체를 탐색한다.
# dfs 함수에서는 백트래킹과 탐색 알고리즘을 구현하는데, 백트래킹은 ex. '23', 'ad'처럼 입력값과
# 해당하는 문자열의 길이가 같으면 재귀 dfs를 빠져나오도록 한다.
# 이후, 입력값의 각 자리수에 대해 해당하는 문자를 하나씩 path에 추가하는데,
# 2-a, 3-d / 2-b, 3-e/ 2-c, 3-f 이런 식으로 루프가 돈다.
# 이후 dfs(0, '')로 초깃값을 주면서 letterCombinations() 함수를 마무리한다.
