from collections import Counter

myString=input("Enter a string:")
print("Original String is",myString)

print(Counter(myString).most_common(3))