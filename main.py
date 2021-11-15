import random

def m8b():
    # Input for the question
    question = input("\nEnter your question for the 8 ball here: ")

    num = random.randint(1,20)

    # 20 Responses --> taken from wikepdia
    if num == 1:
        print("\nIt is certain")
    elif num == 2:
        print("\nIt is decidely so")
    elif num == 3:
        print("\nWithout a doubt")
    elif num == 4:
        print("\nYes, definitely")
    elif num == 5:
        print("\nYou may rely on it")
    elif num == 6:
        print("\nAs I see it, yes")
    elif num == 7:
        print("\nMost likely")
    elif num == 8:
        print("\nOutlook good")
    elif num == 9:
        print("\nYes")
    elif num == 10:
        print("\nSigns point to yes")
    elif num == 11:
        print("\n Reply hazy, try again")
    elif num == 12:
        print("\nAsk again later")
    elif num == 13:
        print("\nBetter not tell you now")
    elif num == 14:
        print("\nCannot predict now")
    elif num == 15:
        print("\nConcentrate and ask again")
    elif num == 16:
        print("\nDon't count on it")
    elif num == 17:
        print("\nMy reply is no")
    elif num == 18:
        print("\nMy sources say no")
    elif num == 19:
        print("\nOutlook not so good")
    elif num == 20:
        print("\nVery doubtful")

    global try_again 
    try_again = input("Would you like to try again? (y/n): ")

m8b()

while try_again == 'y':
    m8b()

print("\nOkay, the program has ended")
