import random
 
def guess():
    num = int(input("Please enter your guess\n: "))
    return num
# function for the guess
 


print( '### Welcome to the number guessing game ###\n' ) 

print("The objective is to guess the number I'm thinking of.\n")
print("I will give you clues after your first guess.\n")
secretNumber = random.randint(1,100)
# Creates the random number and stores it in a variable
print("I have of a number from 1-100")

while True:
    #while loop keeps the program running

    numGuessed=guess()
    # creates a new variable of the guess
    if numGuessed < secretNumber:
        print("Guess is too low, guess higher!")
        
    elif numGuessed == secretNumber:
        print("Correct")
        break
        #'break' stops the while loop
    elif numGuessed > secretNumber:
        print("Guess is too high, guess lower !")
        
    else :
        print("unavaible")
