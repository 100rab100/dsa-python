# Day 4: Check if a number is positive, negative or zero
# Topic: Basic Programs
# Approach: Compare the number with 0 using if-elif-else
# Time: O(1)  Space: O(1)

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"


num = float(input("Enter a number: "))
print(check_number(num))

# Sample run:
# Enter a number: -3
# Negative

# ---------------------------------------------------------
# Approach 2: one-line conditional expression
# ---------------------------------------------------------
# print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")

# ---------------------------------------------------------
# Approach 3: using the sign of the number
# ---------------------------------------------------------
# sign = (num > 0) - (num < 0)    # 1, -1 or 0
# print({1: "Positive", -1: "Negative", 0: "Zero"}[sign])

# Edge cases:
# check_number(0)        -> Zero
# check_number(-0.0)     -> Zero  (-0.0 == 0 in Python)
# check_number(10**100)  -> Positive
