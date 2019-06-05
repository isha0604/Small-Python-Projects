import random

def msg(room):
     if room['msg'] =='':
         return "You have entered the" + room['name'] + '.'
     else:
         return room['msg']

def get_choice(room,dir):
    if dir =='N':
        choice = 0
    elif dir == 'E':
        choice = 1
    elif dir == 'S':
         choice = 2
    elif dir == 'W':
        choice = 3
    else:
        return -1


    if room['directions'][choice] == 0:
        return 4
    else:
        return choice

def main():
    dirs = (0,0,0,0)

    entrance = {'name':'Entrance Way','directions':dirs,'msg':''}
    livingroom = {'name':'Living Room','directions':dirs,'msg':''}
    hallway = {'name':'Hallway','directions':dirs,'msg':''}
    kitchen = {'name':'Kitchen','directions':dirs,'msg':''}
    diningroom = {'name':'Dining Room','directions':dirs,'msg':''}
    familyroom = {'name': 'Family Room','directions':dirs,'msg':''}

    entrance['directions'] = (kitchen,livingroom,0,0)
    livingroom['directions'] = (diningroom,0,0,entrance)
    hallway['directions'] = (0,kitchen,0,familyroom)
    kitchen['directions'] = (0,diningroom,entrance,hallway)
    diningroom['directions'] = (0,0,livingroom,kitchen)
    familyroom['directions'] = (0,hallway,0,0)

    rooms = [livingroom,hallway,kitchen,diningroom,familyroom]
    room_having_milk = random.choice(rooms)
    milk_delivered = False
    room = entrance

    print('Welcome Dear!Can you find russel\'s basket?')

    while True:
         if milk_delivered and room['name'] == 'Entrance Way':
            print("You have delivered the milk and back to the entrance " + "You can now leave.Good Work!")
            break;

         elif not milk_delivered  and room['name'] == room_having_milk['name']:
              milk_delivered = True
              print(msg(room) + 'There is the basket and russel is sleeping right next to it!'
                 + 'You have delivered the milk!' + 'Now get out quick! ')
              room['msg'] = ('You are back in the' + room['name'] +
                             'You already delivered the milk.' + 'Get out of here before russel wakes up')
         else:
              print(msg(room))
              room['msg'] = "You are back in the" + room['name']

         stuck =  True
         while stuck:
                    dir = input("Which direction would you want to go: N,E,S or W?")
                    choice = get_choice(room,dir)
                    if choice == -1:
                          print('Please enter N,E,S or W?')
                    elif choice == 4:
                         print("You cannot go in that direction")
                    else:
                        room = room['directions'][choice]
                        stuck = False
main()





 