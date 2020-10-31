#Stewbaloo
#October 2020
#This is a file containing useful string process functions

def is_yes(word):
    word = str(word)
    if 'y' in word.lower():
        return True
    else:
        return False

def is_no(word):
    word = str(word)
    for counter in word:
        if counter == "n":
            return True
        if counter == "N":
            return True
    return False

