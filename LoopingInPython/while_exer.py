def userNum():
    """Takes USER input to be used to display ith number of smileys"""
    nums = int(input("Please give an integer: "))
    if((nums == 1) or (nums ==0)):
        nums = int(input("Please give an integer that isn't 0 or 1: "))
    nums += 1
    return nums

def smileyPrint(userInput):
    """Takes int generated from userNum() and displays 
    smileys * int selected by user"""
    for num in range(1, userInput):
        print("\U0001f600" * num)
        
def smileyPrintRev(userInput):
    for num in range(1, userInput):
        print("\U0001f600" * (userInput-num))
    
def main():
    userInput = userNum()
    smileyPrint(userInput)
    print("\U0001f600" * userInput)
    smileyPrintRev(userInput)
 
main()
    