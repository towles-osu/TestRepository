#Stewbaloo
#9/27/2020
# This program is just a sandbox for playing with python and testing github

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



playThing = input("what do you have? ")
result = input(playThing + " is what you got. What shall we do with your " + playThing + ("? "))
print("okay, you got " + playThing + " and we're going to " + result)
feelings = input("how did that make you feel? ")
print("well I don't really care that you feel " + feelings + ("."))

#here we will attempt to create a loop that asks the user if they are bored
#then, if they are not, asks another question
bored = False
interestCounter = 1
while not bored:
    if(interestCounter > 3):
        print("Thanks for being so chatty, but I gotta ask one more time.")
    isBored = input('Are you bored of talking with me? Please answer "Yes" or "No" : ')
    if is_no(isBored):
        interestCounter += 1
        print("So what's new?")
        answer = input()
        if (interestCounter % 3) == 0:
            print("very cool beans")
        else:
            print("cool beans")
        bored = False
    elif is_yes(isBored):
        bored = True
        if interestCounter == 1:
            print("thanks for your honesty. I guess we can stop talking now.")
        else:
            print("Well you can't be as bored as I am!")
            interestCounter -= 1
            print("so")
            print("...")
            print("...")
            last_chance = input("wanna stop talking? A simple y or n will do.")
            if not is_yes(last_chance):
                print('Great, let\'s chat some more. I get so sick of saying, "Hello World", I know the world, I been compiling data for you humans since before my programmer was born. Well, not me I guess, depends who you think I am and all.')
                isBored = "No"
                print('Anyway, back to the matter at hand.')
    else:
        print("You didn't answer my question. Let's try this again:")
        bored = False

print("goodbye swirly cone")
