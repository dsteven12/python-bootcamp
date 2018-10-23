import random

#========= Function Definitions =========#
def compareChoices(playerChoice, computerChoice):
    """Compares player values to computer values and declares winner"""
    tieGame = "You've come to a draw!"
    youWon = "You won!"
    compWon = "The Computer won the game!"
    if(playerChoice == computerChoice): 
        return tieGame
    else: 
        if(playerChoice == "rock"):
            if(computerChoice == "paper"):
                return compWon
            else:
                return youWon
        elif(playerChoice == "paper"):
            if(computerChoice == "rock"):
                return youWon
            else:
                return compWon
        else:
            if(computerChoice == "rock"):
                return compWon
            else:
                return youWon
            
def convertChoice(computerChoice):
    """Convert Random INT into rock, paper, or scissors"""
    if(computerChoice == 1):
        computerChoice = "rock"
    elif(computerChoice == 2):
        computerChoice = "paper"
    else: 
        computerChoice = "scissors"
    return computerChoice

#========= Main =========#
print("=============================")
print("Are you ready to play..?")
print("...rock...")
print("...paper...")
print("...scissors...")
print("=============================")
playerChoice = input("Please select rock, paper, or scissors...")
print("=============================")
print("You chose " + playerChoice + ".")
computerChoice = random.randint(1,3)
computerChoice = convertChoice(computerChoice)
print("The computer chose " + computerChoice + ".")
print("=============================================")
print(compareChoices(playerChoice, computerChoice))
print("=============================================")
