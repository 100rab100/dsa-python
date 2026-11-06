# Day 3: Check if a number is even or odd
# Topic: Basic Programs
# Approach: A number is even if it leaves remainder 0 when divided by 2
# Time: O(1)  Space: O(1)

n = int(input("Enter a number: "))

if n % 2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")

# Sample run:
# Enter a number: 7
# 7 is odd

# ---------------------------------------------------------
# Approach 2: bitwise AND (the last bit of an odd number is 1)
# ---------------------------------------------------------
# if n & 1:
#     print(n, "is odd")
# else:
#     print(n, "is even")

# ---------------------------------------------------------
# Approach 3: one-line conditional expression
# ---------------------------------------------------------
# print(n, "is", "even" if n % 2 == 0 else "odd")
