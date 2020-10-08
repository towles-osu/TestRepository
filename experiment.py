#Stewbaloo
#9/27/2020
# This program is just a sandbox for playing with python and testing github

playThing = input("what do you have? ")
result = input(playThing + " is what you got. What shall we do with your " + playThing + ("? "))
print("okay, you got " + playThing + " and we're going to " + result)
feelings = input("how did that make you feel? ")
print("well I don't really care that you feel, " + feelings + ("."))

#here we will attempt to create a loop that asks the user if they are bored
#then, if they are not, asks another question
bored = False
while(bored == False):
    isBored = input('Are you bored? Please answer "True" or "False" : ')
    if(isBored == 'False'):
        print("So what's new?")
        answer = input()
        print("cool beans")
        bored = False
    else:
        bored = True
        print("Well you can't be as bored as I am!")
