# Day 29: Searching & Sorting Algorithms

# Q1: Linear Search
numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Not found")

print("---------------------------")

# Q2: Binary Search
numbers = sorted(list(map(int, input("Enter sorted numbers: ").split())))
target = int(input("Enter target: "))

low = 0
high = len(numbers) - 1

found = False

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == target:
        print("Found at index", mid)
        found = True
        break

    elif numbers[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

if not found:
    print("Not found")

print("---------------------------")

# Q3: Bubble Sort
numbers = list(map(int, input("Enter numbers: ").split()))

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)

print("---------------------------")

# Q4: Selection Sort
numbers = list(map(int, input("Enter numbers: ").split()))

n = len(numbers)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("Sorted list:", numbers)

print("---------------------------")

# Q5: Insertion Sort
numbers = list(map(int, input("Enter numbers: ").split()))

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1

    while j >= 0 and key < numbers[j]:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = key

print("Sorted list:", numbers)

print("---------------------------")

# Q6: Find largest element
numbers = list(map(int, input("Enter numbers: ").split()))

largest = max(numbers)

print("Largest:", largest)

print("---------------------------")

# Q7: Find smallest element
smallest = min(numbers)

print("Smallest:", smallest)

print("---------------------------")

# Q8: Check if list is sorted
if numbers == sorted(numbers):
    print("List is sorted")
else:
    print("List is not sorted")

print("---------------------------")

# Q9: Reverse sorted list
numbers.sort(reverse=True)

print("Reverse sorted:", numbers)

print("---------------------------")

# Q10: Count occurrences of target
target = int(input("Enter target: "))

count = numbers.count(target)

print("Occurrences:", count)
