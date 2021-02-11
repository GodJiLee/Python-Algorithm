s = ['h', 'e', 'l', 'l', 'o']

# slicing & trick (O(1))
s[:] = s[::-1]
s

# Pythonic way
s.reverse()
s

# swap using two-pointer
left, right = 0, len(s)-1
while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
s