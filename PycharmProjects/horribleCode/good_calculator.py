# Following KISS, DRY, Clean Code

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def get_operation_choice():
    print("Choose operation:")
    print("1 for Add, 2 for Subtract, 3 for Multiply")
    return int(input("Enter choice: "))


def main():
    print("Simple Calculator")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    choice = get_operation_choice()

    if choice == 1:
        print(f"Result: {add(a, b)}")
    elif choice == 2:
        print(f"Result: {subtract(a, b)}")
    elif choice == 3:
        print(f"Result: {multiply(a, b)}")
    else:
        print("Invalid choice")


main()
