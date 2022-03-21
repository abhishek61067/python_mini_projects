# develop rock paper scissors game
# display the option for the user to choose on 1 for rock, 2 for paper, 3 for scissors
def options():
    print("1 for rock, 2 for paper, 3 for scissors")


def computerRandomNumberGen():
    import random
    return random.randint(1, 3)


def userinformation():
    print("enter your name")
    name = input()
    print("enter your age")
    age = input()
    print("enter your address")
    address = input()
    print("enter your phonenumber")
    phonenumber = input()


def displayUserChoice(userChoice):
    if userChoice == 1:
        print("user chooses rock")
    elif userChoice == 2:
        print("user chooses paper")
    elif userChoice == 3:
        print("user chooses scissors")
    else:
        print("user chooses invalid input")


def displaycomputerchoice(computerChoice):
    if computerChoice == 1:
        print("computer chooses rock")
    elif computerChoice == 2:
        print("computer chooses paper")
    elif computerChoice == 3:
        print("computer chooses scissors")
    else:
        print("computer chooses invalid input")


def determineWinnerofRPS():
    print("enter your choice")
    userChoice = int(input())
    computerChoice = computerRandomNumberGen()
    displayUserChoice(userChoice)
    displaycomputerchoice(computerChoice)
    if userChoice == computerChoice:
        print("its a tie")
    elif userChoice == 1 and computerChoice == 2:
        print("computer wins")
    elif userChoice == 1 and computerChoice == 3:
        print("user wins")
    elif userChoice == 2 and computerChoice == 1:
        print("user wins")
    elif userChoice == 2 and computerChoice == 3:
        print("computer wins")
    elif userChoice == 3 and computerChoice == 1:
        print("computer wins")
    elif userChoice == 3 and computerChoice == 2:
        print("user wins")
    else:
        print("invalid input")


def main():
    print("welcome to rock paper scissors game")
    options()
    userinformation()
    determineWinnerofRPS()


main()