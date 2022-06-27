import collections,re
from typing import Type

n=int(input("Enter How Many Subject:"))

book_item=collections.OrderedDict()

for i in range(n):
    subject_name_marks=re.split(r'(\d+)$',input("Enter subject and marks: ").strip())
    subject_name=subject_name_marks[0]
    subject_marks=int(subject_name_marks[1])

    if subject_name not in book_item:
       book_item[subject_name]=subject_marks
    else:
       book_item[subject_name]+=subject_marks

print((book_item))


for i in book_item:
    print(i+str(book_item[i]))