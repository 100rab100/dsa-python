# Day 22: FizzBuzz for 1 to n
# Topic: Basic Programs
# Approach: For each number, check 15 first, then 3, then 5, otherwise print the number
# Time: O(n)  Space: O(1)

n = int(input("Enter n: "))

for i in range(1, n + 1):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Sample run (n = 15):
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz

# ---------------------------------------------------------
# Approach 2: build the word from parts  (Time: O(n), Space: O(1))
# ---------------------------------------------------------
# for i in range(1, n + 1):
#     word = ""
#     if i % 3 == 0:
#         word += "Fizz"
#     if i % 5 == 0:
#         word += "Buzz"
#     print(word or i)
