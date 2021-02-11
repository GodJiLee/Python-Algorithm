# Input
paragraph = 'Bob hit a ball, the hit BALL flew for after it was hit'
banned = ['hit']

# pre-cleaning
paragraph = paragraph.lower()
par = paragraph.split(',')
par1 = par[0].split()
par2 = par[1].split()
par = par1 + par2

# find common words
common = []
for word in par:
    count = 0
    for iter in par:
        if word == iter:
            count += 1
    if count >= 2:
        common.append(word)

# delete banned words
common = set(common)
common = list(common)
common

for ban in banned:
    for word in common:
        if word == ban:
            common.remove(word)

for res in common:
    print(res)


# Input
paragraph = 'Bob hit a ball, the hit BALL flew for after it was hit'
banned = ['hit']

# 1
import re
import collections

# pre-processing
words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]
counts = collections.Counter(words) # counts the number of words

counts.most_common(1)[0][0] # find the most common word

# 2
# defaultdict
counts = collections.defaultdict(int)
for word in words:
    counts[word] += 1

# argmax
max(counts, key=counts.get)