# Day 13: Print the first n terms of the Fibonacci series
# Topic: Basic Programs
# Approach: Keep the last two terms (a, b) and move them forward in a for loop
# Time: O(n)  Space: O(1)

n = int(input("Enter number of terms: "))

if n <= 0:
    print("Enter a positive number")
else:
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Sample run:
# Enter number of terms: 7
# 0 1 1 2 3 5 8

# ---------------------------------------------------------
# Approach 2: using a third variable instead of tuple swap  (Time: O(n), Space: O(1))
# ---------------------------------------------------------
# a = 0
# b = 1
# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

# ---------------------------------------------------------
# Approach 3: recursion  (Time: O(2^n), Space: O(n))
# ---------------------------------------------------------
# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n - 1) + fib(n - 2)
#
# for i in range(n):
#     print(fib(i), end=" ")
