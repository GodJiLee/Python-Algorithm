
S = 'aAAbbbb'
J = 'aA'

# 1. using hash table
def numJewelsInStones(self, J: str, S: str) -> int:
    # declare hash table
    fregs = {}
    count = 0

    # count frequency of Stones
    for char in S:
        if char not in fregs:
            fregs[char] = 1
        else:
            fregs[char] += 1

    # count frequency of Jewels
    for char in J:
        if char in fregs:
            count += fregs[char]

import collections
# 2. using defaultdict
def numJewelsInStones(self, J: str, S: str) -> int:
    fregs = collections.defaultdict(int)
    count = 0

    # count frequency of Stones 
    for char in S:
        fregs[char] += 1

    # sum of Jewels' frequency without comparison
    for char in J:
        count += fregs[char]

    return count

# 3. using Counter
def numJewelsInStones(self, J: str, S: str) -> int:
    freqs = collections.Counter(S) # count frequency of Stones
    count = 0

    # Sum of Jewels' frequency without comparison
    for char in J:
        count += freqs[char] # default = 0

    return count

# 4. Pythonic Way
def numJewelsInStones(self, J: str, S: str) -> int:
    return sum(s in J for s in S)
