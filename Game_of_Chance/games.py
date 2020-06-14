import random

money = 100


# Write your game of chance functions here
def head_or_tails(bet, option):
    global money

    options = {
        1: "Heads",
        2: "Tails"
    }

    num = random.randint(1, 2)

    print("Playing Heads or Tails")
    print("Current Balance: ${0}".format(money))
    print("Bet ${0} on {1}".format(bet, option))

    if options[num].lower() == option.lower():
        print("It landed on {0}".format(options[num].lower()))
        print("You Won!")
        money += bet
        print("New Balance: ${0}".format(money))
    else:
        print("It landed on {0}".format(options[num].lower()))
        print("You Lost!")
        money -= bet
        print("New Balance: ${0}".format(money))


# Call your game of chance functions here
head_or_tails(10, "heads")
