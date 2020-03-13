"""
------------------------------------------------------------------------
[SL Dog Grooming]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-09-27"
------------------------------------------------------------------------
"""

l = int(input('Number of large dogs groomed: '))
s = int(input('Number of small dogs groomed: '))
gl = 75
gs = 50
total = gl * l + gs * s
print('Total earned for the day: {:,.2f}.'.format(total))
