# -*- coding: utf-8 -*-
#!C:\Users\המחשב שלי\AppData\Local\Programs\Python\Python38-32\Scripts\pyinstaller-script.py
def seven_state_hangman(number):
	if number==1:
		return """    x-------x"""
	if number==2: 
		return """    x-------x\n    |\n    |\n    |\n    |\n    |"""
	if number==3: 
		return """    x-------x\n    |       |\n    |       0\n    |       \n    |\n    |"""
	if number==4: 
		return """    x-------x\n    |       |\n    |       0\n    |       |\n    |\n    |"""
	if number==5: 
		return """    x-------x\n    |       |\n    |       0\n    |      /|\ \n    |\n    |"""
	if number==6: 
		return """    x-------x\n    |       |\n    |       0\n    |      /|\ \n    |      / \n    |"""
	if number==7:
		return """    x-------x\n    |       |\n    |       0\n    |      /|\ \n    |      / \ \n    |"""


def print_hangman_states(dictionary,num_of_tries):
	
	if 0<num_of_tries<8: print(seven_state_hangman(num_of_tries))
	else: return None

def print_hangman_screen():
	print("""  _    _\n | |  | |\n | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __\n |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n | |  | | (_| | | | | (_| | | | | | | (_| | | | |\n |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n                      __/ |\n                     |___/""")
	
def show_hidden_word(secret_word, old_letters_guessed):

	secret_word_list = list(secret_word) #making list for secret_word
	old_letters_list = list(old_letters_guessed) #making list for old_letters_guessed
	secret_len = len(secret_word_list) #length of secret_word
	old_len = len(old_letters_list) #length of old_letters_guessed
	string_guessed_list = list("_" * secret_len) ##making a list of "_" characters in length secret_len

	for i_secret in range(secret_len): ##index for secret_word. reaches until secret_len-1
		for i_old in range(old_len):##index for old_letters_list
			if secret_word_list[i_secret] == old_letters_list[i_old]: ##if the letter for secret_word_list is equal to old_letters_list: 
				string_guessed_list[i_secret] = secret_word[i_secret] ##insert the letter of secret_word in index i_secret to string_guessed_list in index i_secret
	string_guessed = " ".join(string_guessed_list) ##Creat a string composed from "_" and spaces (" ")		
	
	return string_guessed
"""The func. gets two parameters and returns a string composed from '_' characters and letters (if they're in secret_word)
	:param secret_word: secret word letter
    :param old_letters_guessed: list of old letters guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: The result of creating a string composed from "_" and spaces (" ")	
    :rtype: str
	"""

def check_win(secret_word, old_letters_guessed):
	"""Get secret word and list and check if the player wins
	:param secret_word: a word (string)
    :param old_letters_guessed: a list of letters
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True if all the letters in string_guessed are alphabetic. if not, returns False
    :rtype: boolian
	"""
	secret_word_list = list(secret_word) #making list for secret_word
	secret_len = len(secret_word_list) #length of secret_word
	old_len = len(old_letters_guessed) #length of old_letters_guessed
	string_guessed_list = list("_" * secret_len)
	for i_secret in range(secret_len):
		for i_old in range(old_len):
			if secret_word_list[i_secret] == old_letters_guessed[i_old]:
				string_guessed_list[i_secret] = secret_word[i_secret]
	string_guessed = "".join(string_guessed_list)
	if string_guessed.isalpha() == True:
		return True ## The player wins
	else: return False	## The player didn't win

def is_valid_input(letter_guessed):
	""" check if the letter's lenght is 1 and alphabetic 
	:param letter_guessed: letter/s that user puts 
    :type letter_guessed: str
    :return: True if the letter is length 1 and it's alphabetic, False if not alpha or the length is bigger than 1
    :rtype: boolian
	"""
	if letter_guessed.isalpha() == False or len(letter_guessed) > 1: #Check if input letter_guessed is alphabetic and it's lenght
		return False## the letter isn't standing one of the conditions , Not Valid!
	return True ##the letter is length 1 and it's alphabetic , It's Valid!


