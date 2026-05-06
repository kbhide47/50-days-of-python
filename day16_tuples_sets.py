# Day 16: Tuples & Sets Practice

# Q1: Create a tuple and print it
t = (1, 2, 3, 4, 5)
print("Tuple:", t)

print("---------------------------")

# Q2: Access elements of tuple
print("First element:", t[0])
print("Last element:", t[-1])

print("---------------------------")

# Q3: Count occurrences in tuple
num = int(input("Enter number to count in tuple: "))
print("Count:", t.count(num))

print("---------------------------")

# Q4: Find index of element in tuple
num = int(input("Enter number to find index: "))
if num in t:
    print("Index:", t.index(num))
else:
    print("Not found")

print("---------------------------")

# Q5: Convert list to tuple
lst = list(map(int, input("Enter numbers: ").split()))
tup = tuple(lst)
print("Tuple:", tup)

print("---------------------------")

# Q6: Create a set and print it
s = set(lst)
print("Set (unique elements):", s)

print("---------------------------")

# Q7: Add and remove elements in set
s.add(int(input("Enter element to add: ")))
print("After adding:", s)

x = int(input("Enter element to remove: "))
if x in s:
    s.remove(x)
    print("After removing:", s)
else:
    print("Element not found")

print("---------------------------")

# Q8: Union and intersection of sets
s1 = set(map(int, input("Enter first set: ").split()))
s2 = set(map(int, input("Enter second set: ").split()))

print("Union:", s1 | s2)
print("Intersection:", s1 & s2)

print("---------------------------")

# Q9: Difference between sets
print("Difference (s1 - s2):", s1 - s2)

print("---------------------------")

# Q10: Check subset
if s1.issubset(s2):
    print("s1 is subset of s2")
else:
    print("s1 is not subset of s2")
