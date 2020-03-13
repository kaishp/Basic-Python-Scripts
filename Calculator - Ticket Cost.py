"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-10-18"
------------------------------------------------------------------------
"""

# Constants
SENIOR_AGE = 65
SENIOR_PRICE = 4.0
ADULT_AGE = 18
ADULT_PRICE = 5.0
INFANT_AGE = 3
INFANT_PRICE = 0
STUDENT_AGE_LO = 10
STUDENT_AGE_HI = 15
STUDENT_PRICE = 1.0
KID_PRICE = 2.0

# Variable
total = 0

# Input
purchase = input("Purchase a ticket (Y/N)? ")


# Script
while purchase == "Y":
    age = int(input("How old are you? "))
    if age >= SENIOR_AGE:
        print("That ticket costs ${:.2f}".format(SENIOR_PRICE))
        total += SENIOR_PRICE
        purchase = input("Purchase a ticket (Y/N)? ")
    elif ADULT_AGE <= age < SENIOR_AGE:
        print("That ticket costs ${:.2f}".format(ADULT_PRICE))
        total += ADULT_PRICE
        purchase = input("Purchase a ticket (Y/N)? ")
    elif INFANT_AGE >= age:
        print("That ticket costs ${:.2f}".format(INFANT_PRICE))
        total += INFANT_PRICE
        purchase = input("Purchase a ticket (Y/N)? ")
    else:
        if STUDENT_AGE_LO <= age <= STUDENT_AGE_HI:
            school = input("Are you a student at this school? (Y/N): ")
            if school == "Y":
                print("That ticket costs ${:.2f}".format(STUDENT_PRICE))
                total += STUDENT_PRICE
            else:
                print("That ticket costs ${:.2f}".format(KID_PRICE))
                total += KID_PRICE
        else:
            print("That ticket costs ${:.2f}".format(KID_PRICE))
            total += KID_PRICE
        purchase = input("Purchase a ticket (Y/N)? ")

# Output
print()
print("Total tickets price: ${:.2f}".format(total))
