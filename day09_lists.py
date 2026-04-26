# Day 09: Lists Practice

# Q1: Create a list and print it
lst = [1, 2, 3, 4, 5]
print("List:", lst)

print("---------------------------")

# Q2: Take list input from user
lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Your list:", lst)

print("---------------------------")

# Q3: Find length of list
print("Length:", len(lst))

print("---------------------------")

# Q4: Find sum of list elements
total = sum(lst)
print("Sum:", total)

print("---------------------------")

# Q5: Find maximum and minimum
print("Maximum:", max(lst))
print("Minimum:", min(lst))

print("---------------------------")

# Q6: Append an element
lst.append(int(input("Enter number to append: ")))
print("Updated list:", lst)

print("---------------------------")

# Q7: Remove an element
lst.remove(int(input("Enter number to remove: ")))
print("Updated list:", lst)

print("---------------------------")

# Q8: Reverse a list
lst.reverse()
print("Reversed list:", lst)

print("---------------------------")

# Q9: Sort a list
lst.sort()
print("Sorted list:", lst)

print("---------------------------")

# Q10: Count occurrences of an element
num = int(input("Enter number to count: "))
print("Count:", lst.count(num))
