# Day 46: Heap and Priority Queue Problems

import heapq

# Q1: Create a Min Heap
numbers = [30, 10, 50, 20, 40]

heapq.heapify(numbers)

print("Min Heap:", numbers)

print("---------------------------")

# Q2: Insert into Heap
heapq.heappush(numbers, 5)

print("After Insertion:", numbers)

print("---------------------------")

# Q3: Remove Minimum Element
minimum = heapq.heappop(numbers)

print("Removed Minimum:", minimum)
print("Heap:", numbers)

print("---------------------------")

# Q4: Find Smallest Element
print("Smallest Element:", numbers[0])

print("---------------------------")

# Q5: Find 3 Smallest Elements
nums = list(map(int, input("Enter numbers: ").split()))

print("3 Smallest:", heapq.nsmallest(3, nums))

print("---------------------------")

# Q6: Find 3 Largest Elements
print("3 Largest:", heapq.nlargest(3, nums))

print("---------------------------")

# Q7: Heap Sort
nums = list(map(int, input("Enter numbers: ").split()))

heapq.heapify(nums)

sorted_list = []

while nums:
    sorted_list.append(heapq.heappop(nums))

print("Sorted List:", sorted_list)

print("---------------------------")

# Q8: Kth Smallest Element
nums = list(map(int, input("Enter numbers: ").split()))

k = int(input("Enter k: "))

print("Kth Smallest:", heapq.nsmallest(k, nums)[-1])

print("---------------------------")

# Q9: Priority Queue Example
tasks = []

heapq.heappush(tasks, (2, "Study"))
heapq.heappush(tasks, (1, "Assignment"))
heapq.heappush(tasks, (3, "Gaming"))

print("Priority Queue:")

while tasks:
    priority, task = heapq.heappop(tasks)
    print(priority, "-", task)

print("---------------------------")

# Q10: Merge Sorted Lists
list1 = [1, 3, 5]
list2 = [2, 4, 6]

merged = list(heapq.merge(list1, list2))

print("Merged List:", merged)
