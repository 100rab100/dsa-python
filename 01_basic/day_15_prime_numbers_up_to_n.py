# Day 15: Print all prime numbers between 1 and n
# Topic: Basic Programs
# Approach: For each number, use a flag and check divisors up to its square root
# Time: O(n * sqrt(n))  Space: O(1)

import math

n = int(input("Enter a number: "))

for num in range(2, n + 1):
    is_prime = True                              # assume prime at the start

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False                     # found a divisor, so not prime
            break

    if is_prime:
        print(num, end=" ")

# Sample run:
# Enter a number: 30
# 2 3 5 7 11 13 17 19 23 29

# ---------------------------------------------------------
# Approach 2: for-else, no flag needed  (Time: O(n * sqrt(n)), Space: O(1))
# ---------------------------------------------------------
# for num in range(2, n + 1):
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             break
#     else:
#         print(num, end=" ")

# ---------------------------------------------------------
# Approach 3: Sieve of Eratosthenes  (Time: O(n log log n), Space: O(n))
# ---------------------------------------------------------
# sieve = [True] * (n + 1)
# for i in range(2, int(math.sqrt(n)) + 1):
#     if sieve[i]:
#         for j in range(i * i, n + 1, i):
#             sieve[j] = False
#
# for num in range(2, n + 1):
#     if sieve[num]:
#         print(num, end=" ")
