"""
------------------------------------------------------------------------
[Addition Quiz]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-10-18"
------------------------------------------------------------------------
"""

# Imports
from random import randint

# Variable
correct = 0
n = 0
total = 0
cont = "Y"

# Script
while cont == "Y":
    n += 1
    a = randint(1, 999)
    print("{:>5}".format(a))
    b = randint(1, 999)
    print("+ {:>3}".format(b))
    total = a + b
    a_b = int(input("= "))
    if a_b == total:
        print("Congratulations!")
        correct += 1
    else:
        print("Sorry, the correct answer is {}".format(total))
    print()
    cont = input("Continue (Y/N): ")


# Output
print()
print("Your final score is {}/{}".format(correct, n))
