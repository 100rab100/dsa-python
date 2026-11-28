# Day 24: Print a right-angled triangle star pattern
# Topic: Basic Programs
# Approach: Outer loop for rows, inner loop prints i stars in row i
# Time: O(n^2)  Space: O(1)

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Sample run (n = 5):
# *
# * *
# * * *
# * * * *
# * * * * *

# ---------------------------------------------------------
# Approach 2: string multiplication  (Time: O(n^2), Space: O(n))
# ---------------------------------------------------------
# for i in range(1, n + 1):
#     print("* " * i)
