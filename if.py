number = 23
guess = int(input('Enter an integer:'))

if guess == number:
    print ('congratulations, you guessed it')
elif guess < number:
    print('no, bigger')
else:
    print ('no, smaller')


