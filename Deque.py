from collections import deque
from typing import Deque


myString=input("Enter a string:")

dq=Deque(myString)


for i in dq:
    print(i)