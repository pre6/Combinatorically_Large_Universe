'''
Code Breaker Game
Version 2: Computer is the Code Maker and User is the Code Maker with possible 
duplicates in the code

1.  Explain Rules
2a. Computer Chooses Code with possible duplicate
2b. Display previous Guess
2c. check cguess
3.  diplay the clues
5.  Repeat Steps 3 and 4 Until the CLues are all black or 12 guesses has passed
6.  End the game
'''

import random

'''
1: Explain the rules
'''

def Beginning():
    print('Welcome to CODEBREAKER! \n')

    print('This is a game where you, the codebreaker have to guess a secret code the codebreaker, the computer has created \n')

    print('You have twelve guesses. The Code is always 5 digits long \n')

    print('After each guess, the computer will provide clues to help you break the code \n')

    print('o: This symbol means that you have guessed the right number but it is in the wrong position \n')

    print('●: This symbol means that you have guessed the right number and it is in the right position \n')

    print('These symbols are in a random order and do not correspond to the order of your guess \n')


'''
2a: Computer Chooses Code with possible Duplicates
'''
def choose_code(max_number, code_length):
    
    Num_Total = list(range(1, max_number + 1))
    # this is the number of the numbers available to use.
    Code = ''
    
    for _ in range(code_length):
        Code += str(random.choice(Num_Total))
        # this randomly pick a number from the total available numbers\
    
    return Code


'''
2b: Display previous guesses

'''
def display_guess(guess_code):
    for thing in guess_code:
        a = " ".join(thing)
        b = guess_code[thing]
        print(a, '|', b )

'''
2c: Check Guess

'''

def Guess(total_guesses,max_num_of_guesses,max_number,code_length):
    Guess = ''
    y = False
    while not(len(Guess)==code_length and y):  
        print('Numbers to Choose from: ')
        print(f"1 to {max_number}")

        g = []
        Guess = input('Please Enter Your Guess: ')
        if len(Guess) != code_length:
            print('You entered a code that is not the right length')
            print('Please Try Again')
        for item in Guess:
            g.append(item)
        K_guess = tuple(g)
        if K_guess in total_guesses:
            y = False
            print('You have already guesses this Code \n')
            print('Please Try Again')
        else:
            y = True
    h = [Guess,K_guess]
    return h


'''
3: calculate clue:

check for doubles    
'''

def Clues(code,guess,code_length):
    print("Take another Guess! \n")
    circle = ''
    check_mark = ''
    i = 0
    while i in range(code_length):
        if code[i] == guess[i]:
            check_mark = check_mark + '● '
            code = code.replace(code[i], ' ',1)
            guess = guess.replace(guess[i], ' ',1)
        i += 1
    for number in code:
        if number ==' ':
            continue
        elif number in guess:
            circle = circle + 'o '
            code = code.replace(number, ' ',1)
            guess = guess.replace(number, ' ',1)
            
    
    clue = circle + check_mark
    return clue



'''
Play Game

'''


def play_game():
    Beginning()
    total_guesses = {}
    print('')

    print("Let's get started! \n")

    print("Hmmm... I am thinking of a code \n")


    # Ask the user for the number of numbers they can select from
    max_number = int(input("Enter the number of numbers you can select from (e.g., 6 for numbers 1-6): "))

    # Ask the user for the length of the code
    code_length = int(input("Enter the length of the code: "))

    max_num_of_guesses = int(input("Enter the length of the code: "))
    code = choose_code(max_number,code_length)
    print(code)

    print('Ok! I got one.\n')
 
    guess_num = 0
    while guess_num < max_num_of_guesses:        
        guess = Guess(total_guesses,max_num_of_guesses,max_number,code_length)
        clue = Clues(guess[0],code,code_length)
        total_guesses[guess[1]] = clue
        guess_num += 1
        if clue == ' '.join(['● '] * code_length) :
            print('Congratulations That was my code')
          
            display_guess(total_guesses)
          
            print('you Guessed it in ', guess_num, ' guesses!')
            break
        else:
            print("Here are your previous Guesses and clues: \n")
            display_guess(total_guesses)
        
            print('You have ', max_num_of_guesses - guess_num, " guesses left \n")
       
            
            continue

    if not(clue == ' '.join(['● '] * max_num_of_guesses)):
        print('You ran out of guesses')
        print('My code was: ', code)


x = play_game()


