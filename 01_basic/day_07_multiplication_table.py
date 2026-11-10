# Day 07: Print the multiplication table of n
# Topic: Basic Programs
# Approach: Loop from 1 to 10 and print n * i
# Time: O(1) for a fixed table of 10 rows (O(k) for k rows)  Space: O(1)


n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

# Sample run:
# Enter a number: 5
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50

# ---------------------------------------------------------
# Approach 2: f-string with aligned columns
# ---------------------------------------------------------
# for i in range(1, 11):
#     print(f"{n} x {i:2} = {n * i:4}")

# ---------------------------------------------------------
# Approach 3: while loop
# ---------------------------------------------------------
# i = 1
# while i <= 10:
#     print(n, "x", i, "=", n * i)
#     i += 1

# ---------------------------------------------------------
# Approach 4: table up to a limit chosen by the user
# ---------------------------------------------------------
# limit = int(input("Table up to: "))
# for i in range(1, limit + 1):
#     print(n, "x", i, "=", n * i)
