# Day 28: Advanced Python Features

# Q1: List comprehension
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print("Squares:", squares)

print("---------------------------")

# Q2: Even numbers using list comprehension
even = [x for x in range(1, 21) if x % 2 == 0]

print("Even numbers:", even)

print("---------------------------")

# Q3: Convert strings to uppercase
words = ["python", "java", "c++"]

upper_words = [word.upper() for word in words]

print("Uppercase words:", upper_words)

print("---------------------------")

# Q4: Dictionary comprehension
numbers = [1, 2, 3, 4, 5]

square_dict = {x: x * x for x in numbers}

print("Dictionary:", square_dict)

print("---------------------------")

# Q5: Zip two lists
names = ["Kasturi", "Rahul", "Anita"]
marks = [90, 85, 95]

combined = list(zip(names, marks))

print("Zipped list:", combined)

print("---------------------------")

# Q6: Enumerate function
fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

print("---------------------------")

# Q7: *args example
def total(*numbers):
    print("Numbers:", numbers)
    print("Sum:", sum(numbers))

total(1, 2, 3, 4, 5)

print("---------------------------")

# Q8: **kwargs example
def student_info(**details):
    for key, value in details.items():
        print(key, ":", value)

student_info(name="Kasturi", age=20, branch="ENTC")

print("---------------------------")

# Q9: Sort list using lambda
students = [("Rahul", 85), ("Anita", 92), ("Kasturi", 88)]

students.sort(key=lambda x: x[1])

print("Sorted by marks:", students)

print("---------------------------")

# Q10: List flattening
matrix = [[1, 2], [3, 4], [5, 6]]

flat = [num for row in matrix for num in row]

print("Flattened list:", flat)
