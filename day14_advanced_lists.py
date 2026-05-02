# Day 14: Advanced List Problems

# Q1: Find largest difference (max - min)
lst = list(map(int, input("Enter numbers: ").split()))
print("Difference:", max(lst) - min(lst))

print("---------------------------")

# Q2: Find all duplicates
lst = list(map(int, input("Enter numbers: ").split()))
duplicates = []

for num in lst:
    if lst.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicates:", duplicates)

print("---------------------------")

# Q3: Merge two sorted lists
lst1 = list(map(int, input("Enter first sorted list: ").split()))
lst2 = list(map(int, input("Enter second sorted list: ").split()))
merged = sorted(lst1 + lst2)
print("Merged list:", merged)

print("---------------------------")

# Q4: Find intersection of two lists
lst1 = list(map(int, input("Enter first list: ").split()))
lst2 = list(map(int, input("Enter second list: ").split()))
intersection = list(set(lst1) & set(lst2))
print("Intersection:", intersection)

print("---------------------------")

# Q5: Find union of two lists
union = list(set(lst1) | set(lst2))
print("Union:", union)

print("---------------------------")

# Q6: Find second smallest element
lst = list(map(int, input("Enter numbers: ").split()))
unique = sorted(set(lst))
if len(unique) >= 2:
    print("Second smallest:", unique[1])
else:
    print("Not possible")

print("---------------------------")

# Q7: Check if two lists are equal
lst1 = list(map(int, input("Enter first list: ").split()))
lst2 = list(map(int, input("Enter second list: ").split()))
if sorted(lst1) == sorted(lst2):
    print("Lists are equal")
else:
    print("Lists are not equal")

print("---------------------------")

# Q8: Find sublist in list
lst = list(map(int, input("Enter main list: ").split()))
sub = list(map(int, input("Enter sublist: ").split()))

found = False
for i in range(len(lst) - len(sub) + 1):
    if lst[i:i+len(sub)] == sub:
        found = True
        break

print("Sublist found" if found else "Sublist not found")

print("---------------------------")

# Q9: Split list into even and odd
lst = list(map(int, input("Enter numbers: ").split()))
even = [x for x in lst if x % 2 == 0]
odd = [x for x in lst if x % 2 != 0]
print("Even:", even)
print("Odd:", odd)

print("---------------------------")

# Q10: Find cumulative sum list
lst = list(map(int, input("Enter numbers: ").split()))
cum_sum = []
total = 0

for num in lst:
    total += num
    cum_sum.append(total)

print("Cumulative sum:", cum_sum)
