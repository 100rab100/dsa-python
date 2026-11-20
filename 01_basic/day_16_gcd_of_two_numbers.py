# Day 16: Find the GCD of two numbers
# Topic: Basic Programs
# Approach: Count up from 1 to a and keep the largest common divisor found
# Time: O(a)  Space: O(1)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1
for i in range(1, a + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD =", gcd)

# Sample run:
# Enter first number: 12
# Enter second number: 18
# GCD = 6

# ---------------------------------------------------------
# Approach 2: Euclidean algorithm  (Time: O(log(min(a, b))), Space: O(1))
# ---------------------------------------------------------
# while b != 0:
#     a, b = b, a % b
# print("GCD =", a)
