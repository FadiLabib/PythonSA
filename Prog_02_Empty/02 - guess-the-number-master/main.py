import random

def guess(x):
    #Get a random number between 1 and x
    #initial guess variable to 0
 
    #Go through the conditions while guess != random number
    #Ask the user for a guess
    #Evaluate if guess is below random number and say that guess is too low
    #Evaluate if guess is above random number and say that guess is too high
    #If it's not too low or too high then exit while loop and print you guessed the number

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


guess(10)