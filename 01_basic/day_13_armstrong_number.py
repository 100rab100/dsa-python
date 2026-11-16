# Day 13: Check if a number is an Armstrong number
# Topic: Basic Programs
# Approach: Add each digit raised to the power of the number of digits, then compare with the original
# Time: O(d)  Space: O(1)   (d = number of digits)

n = int(input("Enter a number: "))

if n < 0:
    print(n, "is not an Armstrong number")
else:
    # Step 1: count the digits
    temp = n
    count = 0
    while temp > 0:
        count += 1
        temp = temp // 10

    # Step 2: add each digit raised to the power of count
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total = total + digit ** count
        temp = temp // 10

    if total == n:
        print(n, "is an Armstrong number")
    else:
        print(n, "is not an Armstrong number")

# Sample run:
# Enter a number: 153
# 153 is an Armstrong number

# ---------------------------------------------------------
# Approach 2: string  (Time: O(d), Space: O(d))
# ---------------------------------------------------------
# n = int(input("Enter a number: "))
# s = str(n)
# total = sum(int(ch) ** len(s) for ch in s)
# print(n, "is an Armstrong number" if total == n else "is not an Armstrong number")
