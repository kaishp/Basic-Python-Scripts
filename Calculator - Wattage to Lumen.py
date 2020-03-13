"""
------------------------------------------------------------------------
[Lightbulb Wattage]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-10-03"
------------------------------------------------------------------------
"""

wattage = int(input("Lightbulb wattage (w): "))

if wattage == 15:
    print("Brightness: 125 lumens")
elif wattage == 25:
    print("Brightness: 215 lumens")
elif wattage == 40:
    print("Brightness: 500 lumens")
elif wattage == 60:
    print("Brightness: 880 lumens")
elif wattage == 75:
    print("Brightness: 1000 lumens")
elif wattage == 100:
    print("Brightness: 1675 lumens")
else:
    print("Invalid wattage")