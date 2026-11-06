# Day 3: Find the largest of three numbers
# Topic: Basic Programs
# Approach: Compare using if-elif-else
# Time: O(1)  Space: O(1)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest =", largest)

# Sample run:
# Enter first number: 12
# Enter second number: 45
# Enter third number: 30
# Largest = 45.0

# ---------------------------------------------------------
# Approach 2: keep a running maximum
# ---------------------------------------------------------
# largest = a
# if b > largest:
#     largest = b
# if c > largest:
#     largest = c

# ---------------------------------------------------------
# Approach 3: built-in max()
# ---------------------------------------------------------
# print(max(a, b, c))
