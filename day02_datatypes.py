# Day 02: Data Types & Type Conversion

# Q1: Check data type
value = input("Enter something: ")
print("Data type is:", type(value))

print("---------------------------")

# Q2: Convert string to int and float
num = input("Enter a number: ")
int_num = int(num)
float_num = float(num)
print("Integer:", int_num)
print("Float:", float_num)

print("---------------------------")

# Q3: Round a float number
num = float(input("Enter a decimal number: "))
print("Rounded value:", round(num))

print("---------------------------")

# Q4: Average of 3 numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
avg = (a + b + c) / 3
print("Average is:", avg)

print("---------------------------")

# Q5: Convert minutes to hours
minutes = int(input("Enter minutes: "))
hours = minutes / 60
print("Hours:", hours)

print("---------------------------")

# Q6: Swap using third variable
a = int(input("Enter a: "))
b = int(input("Enter b: "))
temp = a
a = b
b = temp
print("After swapping:")
print("a =", a)
print("b =", b)

print("---------------------------")

# Q7: Uppercase name
name = input("Enter your name: ")
print("Uppercase:", name.upper())

print("---------------------------")

# Q8: Length of string
text = input("Enter a string: ")
print("Length is:", len(text))

print("---------------------------")

# Q9: Simple Interest
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
print("Simple Interest:", si)

print("---------------------------")

# Q10: Kilometers to meters
km = float(input("Enter distance in km: "))
meters = km * 1000
print("Distance in meters:", meters)
