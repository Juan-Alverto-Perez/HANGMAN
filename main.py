import os


def printStand(status):

    match status:
        case 0:
            print(" -------------")
            print(" |           |")
            print(" |           |")
            print(" |")
            print(" |" )
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("----\n")
        case 1:
            print(" -------------")
            print(" |           |")
            print(" |           |")
            print(" |           O")
            print(" |" )
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("----\n")
        case 2:
            print(" -------------")
            print(" |           |")
            print(" |           |")
            print(" |           O")
            print(" |           |" )
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("----\n")
        case 3:
            print(" -------------")
            print(" |           |")
            print(" |           |")
            print(" |           O")
            print(" |           |-" )
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("----\n")

        case 4:
            print(" -------------")
            print(" |           |")
            print(" |           |")
            print(" |           O")
            print(" |          -|-" )
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("----\n")

        case 5:
            print(" -------------")
            print(" |           |")
            print(" |           |")
            print(" |           O")
            print(" |          -|-" )
            print(" |            |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("----\n")
        case 6:
            print(" -------------")
            print(" |           |")
            print(" |           |")
            print(" |           O")
            print(" |          -|-" )
            print(" |          | |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("----\n")
    update() 
    print("\n")

    print('Wrong guesses:')
    for x in wrongGuesses:
        print (f"{x}", end=' ')
    print("\n")

def getLetter():
    
    guess = input('Guess a letter:')
    while 1 < 2:
        if guess in wrongGuesses:
            print("You already guessed that try again")
            guess = input('Guess a letter:')
        elif len(guess)> 1:
            print('Only one letter at a time!')
            guess = input('Guess a letter:')
        else:
            break
    
    return guess
    
def update():
    for x in word:
        y = '_'
        if x in rightGuesses:
            print (f"{x} ", end='')
        else:
            print (f"{y} ", end='')

def checkGuess(guess, status):
    
    clear()
    if guess in word:
        print('That\'s right!\n')
        rightGuesses.append(guess)
    else:
        print('THATS NOT IN THE WORD!\n')
        wrongGuesses.append(guess)
        status += 1
        
    return status

def clear():
       os.system('cls')
        

###
status = 0

global word
word = ''

guess = ''

global lettersGuessed
lettersGuessed = 0

wrongGuesses = []

global rightGuesses
rightGuesses = []
###




word = input("Word to guess:").lower()
clear()
while(status !=6):
    
    printStand(status)
    guess = getLetter()
    status = checkGuess(guess, status)

clear()
print('YOU LOST!! LOSER')
print(f'The word was {word}')
       








