"""
------------------------------------------------------------------------
[Loan Calculator]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-09-27"
------------------------------------------------------------------------
"""
P = float(input('Amount borrowed: $'))
r = float(input('Interest rate: '))
m = int(input('Length of loan (months): '))

i = r / 100
x = (P * i) / 12
y = 1 - (1 + (i / 12))**-m
payment = x / y


print('The monthly payment is ${:,.2f}.'.format(payment))
