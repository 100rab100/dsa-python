# Day 21: Print numbers 1 to n, skipping multiples of 3
# Topic: Basic Programs
# Approach: Loop from 1 to n and print only the numbers where i % 3 != 0
# Time: O(n)  Space: O(1)

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 3 != 0:
        print(i, end=" ")

# Sample run:
# Enter n: 10
# 1 2 4 5 7 8 10

# ---------------------------------------------------------
# Approach 2: using continue  (Time: O(n), Space: O(1))
# ---------------------------------------------------------
# for i in range(1, n + 1):
#     if i % 3 == 0:
#         continue
#     print(i, end=" ")
