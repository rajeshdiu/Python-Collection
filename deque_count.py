import collections
from itertools import count
nums = (2,9,0,8,2,4,0,9,2,4,8,2,0,4,2,3,4,0)
num_dq=collections.deque(nums)

print(num_dq.count(2))
print(num_dq.count(4))
