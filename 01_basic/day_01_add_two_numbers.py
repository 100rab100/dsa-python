# Day 2: Add two numbers taken from the user
# Topic: Basic Programs
# Approach: Read both inputs, convert text to numbers with float(), then add
# Time: O(1)  Space: O(1)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

total = a + b

print("Sum =", total)

# Sample run:
# Enter first number: 10
# Enter second number: 5.5
# Sum = 15.5

# ---------------------------------------------------------
# Approach 2: whole numbers only, using int() and an f-string
# ---------------------------------------------------------
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# print(f"Sum of {x} and {y} is {x + y}")

# Note: input() always returns text, so "10" + "5" would give "105".
# Converting with int() or float() first is what makes the addition work.
