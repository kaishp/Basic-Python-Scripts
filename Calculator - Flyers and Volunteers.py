"""
------------------------------------------------------------------------
[Flyers & Volunteers]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-09-27"
------------------------------------------------------------------------
"""

fly = int(input('Number of flyers: '))
vol = int(input('Number of volunteers: '))
fl = fly % vol
fpv = fly // vol
print('Flyers per volunteer: {}'.format(fpv))
print('Flyers left over: {}'.format(fl))
