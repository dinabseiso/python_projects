#! usr/bin/env python
# mimsmind0.py

### Imports go here

import sys
from random import randint 


### Body
""" Create a script that will ask the player to guess a number of x-digits
which is manipulable given an argument in the commandline. If not, then 
the default digit length is one. 

Play the guessing game until the user guesses the number correctly,
giving them hints when they're too high or too low."""

def getDigits():
	print ("Let's play the mimsmind0 game.")
	if len(sys.argv) != 2 : 									# If user fails to input an argument on the commandline, set default digit length to 1.
		digits = 1
	else :
		digits = int(sys.argv[1])
	random_number = randint(1, (10**digits - 1))				
	return random_number, digits 								# Return a tuple for the next function. Many functions allow us to control our code best.
	

def guessingGame():
	random_number, digits = getDigits()							# Reach for the two values returned in the getDigits() function.
	guess = raw_input("Guess a %d-digit number: " % digits )
	guess = int(guess)
	tries = 1													# For later keeping track of the user attempts.
	while random_number != guess:
		guess = int(guess)
		if guess > random_number: 
			guess = raw_input("Try again. Guess a lower number: ")
			tries += 1
		elif guess < random_number: 
			guess = raw_input("Try again. Guess a higher number: ")
			tries +=1
	print ("Congratulations! You guessed the correct number in %d tries." % tries )


### Define main() here:

def main():
	guessingGame()


### Boilerplate goes here in order to call main().

if __name__ == "__main__" :
	main()