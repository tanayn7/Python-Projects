#Statement - Guess the Number
#Name- Tanay N Niakm
#Dtae - 24-04-21


import random
print("Hi what's your name? ")
name=input()
print("Nice to meet you", name, "\nLet's play a game.\n")
print("I will think of a number between 1 and 20 and you have to guess it in less than 6 guesses. ")
number = random.randint(1, 20)
guesses_no=0
while(guesses_no < 6):
    print("take a guess ")
    guess=input()
    guess = int(guess)
    guesses_no=guesses_no+1
    if (guess<number):
        print("Wrong, your guess is lower than the number")
    if (guess>number):
        print("Wrong, your guess is higher than the number")    
    if(guess==number):
        break;
if(guess==number):
    print("Yaaaay Good job ,Congratulation", name,". You guessed my number in ", guesses_no," guesses!")
if(guess != number):
    print("Sorryyy, The number I was think of was ", number)
    print("You should try again.")


'''
import random

while True :
    print("Hi what's your name? ")
    name=input()
    print("Nice to meet you", name, "\nLet's play a game.\n")
    print("I will think of a number between 1 and 20 and you have to guess it in less than 6 guesses. ")
    number = random.randint(1, 20)
    guesses_no=0
    while(guesses_no < 6):
        print("take a guess ")
        guess=input()
        guess = int(guess)
        guesses_no=guesses_no+1
        if (guess<number):
            print("Wrong, your guess is lower than the number")
        if (guess>number):
            print("Wrong, your guess is higher than the number")    
        if(guess==number):
            break;
    if(guess==number):
            print("Yaaaay Good job ,Congratulation", name,". You guessed my number in ", guesses_no," guesses!")
    if(guess != number):
        print("Sorryyy, The number I was think of was ", number)
        print("You should try again.")
    answer=str(input("Do you want to play it again(Y/N) :"))
    if(answer == 'n' or answer == 'N'):
        break;
'''



