#Stewbaloo
#October 2020
#This is a file containing useful string process functions

def is_yes(word):
    word = str(word)
    for counter in word:
        if counter == "y":
            return True
        if counter == "Y":
            return True
    return False

def is_no(word):
    word = str(word)
    for counter in word:
        if counter == "n":
            return True
        if counter == "N":
            return True
    return False