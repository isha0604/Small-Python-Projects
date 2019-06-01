story = ''' A vacation is when you take a trip to
some {} place with your {} family.
Usually,go to some place
that is near a/an {} or up on a/an {}.A good vacation place is one where you can ride {} or play {}.'''

def madlibs():
    adjectives = []
    adjectives.append(input("Enter an adjective"))
    adjectives.append(input("Enter an adjective"))
     
    nouns = []
    nouns.append(input("Enter a noun"))
    nouns.append(input("Enter a noun"))

    animal = input("Enter animal in plural form")
    game = input("Enter a game")

    mad_lib = story.format(adjectives[0],adjectives[1],nouns[0],nouns[1],animal,game)


    print(mad_lib)



madlibs()


