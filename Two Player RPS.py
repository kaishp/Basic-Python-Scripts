"""
------------------------------------------------------------------------
[Rock, Paper or Scissors]
------------------------------------------------------------------------
Author: Kaish
__updated__ = "2018-10-04"
------------------------------------------------------------------------
"""

p1 = input("Enter Player 1 choice (R, P, or S): ")
p2 = input("Enter Player 1 choice (R, P, or S): ")

if (p1 == 'R' and p2 == 'S'):
    print('Rock beats scissors! Player 1 wins.')
elif (p1 == 'S' and p2 == 'P'):
    print('Scissors beats paper! Player 1 wins.')
elif (p1 == 'P' and p2 == 'R'):
    print('Paper beats rock! Player 1 wins.')
elif (p2 == 'R' and p1 == 'S'):
    print('Rock beats scissors! Player 2 wins.')
elif (p2 == 'S' and p1 == 'P'):
    print('Scissors beats paper! Player 2 wins.')
elif (p2 == 'P' and p1 == 'R'):
    print('Paper beats rock! Player 2 wins.')
else:
    print('A tie!')
