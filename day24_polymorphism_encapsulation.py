# Day 24: Polymorphism & Encapsulation

# Q1: Polymorphism example
class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()

print("---------------------------")

# Q2: Method overriding
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with self-start")

b = Bike()

b.start()

print("---------------------------")

# Q3: Operator overloading
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print("Addition:", n1 + n2)

print("---------------------------")

# Q4: Encapsulation using private variable
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)

acc = BankAccount(5000)

acc.show_balance()

print("---------------------------")

# Q5: Deposit money
class Bank:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def show(self):
        print("Balance:", self.__balance)

b = Bank()

b.deposit(2000)
b.show()

print("---------------------------")

# Q6: Withdraw money
class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdraw successful")
        else:
            print("Insufficient balance")

    def balance(self):
        print("Balance:", self.__balance)

atm = ATM(5000)

atm.withdraw(1500)
atm.balance()

print("---------------------------")

# Q7: Student details encapsulation
class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def display(self):
        print("Name:", self.__name)
        print("Marks:", self.__marks)

s = Student("Kasturi", 92)

s.display()

print("---------------------------")

# Q8: Polymorphism with shapes
class Circle:
    def area(self):
        print("Area of Circle")

class Rectangle:
    def area(self):
        print("Area of Rectangle")

shapes = [Circle(), Rectangle()]

for shape in shapes:
    shape.area()

print("---------------------------")

# Q9: Encapsulation with getter
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

e = Employee(50000)

print("Salary:", e.get_salary())

print("---------------------------")

# Q10: Encapsulation with setter
class Product:
    def __init__(self):
        self.__price = 0

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

p = Product()

p.set_price(1500)

print("Price:", p.get_price())
