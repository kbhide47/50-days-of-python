# Day 25: Exception Handling Practice

# Q1: Handle division by zero
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

print("---------------------------")

# Q2: Handle invalid input
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Invalid input")

print("---------------------------")

# Q3: Handle index error
try:
    lst = [1, 2, 3]

    index = int(input("Enter index: "))

    print(lst[index])

except IndexError:
    print("Index out of range")

print("---------------------------")

# Q4: Multiple exceptions
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ZeroDivisionError:
    print("Division by zero error")

except ValueError:
    print("Invalid input")

print("---------------------------")

# Q5: Use finally block
try:
    num = int(input("Enter number: "))
    print("Square:", num * num)

except ValueError:
    print("Invalid input")

finally:
    print("Program finished")

print("---------------------------")

# Q6: File handling exception
try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("File not found")

print("---------------------------")

# Q7: Custom exception message
try:
    age = int(input("Enter age: "))

    if age < 18:
        raise Exception("You are not eligible")

    print("Eligible")

except Exception as e:
    print(e)

print("---------------------------")

# Q8: Handle key error
try:
    student = {"name": "Kasturi"}

    print(student["age"])

except KeyError:
    print("Key does not exist")

print("---------------------------")

# Q9: Handle type error
try:
    result = "2" + 2
    print(result)

except TypeError:
    print("Type mismatch error")

print("---------------------------")

# Q10: General exception handler
try:
    num = int(input("Enter number: "))
    print(100 / num)

except Exception as e:
    print("Error:", e)
