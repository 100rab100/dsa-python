# Day 19: Check if a number is a perfect number
# Topic: Basic Programs
# Approach: Add all proper divisors (divisors excluding the number itself) and compare with n
# Time: O(n)  Space: O(1)

n = int(input("Enter a number: "))

total = 0
for i in range(1, n // 2 + 1):
    if n % i == 0:
        total += i

if n > 0 and total == n:
    print(n, "is a perfect number")
else:
    print(n, "is not a perfect number")

# Sample run:
# Enter a number: 6
# 6 is a perfect number

# Examples:
#   6  -> 1 + 2 + 3 = 6                 (perfect)
#   28 -> 1 + 2 + 4 + 7 + 14 = 28       (perfect)
#   12 -> 1 + 2 + 3 + 4 + 6 = 16        (not perfect)
