# Day 23: Inheritance Practice

# Q1: Basic inheritance
class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    pass

d = Dog()
d.sound()

print("---------------------------")

# Q2: Child class method
class Animal:
    def eat(self):
        print("Animal eats food")

class Cat(Animal):
    def meow(self):
        print("Cat says meow")

c = Cat()

c.eat()
c.meow()

print("---------------------------")

# Q3: Vehicle inheritance
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

car = Car()

car.start()
car.drive()

print("---------------------------")

# Q4: Employee inheritance
class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Employee:", self.name)

class Manager(Employee):
    def department(self):
        print("Department: IT")

m = Manager("Rahul")

m.show()
m.department()

print("---------------------------")

# Q5: Person and Student
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def display(self):
        print("Student Name:", self.name)

s = Student("Kasturi")

s.display()

print("---------------------------")

# Q6: Multilevel inheritance
class Grandparent:
    def house(self):
        print("Grandparent's House")

class Parent(Grandparent):
    def car(self):
        print("Parent's Car")

class Child(Parent):
    def bike(self):
        print("Child's Bike")

child = Child()

child.house()
child.car()
child.bike()

print("---------------------------")

# Q7: Method overriding
class Bird:
    def sound(self):
        print("Bird makes sound")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")

sp = Sparrow()

sp.sound()

print("---------------------------")

# Q8: Use super()
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)

t = Teacher("Anita", "Math")

t.display()

print("---------------------------")

# Q9: Bank account inheritance
class Account:
    def __init__(self, balance):
        self.balance = balance

class SavingsAccount(Account):
    def interest(self):
        print("Interest:", self.balance * 0.05)

acc = SavingsAccount(10000)

acc.interest()

print("---------------------------")

# Q10: Shape inheritance
class Shape:
    def area(self):
        print("Area calculation")

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Rectangle Area:", self.length * self.breadth)

r = Rectangle(5, 4)

r.area()
