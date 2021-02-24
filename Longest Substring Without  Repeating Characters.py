# 1. sliding window
def lenthOfLongestSubstring(self, s: str) -> int:
    used = {}
    max_length = start = 0

    for index, char in enumerate(s):
        # updating 'start' position for the repeating string
        if char in used and start <= used[char]:
            start = used[char] + 1
        else: # updating maxlen of string
            max_length = max(max_length, index - start + 1)

        used[char] = index # updating current string's position

    return max_length