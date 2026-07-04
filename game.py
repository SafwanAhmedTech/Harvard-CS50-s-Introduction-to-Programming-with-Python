import random
import sys

while True:
    try:
        n = int(input('Level: '))
    except ValueError:
        continue
    else:
        if n > 0:
            break

number = random.randint(1, n)


while True:
    try:
        guess = int(input('Guess: '))
    except ValueError:
        continue
    if guess < 1:
        continue
    elif guess < number:
        print('Too small!')
    elif guess > number:
        print('Too large!')
    else:
        print('Just right!')
        break

