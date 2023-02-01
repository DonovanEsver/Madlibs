import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low =
        feedback = input(f'Is my {guess} too high (H), too low (L), or correct (C)?? ').lower()  
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1

    print('Finally! You 100% switched up the numbers while we were playing.')  

computer_guess(10)