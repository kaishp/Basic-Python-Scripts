"""
------------------------------------------------------------------------
[Diamond Pattern-maker]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-11-01"
------------------------------------------------------------------------
"""

# Input
w = int(input("Width of diamond: "))
char = input("Printing character: ")
print()
# Scripts

if w % 2 == 0:
    for i in range(2, w, 2):
        print(" " * ((w - i) // 2) + char * i)

else:
    for i in range(1, w, 2):
        print(" " * ((w - i) // 2) + char * i)

for j in range(w, 0, -2):
    print(" " * ((w - j) // 2) + char * j)
