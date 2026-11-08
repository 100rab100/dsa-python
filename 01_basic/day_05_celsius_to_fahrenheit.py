# Day 5: Convert Celsius to Fahrenheit
# Topic: Basic Programs
# Approach: Apply the formula F = (C * 9 / 5) + 32
# Time: O(1)  Space: O(1)

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(celsius, "C =", round(fahrenheit, 2), "F")

# Sample run:
# Enter temperature in Celsius: 100
# 100.0 C = 212.0 F

# ---------------------------------------------------------
# Approach 2: as a reusable function
# ---------------------------------------------------------
# def celsius_to_fahrenheit(c):
#     return (c * 9 / 5) + 32
#
# print(celsius_to_fahrenheit(37))    # 98.6

# ---------------------------------------------------------
# Reverse conversion (Fahrenheit to Celsius)
# ---------------------------------------------------------
# celsius = (fahrenheit - 32) * 5 / 9
