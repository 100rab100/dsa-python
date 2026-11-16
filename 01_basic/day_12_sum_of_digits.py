# Day 12: Find the sum of digits of a number
# Topic: Basic Programs
# Approach: while loop, take the last digit with % 10, add it, then remove it with // 10
# Time: O(d)  Space: O(1)   (d = number of digits)

n = int(input("Enter a number: "))

n = abs(n)          # ignore the minus sign
total = 0

while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10

print("Sum of digits =", total)

# Sample run:
# Enter a number: 534
# Sum of digits = 12

# ---------------------------------------------------------
# Approach 2: string and sum()  (Time: O(d), Space: O(d))
# ---------------------------------------------------------
# n = abs(int(input("Enter a number: ")))
# print(sum(int(ch) for ch in str(n)))

# ---------------------------------------------------------
# Approach 3: recursion  (Time: O(d), Space: O(d))
# ---------------------------------------------------------
# def sum_digits(n):
#     if n == 0:
#         return 0
#     return n % 10 + sum_digits(n // 10)
#
# print(sum_digits(abs(int(input("Enter a number: ")))))
