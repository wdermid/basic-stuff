#guessinggame.py

playAgain = "Y"
while (playAgain == "Y"):
    print("This is a guessing game where the computer will attempt to guess " +
          "your number in the least amount of tries as possible.\n")

    upper = 0
    lower = 0
    upperSign = 1
    lowerSign = 1
    while (upper <= lower):
        print("Upper range boundary must be greater than lower.\n")
        upper = input("Enter an upper range boundary: ")
        if (upper[0] == "-"):
            upperSign = -1
            upper = upper[1:len(upper)]
        while (not upper.isnumeric()):
            upper = input("Invalid entry.\nEnter an upper range boundary: ")
            
        lower = input("Enter a lower range boundary: ")
        if (lower[0] == "-"):
            lowerSign = -1
            lower = lower[1:len(lower)]
        while (not lower.isnumeric()):
            lower = input("Invalid entry.\nEnter a lower range boundary: ")

        upper = upperSign * int(upper)
        lower = lowerSign * int(lower)

    upper = upper
    lower = lower - 1
    answer = ""
    while ((upper - lower) > 1 and answer != "Q"):
            answer = input("Greater than " + str((upper-lower)//2+lower) + "? (Y/N/Q to quit)\n").upper()
            if (answer == "Y"):
                    lower = (upper-lower)//2+lower
            elif (answer == "N"):
                    upper = (upper-lower)//2+lower

    if (answer == "Y"):
        print("Your number is " + str(lower+1))
    elif (answer == "N"):
        print("Your number is " + str(upper))

    playAgain = input("\nPlay again? (Y/N)").upper()
    while(playAgain != "Y" and playAgain != "N"):
        playAgain = input("\nPlay again? (Y/N)").upper()
