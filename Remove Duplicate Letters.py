# 1. recursive
def removeDuplicateLetters(self, s:str) -> str:
    # arrange by set
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        # devide
        if set(s) == set(suffix):
            return char + self.removeDuplicateLetters(suffix.replace(char, ''))
    return ''

# 2. stack
stack.append(char)
seen.add(char)

counter, stack = collections.Counter(s), []

while stack and char < stack[-1] and counter[stack[-1]] > 0:
    seen.remove(stack.pop())


def removeDuplicateLetters(self, s: str) -> str:
    counter, stack = collections.Counter(s), []

    for char in s:
        counter[char] -= 1
        if char in stack:
            continue
        # remove if counter != 0
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            stack.pop()

        stack.append(char)

    return ''.join(stack)

# 2-1 remove anomalism
def removeDuplicateLetters(self, s: str) -> str:
    counter, seen, stack = collections.Counter(s), set(), []

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        # remove if counter != 0
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)

#---------풀이----------------
# 문자열의 각 문자를 도는데, 전에 들어온 문자와 비교했을 때 사전 순서에 어긋나고, 이전 문자가 문자열 내에
# 중복해서 들어가 있다면, 이전 문자열을 제거해준다. (stack과 seen 둘 다)
# 그리고, seen과 stack에는 반복문에서 걸렸던 문자를 할당하고 다음 차례로 넘어간다.
# 만약, seen 집합 안에 문자가 있는 경우, 새로 할당하면 안 되므로 이후 단계는 skip한다.