s = 'A man, a plan, a canal: Panama'

# Regular Expression, slicing
import re
s = s.lower()
s = re.sub('[^a-z0-9]', '', s)
s == s[::-1]

# precleaning
strs = []
for char in s:
    if char.isalnum():
        strs.append(char.lower())

# pop(0), pop()
while len(strs) > 1:
    if strs.pop(0) != strs.pop():
        return False
return True

# Using Deque
import collections
Deque = collections.deque()
strs = Deque
for char in s:
    if char.isalnum():
        strs.append(char.lower())

# popleft()
while len(str) > 1:
    if strs.popleft() != strs.pop():
        return False
