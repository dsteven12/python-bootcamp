import random

#========= Var Definitions =========#
str1 = "You"

#========= Function Definitions =========#
def compareChoices(playerChoice, computerChoice):
    """Compares player values to computer values and declares winner"""
    tieGame = "It's a draw! No one won :("
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
        elif(playerChoice == "scissors"):
            if(computerChoice == "rock"):
                return compWon
            else:
                return youWon
        else:
            return "No choice given."
            
def convertChoice(computerChoice):
    """Convert Random INT into rock, paper, or scissors"""
    if(computerChoice == 1):
        computerChoice = "rock"
    elif(computerChoice == 2):
        computerChoice = "paper"
    else: 
        computerChoice = "scissors"
    return computerChoice

def givePoints(winner, playerScore, computerScore):   
    if (winner.find('you') != -1):
        return playerScore + 1
    elif (winner.find('draw') != -1):
        return
    else: 
        return computerScore + 1
            

#========= Main =========#
playerScore = 0
computerScore = 0
playerChoice = ""
winner = ""

print("=============================")
print("Are you ready to play..?")
print("...rock...")
print("...paper...")
print("...scissors...")
print("=============================")
while (playerChoice != "quit"):
    playerChoice = input("Please select rock, paper, or scissors (or type 'quit' to quit)...")
    if (playerChoice != "quit"):
        if ((playerChoice != "rock") or (playerChoice != "paper") or (playerChoice != "scissors")):
            playerChoice = input("Please select rock, paper, or scissors (or type quit to quit)...")   
    print("=============================")
    print("You chose " + playerChoice + ".")
    computerChoice = random.randint(1,3)
    computerChoice = convertChoice(computerChoice)
    print("The computer chose " + computerChoice + ".")
    print("=============================================")
    winner = compareChoices(playerChoice, computerChoice)
    print(winner)
    winner = winner.lower()
    if (winner.find('you') != -1):
        playerScore += 1
    elif (winner.find('computer') != -1):
        computerScore += 1
    else: 
        print("Tie Game, no one received points!")
    print(f"Your score is {playerScore}")
    print(f"The computer's score is {computerScore}")
    print("=============================================")
