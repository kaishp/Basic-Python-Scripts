"""
------------------------------------------------------------------------
[Multiplication Table Maker]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-11-01"
------------------------------------------------------------------------
"""
# Variables
n = 0


# Input
start = int(input("Starting value for table: "))
end = int(input("Ending value for table: "))
print()

# Scripts

print(" " * 6, end="")
for i in range(start, end + 1):
    print("{:>5}".format(i), end="")

print()
print(" " * 6 + "-" * 5 * (end - start + 1))

for x in range(start, end + 1):
    print("{:>5}".format(x) + "|", end="")
    for y in range(start, end + 1):
        value = x * y
        print("{:>5}".format(value), end="")
        n += 1
        if n % (end - start + 1) == 0:
            print()
