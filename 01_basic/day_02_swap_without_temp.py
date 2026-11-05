# Day 2: Swap two numbers without a temporary variable
# Topic: Basic Programs
# Approach: Addition and subtraction (other methods listed below)
# Time: O(1)  Space: O(1)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swap: a =", a, ", b =", b)

a = a + b
b = a - b
a = a - b

print("After swap:  a =", a, ", b =", b)

# Sample run:
# Enter first number: 10
# Enter second number: 20
# Before swap: a = 10 , b = 20
# After swap:  a = 20 , b = 10

# ---------------------------------------------------------
# Approach 2: XOR (works for integers only)
# ---------------------------------------------------------
# a = a ^ b
# b = a ^ b
# a = a ^ b

# ---------------------------------------------------------
# Approach 3: Python tuple swap (best in real code)
# ---------------------------------------------------------
# a, b = b, a
