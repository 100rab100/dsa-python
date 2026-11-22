# Day 17: Calculate x raised to the power n without using **
# Topic: Basic Programs
# Approach: Multiply result by x, n times, in a for loop
# Time: O(n)  Space: O(1)

x = float(input("Enter base (x): "))
n = int(input("Enter power (n): "))

result = 1
for i in range(abs(n)):
    result = result * x

if n < 0:
    result = 1 / result

print(x, "raised to the power", n, "=", result)

# Sample run:
# Enter base (x): 2
# Enter power (n): 4
# 2.0 raised to the power 4 = 16.0

# ---------------------------------------------------------
# Approach 2: fast exponentiation, square the base and halve the power
# (Time: O(log n), Space: O(1))
# ---------------------------------------------------------
# result = 1
# base = x
# power = abs(n)
#
# while power > 0:
#     if power % 2 == 1:
#         result = result * base
#     base = base * base
#     power = power // 2
#
# if n < 0:
#     result = 1 / result
#
# print(result)
