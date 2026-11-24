# Day 19: Print the first n even numbers
# Topic: Basic Programs
# Approach: The k-th even number is 2 * k, so loop from 1 to n and print 2 * i
# Time: O(n)  Space: O(1)

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(2 * i, end=" ")

# Sample run:
# Enter n: 5
# 2 4 6 8 10

# ---------------------------------------------------------
# Approach 2: range with a step of 2  (Time: O(n), Space: O(1))
# ---------------------------------------------------------
# for num in range(2, 2 * n + 1, 2):
#     print(num, end=" ")
