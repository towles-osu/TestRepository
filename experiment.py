#Stewbaloo
#9/27/2020
# This program is just a sandbox for playing with python and testing github

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
    isBored = input('Are you bored? Please answer "Yes" or "No" : ')
    if isBored == 'no' or isBored == '"No"' or isBored == 'No' or isBored == '"no"':
        interestCounter += 1
        print("So what's new?")
        answer = input()
        if (interestCounter % 3) == 0:
            print("very cool beans")
        else:
            print("cool beans")
        bored = False
    else:
        bored = True
        if interestCounter == 1:
            print("thanks for your honesty. I guess we can stop talking now.")
        else:
            print("Well you can't be as bored as I am!")
            interestCounter -= 1
            print("so")
            print("...")
            print("...")
            lastChance = input("wanna stop talking? A simply y or n will do.")
            if lastChance == 'y' or lastChance == 'Y' or lastChance == '"Y"' or lastChance == '"y"':
                print('Great, let\'s chat some more. I gett so sick of saying, "Hello World", I know the world, I been compiling data for you humans since before my programmer was born. Well, not me I guess, depends who you think I am and all.')
                isBored = False
                print('Anyway, back to the matter at hand.')

print("goodbye swirly cone")
