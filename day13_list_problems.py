# Day 13: List Problems (Logic Building)

# Q1: Find second largest number
lst = list(map(int, input("Enter numbers: ").split()))
unique = list(set(lst))
unique.sort()
print("Second largest:", unique[-2] if len(unique) >= 2 else "Not possible")

print("---------------------------")

# Q2: Remove duplicates from list
lst = list(map(int, input("Enter numbers: ").split()))
result = list(set(lst))
print("Without duplicates:", result)

print("---------------------------")

# Q3: Find common elements in two lists
lst1 = list(map(int, input("Enter first list: ").split()))
lst2 = list(map(int, input("Enter second list: ").split()))
common = list(set(lst1) & set(lst2))
print("Common elements:", common)

print("---------------------------")

# Q4: Check if list is sorted
lst = list(map(int, input("Enter numbers: ").split()))
if lst == sorted(lst):
    print("Sorted")
else:
    print("Not Sorted")

print("---------------------------")

# Q5: Find all pairs with given sum
lst = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == target:
            print("Pair:", lst[i], lst[j])

print("---------------------------")

# Q6: Rotate list by k positions
lst = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))
k = k % len(lst)
rotated = lst[-k:] + lst[:-k]
print("Rotated list:", rotated)

print("---------------------------")

# Q7: Find missing number (1 to n)
lst = list(map(int, input("Enter numbers from 1 to n with one missing: ").split()))
n = len(lst) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(lst)
print("Missing number:", expected_sum - actual_sum)

print("---------------------------")

# Q8: Move zeros to end
lst = list(map(int, input("Enter numbers: ").split()))
non_zero = [x for x in lst if x != 0]
zeros = [0] * lst.count(0)
print("Modified list:", non_zero + zeros)

print("---------------------------")

# Q9: Find frequency of elements
lst = list(map(int, input("Enter numbers: ").split()))
freq = {}

for num in lst:
    freq[num] = freq.get(num, 0) + 1

print("Frequency:", freq)

print("---------------------------")

# Q10: Check if list is palindrome
lst = list(map(int, input("Enter numbers: ").split()))
if lst == lst[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