def check_valid_input(letter_guessed, old_letters_guessed):
	""" check if the letter is not in old list 
	:param letter_guessed:  
    :param old_letters_guessed: 
    :type letter_guessed:
    :type old_letters_guessed: 
    :return: True: letter_guessed is not in list old_letters_guessed, False: if the input not valid or the letter is in the old list
    :rtype: boolian	
	"""
	letter_lower = letter_guessed.lower()
	if is_valid_input(letter_lower) == False or letter_lower in old_letters_guessed:
		#check if the input for letter_guessed is valid or the letter_guessed is already in list old_letters_guessed
		return False ## letter_guessed is not valid or letter_guessed is already exist in list old_letters_guessed	
	return True	#letter_guessed is not in list old_letters_guessed 	

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	"""if the letter guessed before or the input not valid: print 'X' and list of letters guessed, separeted by '->' and return False. otherwise, return True 
	:param letter_guessed: string of input letter/s
    :param old_letters_guessed: list of letters guessed before
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True: if the letter not guessed before, False: 
    :rtype: boolian
	"""
	if check_valid_input(letter_guessed, old_letters_guessed) == True:  #Check if the input is valid: it's lenght is 1 and not guessed before		
		old_letters_guessed.extend(letter_guessed.lower()) ## append the letter_guessed to the list old_letters_guessed
		return True ## means that the letter not guessed before 
	print("X") 	
	old_letters_guessed = sorted(old_letters_guessed) ##sort the list and put it to old_letters_guessed
	print('-> '.join(old_letters_guessed))	
	return False

def choose_word(file_path, index):
	""" get file path string and index for the word in the file and return the secret word for the game 
	:param file_path:string of file path of that contains the words
    :param index: index for the word in the file
    :type file_path: string
    :type index: string
    :return: secret word that its part of the words in the file
    :rtype: string
	"""
	file = open(file_path, "r") #open file path from given string
	words = file.readline() #read line from the file
	list_words = words.split() #get all the words in list
	len_list = len(list_words) #length of list_words (number of words)
	index = int(index) #casting for index because it's type is str
	if index > len_list: #check if the index is bigger than the number of words
		i=(index) % len_list 
	else: i = index	
	for_tuple2 = list_words[i-1] #for_tuple2 gets the word from list 
	for word in list_words: #if the word is in the list more than 1: remove it
		if list_words.count(word) > 1:
			list_words.remove(word)
	for_tuple1 = len(list_words) #for_tuple1 gets the length of the list
	tuple = (for_tuple1,for_tuple2)
	file.close()
	secret_word = tuple[1] #secret_word gets the secret word
	return secret_word			

	
MAX_TRIES = 6
def the_hangman_game(secret_word):
	""" the func. the_hangman_game get a secret word. and user must to guess a letter that input_char receive.
	if the user mistakes, num_of_tries added by 1 until he reaches to MAX_TRIES.
	if he is right, the func. check_win checks if user guessed all the letters in the secret word
	"""
	HANGMAN_PHOTOS = {"State 1": "1", "State 2": "2", "State 3": "3", "State 4": "4", "State 5": "5", "State 6": "6", "State 7": "7"}
	num_of_tries = 0
	old_letters_guessed = []
	print_hangman_states(HANGMAN_PHOTOS, num_of_tries+1) ##printing the first state of hangman
	print(show_hidden_word(secret_word,old_letters_guessed)) ##printing The bottom lines of secret_word
	while num_of_tries < MAX_TRIES:	## if number of tries is smaller than number of MAX_TRIES: continue the while loop
		input_char = input("Guess a letter: ") #input character
		letter_not_guessed = try_update_letter_guessed(input_char, old_letters_guessed) #letter_not_guessed receive a boolian value if the letter not guessed before: False means the letter guessed already
		if letter_not_guessed == True and input_char.lower() in secret_word: #The letter that not guessed before, and it's correct
			string_to_win = show_hidden_word(secret_word, old_letters_guessed) ## string composed with "_" and letters (if guessed correctly)
			print(string_to_win)			
			if check_win(secret_word, old_letters_guessed) == True:
				return True
			else: continue
		elif letter_not_guessed == True: ##The letter not guessed before and not in secret_word
			num_of_tries += 1
			print(":(")
			print_hangman_states(HANGMAN_PHOTOS, num_of_tries+1) #printing the relevant state of hangman
			print(show_hidden_word(secret_word, old_letters_guessed))
			continue
		else: continue
	return False ##We reached to the MAX_TRIES, that's means we lose	
				
	
def main():
	print_hangman_screen()##printing the game's screen
	path_inpoot = input("Enter file path: ") ##number 2
	index = input("Enter index: ")
	print("Let's start!")
	secret_word = choose_word(path_inpoot, index)
	is_winning = the_hangman_game(secret_word)
	if is_winning == True: print("WIN")
	else: print("LOSE")
	
if __name__ == "__main__":
    main()	