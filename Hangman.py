import random
def chosen_word():
    words= ['apple','banana','broccoli','cauliflower','beetroot','fox','dog','girrafe']
    return random.choice(words).upper()

def check(word,guesses,guess):
    #guess=guess.upper()
    status = ''
    #i=0
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else :
            status+='*'
        if letter == guess:
            matches+= 1
    if matches > 1:
        print("Yes the word contains",matches,'"'+guess+'"'+ 's')
    elif matches == 1:
        print("Yes the word contains the letter",'"' +guess+'"')
    else:
        print("Sorry ,The word doesnot contain the letter")
    
    return status

def main():
    word = chosen_word()
    guesses = []
    guessed=False
    print('The word contains', len(word),'letters')
    while not guessed:
        text = 'Please enter one letter or a {}-letter word.'.format(len(word))
        guess=input(text)
        guess=guess.upper()
        if guess in guesses:
            print('You have already guessed "' + guess + '"')
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print("The guess is incorrect")
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word,guesses,guess)
            if result == word:
                guessed = True
            else: 
               print(result)
        else:
            print('Inavlid Entry')
   
    print("Bingo! You have guessed the word  ", word+  'in' , len(guesses),'tries' )


main()