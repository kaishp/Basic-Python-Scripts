"""
------------------------------------------------------------------------
[Rain-meter]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-11-01"
------------------------------------------------------------------------
"""

# Input
num_years = int(input("Number of years of rainfall: "))
print()
print("Enter rainfall in cm.")
print()


# Variable
total = 0
num_mon = num_years * 12


# Scripts
for i in range(1, num_years + 1):
    print("Year {}".format(i))
    for j in range(1, 13):
        mon = float(input("  Month {:>2}: ".format(j)))
        total += mon

average = total / (num_mon)


# Output
print()
print("Number of months: {}".format(num_mon))
print("Total rainfall: {:.1f} cm".format(total))
print("Average rainfall per month: {:.1f} cm".format(average))
