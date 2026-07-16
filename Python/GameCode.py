from random import random as rand

# change it to work with a random amount of numbers till 8 max numbers. kid knows how many numbers

while True:
    number1 = int(9 * rand())
    number2 = int(9 * rand())
    number3 = int(9 * rand())

    if number1 != number2 and number1 != number3 and number2 != number3:
        print("The numbers have been generated. Try to guess them!")
        break
    else :
        continue


while True:
    guess1 = int(input("What is your guess for number 1?"))
    guess2= int(input("What is your guess for number 2?"))
    guess3 = int(input("What is your guess for number 3?"))

    if guess1 == number1 and guess2 == number2 and guess3 == number3:
        print("Congratulations! You guessed all numbers correctly!")
        break
    else: 
        if guess1 == number1:
            print("You guessed number 1 correctly!")
        else:
            print("You guessed number 1 incorrectly.")
        
        if guess2 == number2:
            print("You guessed number 2 correctly!")
        else:
            print("You guessed number 2 incorrectly.")
        
        if guess3 == number3:
            print("You guessed number 3 correctly!")
        else:
            print("You guessed number 3 incorrectly.")
        print("Incorrect. Try again.")
