a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Calculator operation
while True:

    print("\n1. Sum")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Floor Division")
    print("7. Display")
    print("8. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        print("Sum =", a + b)

    elif choice == 2:
        print("Subtraction =", a - b)

    elif choice == 3:
        print("Multiplication =", a * b)

    elif choice == 4:
        print("Division =", a / b)

    elif choice == 5:
        print("Modulus =", a % b)

    elif choice == 6:
        print("Floor Division =", a // b)

    elif choice == 7:
        print("Value of a =", a)
        print("Value of b =", b)

    elif choice == 8:
        print("Calculator Closed")
        break

    else:
        print("Invalid Choice")