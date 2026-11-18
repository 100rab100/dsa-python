# Day 14: Check if a number is prime
# Topic: Basic Programs
# Approach: Check for a divisor from 2 up to the square root of n (for-else)
# Time: O(sqrt(n))  Space: O(1)

import math

n = int(input("Enter a number: "))

if n < 2:
    print(n, "is not a prime number")
else:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")

# Sample run:
# Enter a number: 29
# 29 is a prime number

# ---------------------------------------------------------
# Approach 2: count the factors  (Time: O(n), Space: O(1))
# ---------------------------------------------------------
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1
# print("Prime" if count == 2 else "Not prime")
