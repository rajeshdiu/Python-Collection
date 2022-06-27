
import collections

even_nums = (2, 4, 6)

print("Original tuple:")

print(even_nums)

print(type(even_nums))

even_nums_deque = collections.deque(even_nums)
print("\nOriginal deque:")
print(even_nums_deque)

even_nums_deque.append(8)
even_nums_deque.append(10)
even_nums_deque.append(12)
even_nums_deque.appendleft(2)

print("New deque from an existing iterable object:")
print(even_nums_deque)
print(type(even_nums_deque))