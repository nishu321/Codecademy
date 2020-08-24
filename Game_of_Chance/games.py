import random

money = 100


# Write your game of chance functions here
def head_or_tails(bet, option):
    """
    This function determines if a person wins heads or tails game
    :param bet: The amount user wants to bet
    :param option: The outcome user predict
    :return:
    """
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
    """
    This function determines if a person wins at cho_han game
    :param bet: The amount user wants to bet
    :param option: The outcome user predict
    :return:
    """
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


def high_or_lower(bet):
    """
    This function determines if a person wins at high or low game
    :param bet: The amount user wants to bet
    :return:
    """
    global money

    player = random.randint(2, 14)
    house = random.randint(2, 14)

    options = {
        11: "J",
        12: "Q",
        13: "K",
        14: "A"
    }

    print("Playing Higher or Lower")
    print("Current Balance: ${0}".format(money))
    print("Bet ${0}".format(bet))

    if player > house:
        print("Player's card: {0} House's card: {1}".format(options.get(player, player), options.get(house, house)))
        print("You Won!")
        money += bet
        print("New Balance: ${0}".format(money))
    elif player == house:
        print("Player's card: {0} House's card: {1}".format(options.get(player, player), options.get(house, house)))
        print("Tie")
        print("New Balance: ${0}".format(money))
    else:
        print("Player's card: {0} House's card: {1}".format(options.get(player, player), options.get(house, house)))
        print("You Lost!")
        money -= bet
        print("New Balance: ${0}".format(money))


def roulette(bet, num_option=None, even_or_odd_option=None):
    """
    This function simulates a roulette game
    :param bet: The amount user wants to bet
    :param num_option: Roulette number player wants to bet on
    :param even_or_odd_option: Roulette option player wants to bet on
    :return:
    """
    global money

    roulette_ball = random.randint(0, 37)

    options = {
        37: 00,
        0: "Even",
        1: "Odd"
    }

    roulette_value = []

    if roulette_ball == 37:
        roulette_value.append(options[roulette_ball])
        roulette_value.append("00")
    elif roulette_ball == 0:
        roulette_value.append(roulette_ball)
        roulette_value.append("0")
    else:
        roulette_value.append(roulette_ball)
        roulette_value.append(options[roulette_ball % 2])

    if num_option == None:
        print("Playing Roulette")
        print("Current Balance: ${0}".format(money))
        print("Bet ${0} on {1}".format(bet, even_or_odd_option))

        if roulette_value[1].lower() == even_or_odd_option.lower():
            print("Roulette value: {0} {1} Player's value: {2}".format(roulette_value[0], roulette_value[1],
                                                                       even_or_odd_option))
            print("You Won!")
            money += bet
            print("New Balance: ${0}".format(money))
        else:
            print("Roulette value: {0} {1} Player's value: {2}".format(roulette_value[0], roulette_value[1],
                                                                       even_or_odd_option))
            print("You Lost!")
            money -= bet
            print("New Balance: ${0}".format(money))
    else:
        print("Playing Roulette")
        print("Current Balance: ${0}".format(money))
        print("Bet ${0} on {1}".format(bet, num_option))

        if roulette_value[0] == num_option:
            print(
                "Roulette value: {0} {1} Player's value: {2}".format(roulette_value[0], roulette_value[1], num_option))
            print("You Won!")
            money += bet * 35
            print("New Balance: ${0}".format(money))
        else:
            print(
                "Roulette value: {0} {1} Player's value: {2}".format(roulette_value[0], roulette_value[1], num_option))
            print("You Lost!")
            money -= bet
            print("New Balance: ${0}".format(money))


# Call your game of chance functions here
head_or_tails(10, "heads")
cho_han(10, "even")
high_or_lower(10)
roulette(10,10)