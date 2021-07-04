strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# list.sort()
strs.sort() # impact on the original list
strs

# sorted(list)
sorted(strs)

import collections
dic = collections.defaultdict(int)
for str in strs:
    dic[str] = ''.join(sorted(str))
 
list(dic.values())

anagrams = collections.defaultdict(list)
for word in strs:
    # arrange and then append to the dict
    anagrams[''.join(sorted(word))].append(word)

list(anagrams.values())

# arrangement
# function 'sorted()'
a = [2, 5, 1, 9, 7]
sorted(a)

b = 'zbdaf'
sorted(b)
''.join(sorted(b))

# method 'sort'
alist.sort() # in-place sort
alist = blist.sort() # return: None

c = ['ccc', 'aaaa', 'd', 'bb']
sorted(c, key=len) # arrange by the length of the word

a = ['cde', 'cfc', 'abc']
def fn(s):
    return s[0], s[-1]

print(sorted(a, key=fn))
print(sorted(a))

# lambda expression
a = ['cde', 'cfc', 'abc']
sorted(a, key=lambda s: (s[0], s[-1]))
