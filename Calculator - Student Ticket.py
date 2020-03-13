"""
------------------------------------------------------------------------
[Ticket Cost Calculator]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-09-27"
------------------------------------------------------------------------
"""
cost = float(input('Cost of movie: $'))
discount = 20
new_cost = cost - cost * discount / 100
print('The cost of the movie for a student is ${:,.2f}.'.format(new_cost))
