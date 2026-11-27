# Day 23: Print a square pattern of stars
# Topic: Basic Programs
# Approach: Outer loop for rows, inner loop for columns, print a star in each cell
# Time: O(n^2)  Space: O(1)

n = int(input("Enter size of the square: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# Sample run (n = 4):
# * * * *
# * * * *
# * * * *
# * * * *

# ---------------------------------------------------------
# Approach 2: string multiplication  (Time: O(n^2), Space: O(n))
# ---------------------------------------------------------
# for i in range(n):
#     print("* " * n)
