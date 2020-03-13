"""
------------------------------------------------------------------------
[Colour Mix]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-10-04"
------------------------------------------------------------------------
"""

c1 = input("Enter first colour: ")
c2 = input("Enter second colour: ")

if (c1 == "red" and c2 == "blue") or (c1 == "blue" and c2 == "red"):
    print("Secondary colour is purple")
elif (c1 == "red" and c2 == "yellow") or (c1 == "yellow" and c2 == "red"):
    print("Secondary colour is orange")
elif (c1 == "blue" and c2 == "yellow") or (c1 == "yellow" and c2 == "blue"):
    print("Secondary colour is green")
else:
    print("No secondary colour")