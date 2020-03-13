"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-10-18"
------------------------------------------------------------------------
"""
# Constant
MIN = 90

# Input
budget = float(input("Party budget: $"))
print()

# Variable
another_item = "Y"
spent = 0
remain = budget

# Script
minimum = (MIN / 100) * budget

while spent < budget and another_item == "Y":
    cost = float(input("Cost of item: $"))
    remain = budget - spent
    spent += cost
    if spent > budget:
        print(
            "Item costs too much: ${:.2f} remaining in budget".format(remain))
        spent -= cost
        another_item = input("Buy another item (Y/N): ")
        if another_item != "Y" and spent < minimum:
            print(
                "Have not yet spent the minimum amount: ${:.2f}".format(minimum))
            another_item = "Y"
    elif spent < budget:
        another_item = input("Buy another item (Y/N): ")
        if another_item == "N" and spent < minimum:
            print(
                "Have not yet spent the minimum amount: ${:.2f}".format(minimum))
            another_item = "Y"

remain = budget - spent

# Output
print()
print("Total spent on items: ${:.2f}".format(spent))
print("Amount remaining: ${}".format(remain))
