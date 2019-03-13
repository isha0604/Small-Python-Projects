#Program for Rock(r) , Paper(p) and Scissor(s) Game
""" Game Rules
    1.Rock blunts scissors
    2.Paper covers rock
    3.Scissors cut paper"""

from random import randint
#Player's Turn
print('Enter your Choice:')
player = input('Rock(r),Paper(p) or Scissor(s)?')
#print(player,'vs')

#Computer's Turn
print('Now it\'s computer\'s turn')
choice = randint(1,3)
if choice == 1:
    computer = 'r'
elif choice == 2:
    computer = 'p'
else:
    computer = 's'

print('Computer has chosen',computer)
print('So now the players are',player,'vs',computer)

if(player == computer):
    print('It\'s a DRAW!')
elif(player == 'r' and computer == 'p'):
    print('computer Wins')
elif (player == 'r' and computer == 's'):
    print('player Wins')
elif (player == 'p' and computer =='r'):
    print('player Wins')
elif (player == 'p' and computer == 's'):
    print('computer Wins')
elif (player == 's' and computer == 'r'):
    print('computer Wins')
elif (player == 's' and computer == 'p'):
    print('player Wins')
