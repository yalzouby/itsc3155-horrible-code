# Violating KISS, DRY, Clean Code

# adding two numbers
def add_func(x, y):
    a = x + y
    print("Addition result: " + str(a))
    return a

# subtracting two numbers
def sub_func(x, y):
    a = x - y
    print("Subtraction result: " + str(a))
    return a

# multiplying two numbers
def multi_func(x, y):
    a = x * y
    print("Multiplication result: " + str(a))
    return a

def main():
    print("Calculator")
    a = int(input("Enter first num: "))
    b = int(input("Enter second num: "))

    print("Choose operation:")
    print("1 for add, 2 for subtract, 3 for multiply")

    c = int(input())

    if c == 1:
        add_func(a, b)
    elif c == 2:
        sub_func(a, b)
    elif c == 3:
        multi_func(a, b)
    else:
        print("Invalid choice")

main()
