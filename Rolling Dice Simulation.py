import random



def roll_the_dice():
    sides=6
    print("rolling the dices...")
    print("The values rolled are...")
    print(random.randint(1,sides),'and',random.randint(1,sides))
   

def main():
    playing=True
    while playing:
        play_again= input("Would you like to play again?")
        if play_again=='yes' or play_again=='y':
           roll_the_dice()
        else: break
        
    print("Bingo!You dont want to play the game anymore")
    print("Thanks for playing")
    
main()   




