"""
------------------------------------------------------------------------
[Integer Identity]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-11-01"
------------------------------------------------------------------------
"""

# Input
num = int(input("Number of values: "))
print()
value = int(input("First value: "))

# Variables
neg = 0
zero = 0
pos = 0
even = 0
odd = 0
total = 0
minimum = value
maximum = value

# Scripts
for i in range(1, num + 1):
    total += value
    if value < 0:
        neg += 1
    elif value > 0:
        pos += 1
    else:
        zero += 1

    if value % 2 == 0:
        even += 1
    else:
        odd += 1

    if value < minimum:
        minimum = value
    elif value > maximum:
        maximum = value

    if i == num:
        break
    else:
        value = int(input("Next value: "))


average = total / num


# Output
print()
print("Negative values: {:>5}".format(neg))
print("Zero values: {:>9}".format(zero))
print("Positive values: {:>5}".format(pos))
print("Even values: {:>9}".format(even))
print("Odd values: {:>10}".format(odd))
print("Total: {:>15}".format(total))
print("Minimum: {:>13}".format(minimum))
print("Maximum: {:>13}".format(maximum))
print("Average: {:>16.2f}".format(average))
