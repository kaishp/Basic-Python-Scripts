"""
------------------------------------------------------------------------
[Projected Profit]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-09-27"
------------------------------------------------------------------------
"""

sales = float(input('Enter projected annual sales: $'))
percentage = 18
profit = sales * 18 / 100
print('The projected profit on sales of ${:,.2f} is ${:,.2f}.'.format(
    sales, profit))
