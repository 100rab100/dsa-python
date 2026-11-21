# Day 17: Find the LCM of two numbers
# Topic: Basic Programs
# Approach: Find the GCD with the Euclidean algorithm, then LCM = (a * b) / GCD
# Time: O(log(min(a, b)))  Space: O(1)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b
while y != 0:
    x, y = y, x % y      # when the loop ends, x is the GCD

lcm = a * b // x

print("LCM =", lcm)

# Sample run:
# Enter first number: 4
# Enter second number: 6
# LCM = 12
