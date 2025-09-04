#!/usr/bin/env python3
"""
Simple Calculator
------------------
Prompts the user for:
1. Two numbers
2. An operation (+, -, *, /)

Then performs the calculation and displays the result.
"""

def main():
    print("=== Simple Calculator ===")

    # Get two numbers from the user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❗ Invalid input. Please enter numbers only.")
        return

    # Get the operation
    print("Choose operation:")
    print(" + for addition")
    print(" - for subtraction")
    print(" * for multiplication")
    print(" / for division")

    operation = input("Enter operation: ").strip()

    # Perform the calculation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("❗ Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("❗ Invalid operation.")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
