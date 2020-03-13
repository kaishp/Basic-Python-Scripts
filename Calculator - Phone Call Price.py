"""
------------------------------------------------------------------------
[Happy Customer Phone Company]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-10-04"
------------------------------------------------------------------------
"""


length = int(input("Length of call (minutes): "))
hour_of_call = int(input("Hour of call (24 hour format): "))
base_price = 0.08
price_1 = base_price * length


if (hour_of_call >= 18 and hour_of_call < 24):
    if (hour_of_call < 30):
        price = price_1 - 0.25 * price_1
        print("Total price of call: ${:.2f}".format(price))
    else:
        price = price_1 - ((25 / 100) * price_1)
        price_2 = price - ((10 / 100) * price)
        print("Total price of call ${:.2f}".format(price_2))

elif (hour_of_call >= 0 and hour_of_call < 8 or hour_of_call == 24):
    if (length < 30):
        price = price_1 - ((50 / 100) * price_2)
        print('Total price of call: ${:.2f}'.format(price))
    else:
        price = price_1 - ((50 / 100) * price_1)
        price_2 = price - ((10 / 100) * price)
        print('Total price of call: ${:.2f}'.format(price_2))

else:
    if (length < 30):
        print('Total price of call: ${:.2f}'.format(price_1))
    else:
        price = price - ((10 / 100) * price)
        print('Total price of call: ${:.2f}'.format(price_2))
