# Day 06: Find the area of a circle
# Topic: Basic Programs
# Approach: Apply the formula Area = pi * r * r using math.pi
# Time: O(1)  Space: O(1)

import math

r = float(input("Enter the radius: "))

if r < 0:
    print("Radius cannot be negative")
else:
    area = math.pi * r * r
    print("Area of the circle =", round(area, 2))

# Sample run:
# Enter the radius: 5
# Area of the circle = 78.54

# ---------------------------------------------------------
# Approach 2: using the power operator
# ---------------------------------------------------------
# area = math.pi * r ** 2

# ---------------------------------------------------------
# Bonus: circumference
# ---------------------------------------------------------
# circumference = 2 * math.pi * r
