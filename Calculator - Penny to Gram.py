"""
------------------------------------------------------------------------
[Penny - Gram Converter]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-11-01"
------------------------------------------------------------------------
"""

# Constants
CONVERSION = 1.5552


print("Pennyweight to grams Conversion")
a = "Pennyweight"
b = "Grams"


# Input
start = int(input("Start: "))
limit = int(input("Limit: "))
incre = int(input("Increment: "))
print()


# Scripts
print("{:<11} {:>9}".format(a, b))
print("-" * 11, "-" * 9)
for i in range(start, limit + 1, incre):
    g = i * CONVERSION
    print("{:>11} {:>9.4f}".format(i, g))
