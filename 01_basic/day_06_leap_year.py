# Day 06: Check if a year is a leap year
# Topic: Basic Programs
# Approach: Divisible by 4 and not by 100, or divisible by 400
# Time: O(1)  Space: O(1)

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Sample run:
# Enter a year: 2024
# 2024 is a leap year

# ---------------------------------------------------------
# Approach 2: nested if (shows each rule step by step)
# ---------------------------------------------------------
# if year % 400 == 0:
#     print(year, "is a leap year")
# elif year % 100 == 0:
#     print(year, "is not a leap year")
# elif year % 4 == 0:
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")

# ---------------------------------------------------------
# Approach 3: built-in calendar module
# ---------------------------------------------------------
# import calendar
# print(calendar.isleap(year))
