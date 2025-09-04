#!/usr/bin/env python3
import string
import random

def generate_password(length: int) -> str:
    # Characters use: letters, digits and punctuation
    all_chars = string.ascii_letters + string.digits + string.punctuation
    # Randomly Generte the Password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter desired password length (e.g., 12): "))
        if length <= 0:
            print("❗ Please enter a positive number.")
            return
    except ValueError:
        print("❗ Invalid input. Please enter a number.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()

