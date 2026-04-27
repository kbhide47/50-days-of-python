# Day 10: Mini Project (Calculator + List Operations)

while True:
    print("\n----- MENU -----")
    print("1. Calculator")
    print("2. List Operations")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    # Q1–Q5: Calculator
    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ")

        if op == "+":
            print("Result:", a + b)
        elif op == "-":
            print("Result:", a - b)
        elif op == "*":
            print("Result:", a * b)
        elif op == "/":
            if b != 0:
                print("Result:", a / b)
            else:
                print("Division by zero not allowed")
        else:
            print("Invalid operator")

    # Q6–Q10: List operations
    elif choice == 2:
        lst = list(map(int, input("Enter numbers: ").split()))

        print("\nList Menu")
        print("1. Append")
        print("2. Remove")
        print("3. Find Max/Min")
        print("4. Sort")
        print("5. Reverse")

        sub_choice = int(input("Enter your choice: "))

        if sub_choice == 1:
            x = int(input("Enter number to append: "))
            lst.append(x)
            print("Updated list:", lst)

        elif sub_choice == 2:
            x = int(input("Enter number to remove: "))
            if x in lst:
                lst.remove(x)
                print("Updated list:", lst)
            else:
                print("Element not found")

        elif sub_choice == 3:
            print("Max:", max(lst))
            print("Min:", min(lst))

        elif sub_choice == 4:
            lst.sort()
            print("Sorted list:", lst)

        elif sub_choice == 5:
            lst.reverse()
            print("Reversed list:", lst)

        else:
            print("Invalid choice")

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
