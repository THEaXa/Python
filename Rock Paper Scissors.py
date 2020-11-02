import random
from tabulate import tabulate
P_marks = 0
C_marks = 0

def compGuess():
    options = ['R','P','S']
    compChoice = random.choice(options)

    return compChoice

def compMarks():
    global C_marks
    C_marks+=1
    return C_marks

def playerMarks():
    global P_marks
    P_marks+=1
    return P_marks

def play():
    global name
    name = input("Hello There! What's your name?")
    attempts = int(input("How many rounds do you want to play?"))

    print('Welcome to the game {}. Get ready to have a great time' .format(name))

    rounds = 0
    while rounds < attempts:
        playerChoice = input('Make your choice: [R]ock,[P]aper,[S]cissors')
        upper = playerChoice.upper()

        if upper == compGuess():
            print('tie')

        elif upper == 'R' and compGuess() == 'P':
            print('Paper covers the rock. You lose')
            compMarks()

        elif upper == 'P' and compGuess() == 'R':
            print('Paper covers the rock. You win')
            playerMarks()

        elif upper == 'P' and compGuess() == 'S':
            print('Scissors cut paper. You lose')
            compMarks()

        elif upper == 'S' and compGuess() == 'P':
            print('Scissors cut paper. You Win')
            playerMarks()

        elif upper == 'R' and compGuess() == 'S':
            print('Rock breaks scissors. You Win')
            playerMarks()

        elif upper == 'S' and compGuess() == 'R':
            print('Rock breaks scissors. You LOSE')
            compMarks()

        else:
            print('Invalid choice')
        rounds += 1

    print(tabulate([[name, P_marks], ['Computer', C_marks]], headers=['Participants', 'marks']))
    if P_marks > C_marks:
        print("Congratulations!! You win :)")
    elif P_marks == C_marks:
        print("You've not won but it's safe to say that you think like a machine ;)")
    else:
        print("You lose :(")

play()
