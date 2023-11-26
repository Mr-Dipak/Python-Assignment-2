"""
Q 7. Write a Python program to make a simple arithmetic calculator.

Problem Statement: 
We need to write a Python program that accepts two numbers and an arithmetic operator from the user and performs the arithmetic operation on
those two numbers.


"""

def arithmetic_calculator(a, b, operator):

    if operator == "+":
        sum = a + b
        return sum
    elif operator == "-":
        subtract = a - b
        return subtract
    elif operator == "*":
        multiplay  = a * b
        return multiplay
    elif operator == "/":
        if b != 0:
            divide = a / b
            return divide
        else:
            return "Error: Division by zero is undefined."



num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
operator = input("Enter Operator ( +, -, *, /): " )

result = arithmetic_calculator(num1, num2, operator)
print(result)

