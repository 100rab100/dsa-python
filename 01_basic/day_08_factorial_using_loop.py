# Day 08: Find the factorial of n using a loop
# Topic: Basic Programs
# Approach: Start with result = 1 and multiply it by every number from 1 to n
# Time: O(n)  Space: O(1)

n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers")
else:
    result = 1
    for i in range(1, n + 1):
        result = result * i
    print("Factorial of", n, "is", result)

# Sample run:
# Enter a number: 5
# Factorial of 5 is 120

# ---------------------------------------------------------
# Approach 2: while loop
# ---------------------------------------------------------
# result = 1
# i = 1
# while i <= n:
#     result = result * i
#     i += 1
# print(result)

# ---------------------------------------------------------
# Approach 3: count down using n itself
# ---------------------------------------------------------
# result = 1
# while n > 1:
#     result = result * n
#     n = n - 1
# print(result)

# ---------------------------------------------------------
# Approach 4: recursion  (Time: O(n), Space: O(n))
# ---------------------------------------------------------
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
#
# print(factorial(n))

# ---------------------------------------------------------
# Approach 5: built-in math.factorial()
# ---------------------------------------------------------
# import math
# print(math.factorial(n))
