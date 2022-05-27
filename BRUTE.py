import time
import itertools
import string

password = input('Please enter your password: ')

def guess_password(real):
    chars = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    for password_length in range(1, 20):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                return 'the password is {}, found in {} guesses.'.format(guess, attempts)
            print(guess, attempts)
		

print(guess_password('password'))
