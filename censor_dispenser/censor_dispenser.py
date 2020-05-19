# These are the emails you will be censoring. The open() function is opening the text file that the emails are
# contained in and the .read() method is allowing us to save their contexts to the following variables:
# email_one = open("c:/Users/nishu/Documents/Codecademy_Projects/censor_dispenser/email_one.txt", "r").read()
# email_two = open("c:/Users/nishu/Documents/Codecademy_Projects/censor_dispenser/email_two.txt", "r").read()
# email_three = open("c:/Users/nishu/Documents/Codecademy_Projects/censor_dispenser/email_three.txt", "r").read()
# email_four = open("c:/Users/nishu/Documents/Codecademy_Projects/censor_dispenser/email_four.txt", "r").read()


def censor_email_one(phrase, filename):
    """
    Removes phrase or word from email text file.
    :param filename: file to censor
    :param phrase: word or phrase to remove from file
    :return: Return censored text
    :rtype: STR
    """
    with open(filename, "r") as email_one:
        content = email_one.read()

    censored_text = ""

    for line in content.split("\n"):
        if phrase.lower() in line.lower():
            line = line.lower().replace(phrase.lower(), "@")
        censored_text += line.lower() + "\n"

    return censored_text


def censor_email_two(phrases, filename):
    """
    Removes all phrases or words from list
    :param filename: file to censor
    :param phrases: list of phrases or words to remove
    :return: Return censored text
    :rtype: STR
    """
    with open(filename, "r") as email_two:
        content = email_two.read()

    censored_text = ""

    for line in content.split("\n"):
        for phrase in phrases:
            if phrase.lower() in line.lower():
                line = line.lower().replace(phrase.lower(), "@")
        censored_text += line.lower() + "\n"

    return censored_text


def censor_email_three(phrases, negative_words, filename):
    """
    Removes all phrases or words from list if they occur more than twice
    :param phrases: list of phrases or words to remove
    :param negative_words: list of negative phrases or words to remove
    :param filename: file to censor
    :return: Return censored text
    :rtype: STR
    """
    with open(filename, "r") as email_three:
        content = email_three.read()

    content = censor_email_two(phrases, filename)

    word_lst = []

    for word in content.split():
        word_lst.append(word)

    counter = 0
    for i in range(len(word_lst)):
        if word_lst[i].lower() in negative_words:
            counter += 1
            if counter > 2:
                word_lst[i] = word_lst[i].lower().replace(word_lst[i].lower(), "@")

    return " ".join(word_lst)


def censor_email_four(phrases, negative_words, filename):
    """
    Removes all phrases or words from list and words that come before and after
    :param phrases: list of phrases or words to remove
    :param negative_words: list of negative phrases or words to remove
    :param filename: file to censor
    :return: Return censored text
    :rtype: STR
    """
    with open(filename, "r") as email_four:
        content = email_four.read()

    content = censor_email_three(phrases, negative_words, filename)

    word_lst = []

    for word in content.split():
        word_lst.append(word)

    for i in range(len(word_lst)):
        if "@" in word_lst[i]:
            word_lst[i - 1] = "#"
            word_lst[i + 1] = "#"

    return " ".join(word_lst)


# Test censor one
# print(censor_email_one("learning algorithms","email_one.txt"))

# Test censor two
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself"]
# print(censor_email_two(proprietary_terms,"email_two.txt"))

# Test censor three
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]
# print(censor_email_three(proprietary_terms, negative_words, "email_three.txt"))

# Test censor four
# print(censor_email_four(proprietary_terms, negative_words, "email_four.txt"))
