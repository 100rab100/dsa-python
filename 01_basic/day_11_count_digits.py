# Day 11: Count the digits in a number
# Topic: Basic Programs
# Approach: while loop, remove the last digit with // 10 and count each step
# Time: O(d)  Space: O(1)   (d = number of digits)

n = int(input("Enter a number: "))

n = abs(n)          # ignore the minus sign
count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        n = n // 10
        count += 1

print("Number of digits =", count)

# Sample run:
# Enter a number: 534
# Number of digits = 3

# ---------------------------------------------------------
# Approach 2: string length  (Time: O(d), Space: O(d))
# ---------------------------------------------------------
# n = int(input("Enter a number: "))
# print(len(str(abs(n))))

# ---------------------------------------------------------
# Approach 3: log10  (Time: O(1), Space: O(1))
# ---------------------------------------------------------
# import math
# n = abs(int(input("Enter a number: ")))
# print(1 if n == 0 else int(math.log10(n)) + 1)

# ---------------------------------------------------------
# Approach 4: recursion  (Time: O(d), Space: O(d))
# ---------------------------------------------------------
# def count_digits(n):
#     if n < 10:
#         return 1
#     return 1 + count_digits(n // 10)
#
# print(count_digits(abs(int(input("Enter a number: ")))))
