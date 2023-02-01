import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Nope, not even close, too low')
        elif guess > random_number:
            print('Nowhere near the number, too high')    


    print('Cheater. No way you guessed it right.')

guess(10)


