import random
def valid_num(s):
    if s.isdigit() and 1<= int(s) <=100 :
        return True
    else:
        return False


def Guess_Number():
    num =  random.randint(20,40)
    Guessed_Num =  False
    guess= input("Guess a number between 1 and 100")
    number_of_guesses = 0
    while not Guessed_Num:
        if not valid_num(guess):
            guess=input("The number entered is invalid...Please enter a number between 1 and 100")
            continue
        else:
            number_of_guesses+=1
            guess = int(guess)
        if guess < num:
           guess = input("Your guess is lower than the actual number.Guess Again:")
        elif guess > num:
             guess = input("Your guess is higher than the actual number.Guess Again")
        else:
             print("Wow!You have guessed in",number_of_guesses,"guesses!")
             Guessed_Num = True
   
    print("Thanks for playing")

Guess_Number()

