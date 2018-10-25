# str = "CLEAN UP YOUR ROOM!"
# times = int(input("How many times do I have to tell you?..."))

# for time in range(times):
#     print(str)
    
for num in range(1,21):
    if (num == 4 or num == 13):
        state = "UNLUCKY!!!"
    elif (num % 2 == 0):
        state = "Even"
    else:
        state = "oDd"
    print(f"{num} is {state}")