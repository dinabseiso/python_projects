#! usr/bin/env python
# mimsmind1.py

### Imports go here

import sys
from random import randint 


### Body

def getDigits():
	if len(sys.argv) != 2 : 
		digits = 3
	else :
		digits = sys.argv[1]
	digits = int(digits)
	# Compute the maximum number of tries allowed.
	max_tries = 2**digits + digits 												
	random_number = randint(1, (10**digits - 1))
	# Be nice, and let them know how many tries they have total.
	print ("Let's play the mimsmind1 game. You have %d tries." % max_tries)		
	# Create the tuple for grabbing the values later!
	return random_number, digits, max_tries										


def make_lists(number):
	""" This list comprehension (yes!) is implemented to create a list 
	where every item is an integer form of an index within the passed in
	string or number.
	"""

	return [int(digit) for digit in number]

def cows_and_bulls(guess_string, random_number_string):
	""" This function pulls a list of numbers from the make_lists() above
	in order to evaluate index by index whether there is a match (a bull). 
	It counts all True hits in a list of tuples (the product of zip()), to see
	whether the two values in the tuple match.

	It then enters a for loop that iterates through the set of characters in guess_list.
	set() only maintains unique values. So, for example, if there are duplicate
	integers or characters, only one will be represented in the set. set([1, 2, 2]) will 
	return [1, 2]. So, for every digit in this set, it will take the minimum number 
	of matches found in either the guessed value or the randomly generated value. We take
	the minimum of the two because unless we have a complete match between guessed value and
	the randomly generated one, we will have the most matches between the set that originates
	from the guessed value than with our randomly generated value. The only time when this is
	not true is when our randomly generated number contains many duplicate integers, which 
	is why we have the min() function as well. The total number of matches (this includes bulls)
	is cumulatively summated. If we did not have min(guess_list.count(digit)), and instead had 
	evertthing else exclusively, we would run into a problem where it says we have cows when
	we really do not have any cows at all.

	Because we calculated the total number of cows and bulls, we want to subtract bulls in 
	order to get our count of cows. 

	We return the counts as a tuple. 
	"""
	
	guess_list, random_number_list = make_lists(guess_string), make_lists(random_number_string)
	bull_count = [digit1 == digit2 for digit1, digit2 in zip(guess_list, random_number_list)].count(True)
	cows_and_bulls = 0
	for digit in set(guess_list):
		cows_and_bulls += min(guess_list.count(digit), random_number_list.count(digit))
	cow_count = cows_and_bulls - bull_count
	return bull_count, cow_count


def guessingGame():
	# Pull from getDigits() the variables you need.
	random_number, digits, max_tries = getDigits()
	guess = raw_input("Guess a %d-digit number: " % digits )
	tries = 1
		# The below while loop will persist until tries becomes 
		# equivalent to max_tries. The try-except will catch when 
		# a non-numerical value is passed in. 
	while tries < max_tries:
		try : 																
			guess_string = guess
			guess = int(guess)
			random_number_string = str(random_number)
			random_number_string = random_number_string.zfill(digits)
		except ValueError : 
			guess = raw_input("That's not a %d-digit number. Try again, please: " % digits) 
			tries += 1
		# Here is a check to see that the number of characters entered matches
		# the number of characters in the random number generated, including zeroes.
		# If not, then the user is told what went wrong, and asked to enter in another
		# value.
		if len(random_number_string) == len(guess_string): 
			# If the randomly generated number and the guess do not equal one another, 
			# and the number of attempts do not equal the maximum allowed attempts, then
			# a hint is attempted for additional guesses.
			if (random_number != guess) and (tries != max_tries):				# If they have tries left, do some work.
				# A tuple is returned by the function cows_and_bulls, explained above.
				bull_count, cow_count = cows_and_bulls(guess_string, random_number_string)
				# .format() as a different way to reflect held values.
				guess = raw_input("{} bull(s), {} cow(s). Try again: " .format(bull_count, cow_count))
				tries += 1
			# But if they do not have tries left... break out of the while loop to soon end the game.
			elif (random_number != guess) and (tries == max_tries):	
				break															 
			else: 
				# If they guessed correctly, let them know!
				print ("Congratulations! You guessed the correct number in {} tries." .format(tries) )	
				# Break out of the game. Otherwise, will be stuck in the while loop because the clause is still True.
				break															
		else : 
			# Remind them of the digits they need to enter.
			guess = raw_input("Incorrect number of digits. Please enter a %d-digit number, preceding with zeroes if you must: " % digits) 	
			tries +=1
	# This if statement is outside of the while loop in the event that the user is rude and inputs a series of non-numerical
	# arguments over and over again. 
	if tries >= max_tries:
		print ("I'm sorry! You ran out of guesses. Better luck next time. (The number was {} by the way.)" .format(random_number))



### Define main() here

def main():
	guessingGame()


### Boilerplate for calling main()


if __name__ == "__main__" :
	main()