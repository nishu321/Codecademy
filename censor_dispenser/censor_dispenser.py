# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
# email_one = open("c:/Users/nishu/Documents/Codecademy_Projects/censor_dispenser/email_one.txt", "r").read()
# email_two = open("c:/Users/nishu/Documents/Codecademy_Projects/censor_dispenser/email_two.txt", "r").read()
# email_three = open("c:/Users/nishu/Documents/Codecademy_Projects/censor_dispenser/email_three.txt", "r").read()
# email_four = open("c:/Users/nishu/Documents/Codecademy_Projects/censor_dispenser/email_four.txt", "r").read()


def censor_email_one(phrase):
    """
    Removes phrase or word from email text file.
    :param phrase: word or phrase to remove from file
    :return: Return censored text
    :rtype:STR
    """
    with open("c:/Users/nishu/Documents/Codecademy_Projects/censor_dispenser/email_one.txt", "r") as email_one:
        content = email_one.read()

    censored_text = ""

    for line in content.split("\n"):
        if phrase in line:
            line = line.replace(phrase, "@")
            censored_text += line + "\n"
        else:
            censored_text += line + "\n"

    return censored_text


# Test censor one
print(censor_email_one("learning algorithms"))
