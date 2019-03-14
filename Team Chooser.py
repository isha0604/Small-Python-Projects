#Program to create two random teams from a list of players
#In this we are taking player names and team names from two files which are uploaded in the same repository for reference with names 'players.txt' and 'teamNames'.txt

from random import choice
#players = ['Harry','Rahul','Mukesh','Bob','Catty','Paul']
players = []
file = open('players.txt','r')
players = file.read().splitlines()
file = open('teamNames.txt','r')
teamNames = file.read().splitlines()
#teamNames = ['Lakers','Braves','Warriors','Eagles','Bears','Yankies']
print('The teams are:',teamNames)
print('The Players are:',players)
tmA = choice(teamNames)
teamNames.remove(tmA)
print('The first team is:',tmA)
print('The teams left are:',teamNames)
tmB = choice(teamNames)

print('The second team is:',tmB)
teamA = []
teamB = []

while len(players) > 0:
           player1 = choice(players)
           print('The chosen players is:',player1)
           teamA.append(player1)
           players.remove(player1)


           #for odd number of players
           if players == []:
               print('No Players left now')
               break
           print('Players left are:', players)
           player2 = choice(players)
           print('The chosen players is:',player2)
           teamB.append(player2)
           players.remove(player2)
           print('Players left are:',players)
print('Players in', tmA,' are',teamA)
print('Players in',tmB,' are',teamB)
