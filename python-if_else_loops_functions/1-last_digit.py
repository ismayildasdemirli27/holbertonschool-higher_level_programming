#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Calculate the last digit
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10

# Print the initial part of the string
print(f"Last digit of {number} is {last_digit} and is ", end="")

# Check conditions and print the rest
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
