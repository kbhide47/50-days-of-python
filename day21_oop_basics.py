# Day 21: OOP Basics

# Q1: Create a simple class
class Student:
    pass

s1 = Student()
print("Class and object created")

print("---------------------------")

# Q2: Add attributes to object
class Student:
    name = "Kasturi"
    age = 20

s1 = Student()

print("Name:", s1.name)
print("Age:", s1.age)

print("---------------------------")

# Q3: Use constructor (__init__)
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Kasturi", 20)

print("Name:", s1.name)
print("Age:", s1.age)

print("---------------------------")

# Q4: Create method inside class
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello,", self.name)

s1 = Student("Kasturi")
s1.greet()

print("---------------------------")

# Q5: Create class for rectangle
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

r1 = Rectangle(5, 3)

print("Area:", r1.area())

print("---------------------------")

# Q6: Create class for calculator
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

calc = Calculator()

print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))

print("---------------------------")

# Q7: Create class for circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c1 = Circle(4)

print("Circle Area:", c1.area())

print("---------------------------")

# Q8: Create class with user input
class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def display(self):
        print("Name:", self.name)
        print("City:", self.city)

name = input("Enter name: ")
city = input("Enter city: ")

p1 = Person(name, city)
p1.display()

print("---------------------------")

# Q9: Create BankAccount class
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount(1000)

acc.deposit(500)
acc.show_balance()

print("---------------------------")

# Q10: Create Employee class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)

e1 = Employee("Rahul", 50000)

e1.display()
