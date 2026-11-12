# Day 15: Reverse a number
# Topic: Basic Programs
# Approach: while loop, take the last digit with % 10 and remove it with // 10
# Time: O(d)  Space: O(1)   (d = number of digits)

n = int(input("Enter a number: "))

rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

print("Reversed number =", rev)

# Sample run:
# Enter a number: 534
# Reversed number = 435

# ---------------------------------------------------------
# Approach 2: string slicing  (Time: O(d), Space: O(d))
# ---------------------------------------------------------
# n = input("Enter a number: ")
# print("Reversed number =", int(n[::-1]))

# Note: trailing zeros disappear, so 2100 gives 12.
