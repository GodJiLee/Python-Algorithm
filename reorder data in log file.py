logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']

# separate digits and letters
dig, let = [], []
for log in logs:
    if log.split()[1].isdigit():
        dig.append(log)
    else:
        let.append(log)

# sort by letters
let.sort(key = lambda x: (x.split()[1:], x.split()[0]))

# result
let + dig

# lambda expression
s = ['2 A', '1 B', '4 C', '1 A']
sorted(s)

s.sort(key = lambda x: (x.split()[1], x.split()[0]))
s

# defintion
def func(x):
    return x.split()[1], x.split()[0]

s.sort(key=func)
s