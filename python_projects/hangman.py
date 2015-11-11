#! usr/bin/env python
# hangman.py

### Imports here
from random import randint
import string

### Body here

def start_of_game():
	print("Let's play Hangman!")
	list_of_words = generate_list_of_words()
	target = target_word(list_of_words)
	letter_bank = generate_alphabet()
	hits_and_misses(target, letter_bank)
	return target, letter_bank


def generate_list_of_words():
	with open("words.txt") as fin:
		list_of_words = [words.strip() for words in fin]
		return list_of_words

def generate_alphabet():
	letter_bank = list(string.ascii_lowercase)
	return letter_bank

def target_word(list_of_words):
	list_length = len(list_of_words)
	random_index = randint(0, list_length-1)
	target = list_of_words[random_index]
	print target # Is a string.
	return target


def hits_and_misses(target, letter_bank):
	for i in target:
		if i not in letter_bank:
			print i, 
		else:
			print " _ ", 
	print "\n"

def take_letter(target, letter_bank):
	guessed_letter = raw_input("Guess a letter, please: ")
	# Do validation checks in another function to make sure not appending
	# same letter twice; check that they are not inputting anything that 
	# is not a character; check that they are not inputting anything that
	# is greater than length = 1. 
	letter_bank.remove(guessed_letter)
	if guessed_letter in target:
		print("That was a hit!")
		check = True
	else:
		print("Sorry :{ That was not a hit.")
		check = False
	hits_and_misses(target, letter_bank)
	print("Your letter bank: {}".format(letter_bank))
	return letter_bank, check


def compare_to_target(guessed_letter):
	print_hits_and_misses(new_)

def letter_bank(letter_bank, hits, misses):
	hits_and_misses_to_remove = hits + miss
	for item in hits_and_misses_to_remove:
		if item in bank:
			new_bank = bank.remove(item)
	return new_bank

def guessing_game(target, letter_bank):
	health_meter = 6
	while health_meter > 0:
		list_ = [1 for i, char in enumerate(target) if char not in letter_bank]
		if sum(list_) == len(target):
			print ("You won! :}")
			break
		else:
			letter_bank, check = take_letter(target, letter_bank)
			if check == False:
				health_meter -= 1
	if health_meter == 0:
		print ("You killed him...")



	 	

### Def main() here

def main():
	target, letter_bank = start_of_game()
	guessing_game(target, letter_bank)

### Boilerplate

if __name__ == "__main__":
	main()