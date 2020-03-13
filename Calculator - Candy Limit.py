"""
------------------------------------------------------------------------
[Candy Calculator]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-10-18"
------------------------------------------------------------------------
"""

# Input
limit = int(input("Mom's limit on the number of candies: "))
first_household = int(input("\nCandies from the first household: "))
total = first_household


# Script
while total < limit:
    next_household = int(input("Candies from the next household: "))
    total += next_household

extra = total - limit

# Output
print("\nYou gathered {} candies in total.".format(total))
print("You have {} candies over Mom's limit".format(extra))
