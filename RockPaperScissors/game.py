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

#========= Main =========#
playerScore = 0
computerScore = 0
playerChoice = ""
winningScore = 3

print("=============================")
print("Are you ready to play..? (Best of 3")
print("...rock...")
print("...paper...")
print("...scissors...")
print("=============================")
while (playerScore < winningScore and computerScore < winningScore):
    if ((playerChoice != "rock") or (playerChoice != "paper") or (playerChoice != "scissors") or (playerChoice != "quit")):
        playerChoice = input("Please select rock, paper, or scissors (or type quit to quit)...")   
        if (playerChoice.lower() == "quit"):
            break
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
    print(f"Your score: {playerScore} ::: Computer's score: {computerScore}")
    print("=============================================")
if (playerScore > computerScore):
    print("CONGRATS! You won!")
elif (playerScore < computerScore): 
    print("OH NO, you lost...")
elif (playerScore == computerScore):
    print("IT'S A TIE!")
else:
    print("Thanks for playing!")
print(f"FINAL SCORES: Your score: {playerScore} ::: Computer's score: {computerScore}")
