"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Kaish
__updated__ = 2018-09-19
------------------------------------------------------------------------
"""

x = float(input("Cost of 1 pizza: $"))
y = int(input("Number of pizzas: "))
total = x * y

print("Total cost of {} pizzas: ${:.2f}".format(y, total))
