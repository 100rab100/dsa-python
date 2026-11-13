# Day 10: Check if a number is a palindrome
# Topic: Basic Programs
# Approach: Reverse the number with a while loop, then compare it with the original
# Time: O(d)  Space: O(1)   (d = number of digits)

n = int(input("Enter a number: "))

original = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10

if original == rev:
    print(original, "is a palindrome number")
else:
    print(original, "is not a palindrome number")

# Sample run:
# Enter a number: 121
# 121 is a palindrome number

# ---------------------------------------------------------
# Approach 2: string slicing  (Time: O(d), Space: O(d))
# ---------------------------------------------------------
# n = input("Enter a number: ")
# if n == n[::-1]:
#     print(n, "is a palindrome number")
# else:
#     print(n, "is not a palindrome number")

# Note: negative numbers are not palindromes (-121 reads as 121-).
