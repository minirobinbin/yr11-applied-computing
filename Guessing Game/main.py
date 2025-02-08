from random import randint

guesses = 0

def guess(number, guesses):
    user_guess = input('\n')
    if user_guess.lower() == number:
        print('WOW! Correct!')
        guesses = 0
        return
    else:
        if guesses == 5:
            print('Sadly, you got all your 5 guesses wrong, you lost!')
            guesses = 0
            return
        else:
            guessNumber = 5 - guesses
            print(f'Wrong... try again! You have {guessNumber} guess left!')
            guesses = guesses + 1
            guess(number, guesses)

def intro(guesses):
    intro = input('Welcome! Would you like to start a new game of the guessing game?(y/n)\n')
    if intro.lower() == 'y':
        print('Okay! Lets start a new game...')
        number = str(randint(1, 9))
        #print(f'{number}')
        guess1 = input('What is your first guess?\n')
        if guess1.lower() == number:
            print('WOW! Correct on the first try!')
            guesses = 0
            return
        else:
            guessNumber = 5 - guesses
            print(f'Wrong... try again! You have {guessNumber} left!')
            guesses = guesses + 1
            guess(number, guesses)
    else:
        print('okay...bye bye :(')

intro(guesses)
