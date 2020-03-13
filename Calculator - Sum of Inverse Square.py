"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-11-01"
------------------------------------------------------------------------
"""

# Input
num = int(input("Number (>=1): "))
print()
total = 0

# Scripts
for i in range(1, num + 1, 1):
    total += 1 / (i**2)

# Output
print("Sum of inverse squares for {} = {}".format(num, total))
