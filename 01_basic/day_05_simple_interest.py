# Day 5: Calculate simple interest
# Topic: Basic Programs
# Approach: Apply the formula SI = (P * R * T) / 100
# Time: O(1)  Space: O(1)

def simple_interest(principal, rate, time):
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate and time must be non-negative")
    return (principal * rate * time) / 100


p = float(input("Enter principal amount: "))
r = float(input("Enter annual rate of interest (%): "))
t = float(input("Enter time (in years): "))

si = simple_interest(p, r, t)
print("Simple Interest =", si)
print("Total Amount =", p + si)

# Sample run:
# Enter principal amount: 1000
# Enter annual rate of interest (%): 5
# Enter time (in years): 2
# Simple Interest = 100.0
# Total Amount = 1100.0

# ---------------------------------------------------------
# Approach 2: without a function
# ---------------------------------------------------------
# si = (p * r * t) / 100
# print("Simple Interest =", si)
