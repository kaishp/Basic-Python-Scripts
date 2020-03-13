"""
------------------------------------------------------------------------
[Cylinder Container Cost Calculator]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-09-27"
------------------------------------------------------------------------
"""

d = float(input('Diameter of container base (cm): '))
h = float(input('Height of container (cm): '))
per_cost = float(input('Cost of material ($/cm^2): '))
num_of_cont = int(input('Number of containers: '))

PI = 3.14
r = d / 2
circle = PI * (r**2)
rect = PI * d * h
surf_area = circle + rect

cost = surf_area * per_cost
total = num_of_cont * cost

print('The cost of one container is: ${:,.2f}'.format(cost))
print('The total cost of all containers is ${:,.2f}'.format(total))
