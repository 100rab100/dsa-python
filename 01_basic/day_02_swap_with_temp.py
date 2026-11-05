# Day 2: Swap two numbers using a temporary variable
# Topic: Basic Programs
# Approach: Store one value in temp, then overwrite a and b
# Time: O(1)  Space: O(1)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swap: a =", a, ", b =", b)

temp = a
a = b
b = temp

print("After swap:  a =", a, ", b =", b)

# Sample run:
# Enter first number: 10
# Enter second number: 20
# Before swap: a = 10 , b = 20
# After swap:  a = 20 , b = 10

# Python shortcut (no temp variable needed):
# a, b = b, a
