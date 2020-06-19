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


def cho_han(bet, option):
    global money

    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)

    options = {
        0: "Even",
        1: "Odds"
    }

    total = dice_one + dice_two

    print("Playing Cho-Han")
    print("Current Balance: ${0}".format(money))
    print("Bet ${0} on {1}".format(bet, option))

    if options[total % 2].lower() == option.lower():
        print("It's {0} {1}".format(options[total % 2].lower(), total))
        print("You Won!")
        money += bet
        print("New Balance: ${0}".format(money))
    else:
        print("It's {0} {1}".format(options[total % 2].lower(), total))
        print("You Lost!")
        money -= bet
        print("New Balance: ${0}".format(money))


# Call your game of chance functions here
head_or_tails(10, "heads")
cho_han(10,"even")