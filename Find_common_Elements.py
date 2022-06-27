from collections import deque,Counter


dq=['PHP', 'PHP', 'Python', 'PHP', 'Python', 'JS', 'Python', 'Python', 'PHP', 'Python']

print(dq)
ctr=Counter(dq)
print(ctr.most_common(1)[0][0])
