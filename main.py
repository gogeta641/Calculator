# Calculator

# Add
def add(n1, n2):
    return(n1 + n2)

# Subtract
def subtract(n1, n2):
    return(n1 - n2)

# Multiply
def multiply(n1, n2):
    return(n1 * n2)

# Divide
def divide(n1, n2):
    return(n1 / n2)

# Dictionary

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
    }

def calculator():
    num1 = int(input("What's the first number?: "))

    for operand in operations:
        print(operand)

    operand = input("Pick an operations from the line above: ")
    num2 = int(input("What's the second number?: "))

    answer = operations[operand](num1, num2)
    print(f"{num1} {operand} {num2} = {answer}")

    repeat = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")

    if repeat == "n":
        calculator()

    while repeat == "y":
        operand = input("Pick another operation: ")
        num3 = int(input("What's the next number?: "))
        second_answer = operations[operand](answer, num3)
        print(f"{answer} {operand} {num3} = {second_answer}")
        answer = second_answer
        repeat = input(f"Type 'y' to continue calculating with {second_answer}, or type 'n' to start a new caculation.: ")
        if repeat == "n":
            calculator()

calculator()