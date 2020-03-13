"""
------------------------------------------------------------------------
[Population Calculator]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-10-18"
------------------------------------------------------------------------
"""

# Variable
n = 0
rate = 1 / 10
# Input
current_population = int(input("Current population: "))
growth_rate = float(input("Growth Rate (%): "))
target_population = int(input("Target Population: "))

# Script
while current_population <= target_population:
    n += 1
    current_population += (current_population * 1 / 10)


# Output
print()
print("It will take {} year(s) to reach the target population.".format(n))
