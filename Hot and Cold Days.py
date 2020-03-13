"""
------------------------------------------------------------------------
[Hot & Cold Days]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-10-18"
------------------------------------------------------------------------
"""

# Constants
SENTINEL = -500
HOT_DAYS = 27
COLD_DAYS = 17

# Variables
temp = int(input("Temperature C (-500 to stop): "))
hot_days = 0
pleasant_days = 0
cold_days = 0
n = 0
total = 0

# Script
while temp != SENTINEL:
    n += 1
    total += temp
    if temp > HOT_DAYS:
        hot_days += 1
    elif temp <= COLD_DAYS:
        cold_days += 1
    else:
        pleasant_days += 1
    temp = int(input("Temperature C (-500 to stop): "))
average = total / n

# Output
print("\nCold days: {:8} \nPleasant days: {:4} \nHot days: {:9} \nAverage: {} C".format(
    cold_days, pleasant_days, hot_days, int(average)))
