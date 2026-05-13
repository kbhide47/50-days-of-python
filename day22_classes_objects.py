# Day 22: Classes & Objects Practice

# Q1: Create Car class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

car1 = Car("Toyota", "Fortuner")
car1.display()

print("---------------------------")

# Q2: Student marks class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            print(self.name, "Pass")
        else:
            print(self.name, "Fail")

s1 = Student("Kasturi", 85)
s1.result()

print("---------------------------")

# Q3: Bank account withdraw
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw successful")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.balance)

acc = BankAccount(5000)

acc.withdraw(2000)
acc.show_balance()

print("---------------------------")

# Q4: Employee bonus calculation
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def bonus(self):
        return self.salary * 0.10

e1 = Employee("Rahul", 60000)

print("Bonus:", e1.bonus())

print("---------------------------")

# Q5: Mobile class
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def details(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

m1 = Mobile("Samsung", 25000)

m1.details()

print("---------------------------")

# Q6: Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)

b1 = Book("Python Basics", "ABC")

b1.display()

print("---------------------------")

# Q7: Area and perimeter of rectangle
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

r1 = Rectangle(10, 5)

print("Area:", r1.area())
print("Perimeter:", r1.perimeter())

print("---------------------------")

# Q8: Create Laptop class
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def specs(self):
        print("Laptop:", self.brand)
        print("RAM:", self.ram, "GB")

l1 = Laptop("HP", 16)

l1.specs()

print("---------------------------")

# Q9: Create ATM class
class ATM:
    def __init__(self, pin):
        self.pin = pin

    def check_pin(self, entered_pin):
        if self.pin == entered_pin:
            print("PIN Correct")
        else:
            print("Wrong PIN")

atm1 = ATM(1234)

atm1.check_pin(1234)

print("---------------------------")

# Q10: Create ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        print("Cart Items:", self.items)

cart = ShoppingCart()

cart.add_item("Shoes")
cart.add_item("Bag")

cart.show_items()
