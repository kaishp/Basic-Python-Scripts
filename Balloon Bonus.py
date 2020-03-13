"""
------------------------------------------------------------------------
[Balloon Bonus]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-10-03"
------------------------------------------------------------------------
"""

collected = int(input("Balloons collected: "))

if collected == 1:
    bonus_point = 10

elif collected == 2:
    bonus_point = 25

elif collected >= 3:
    bonus_point = 50

else:
    bonus_point = 0

print("Bonus points earned: {}".format(bonus_point))
