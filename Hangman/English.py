from __future__ import print_function
import random


starwars_list = ['Jar Jar Binks','Leia', 'Darth Vader','Luke Skywalker','Yoda', 'Boba Fett', 'Sith', 'Rancor', 'TIE fighter', 'X Wing', 'Execute Order', 'Blaster Pistol', 'lightsaber', 'Tatooine', 'Hoth', 'Endor']
cse_list = ['Python is the best!', 'Computer Science', 'Python', 'Javascript', 'HTML and CSS', 'Bootstrap', 'PLTW', 'Codecademy', 'Cloud 9', 'Interactive Design Environment', 'Internet Protocol']
english_list = ['Alliteration', 'Onomatopoeia', 'Shakespeare', 'Of Mice and Men', 'Animal Farm', 'Allusion', 'Poetry', 'Thesis', 'Metaphor', 'Idiom']

theme_picker = raw_input("Would you like to play with words from the Star Wars theme, CSE theme, or the English theme? (english/cse/star wars): \n")

def secret_message_picker(theme_picker):
    '''Picks a theme and a random word from said theme'''
    if theme_picker.lower() == "cse":
        message = random.choice(cse_list)
    elif theme_picker.lower() == "english":
        message = random.choice(english_list)
    elif theme_picker.lower() == "star wars":
        message = random.choice(starwars_list)
        
    return message

global secret_message
secret_message = secret_message_picker(theme_picker)

global guess_letters
guessed_letters = []
global correct_guess_letters
correct_guess_letters = []
global secret_list
secret_list = []
for character in secret_message:
    secret_list.append(character)
    

def play_again():
    ''' Allows the player to replay the game.'''
    again = raw_input("Would you like to play again? (y/n): \n")
    if again.lower() == 'y' or again.lower() == 'yes':
        hangman()
    else:
        print("Thank you for playing!")
        
    return again

def dashed_function(secret_message):
    '''Converts the secret message to a dashed line.'''
    dashed_secret = []
    for char in secret_message:
        if char == ' ' or char == ',' or char == '.' or char == '!' or char == '!':
            dashed_secret.append(char)
        else:
            dashed_secret.append('-')
    
    encrypted_message = ""
    for x in dashed_secret:
        encrypted_message += x
        
    #print(encrypted_message)
    return encrypted_message
    
global final_result
final_result = dashed_function(secret_message)
global final_list
final_list = []
for a_letter in final_result:
    final_list.append(a_letter)
    
def guess_function(player_guess):
    '''Checks if the guess is in secret or is a previously guessed letter'''
    final_string = ""
    if len(player_guess) > 1 or len(player_guess) == 1:
        player_guess = player_guess[0]
        for data in range(len(secret_list)):
            if player_guess == secret_list[data]:
                guessed_letters.append(player_guess)
                correct_guess_letters.append(player_guess)
                final_list[data] = player_guess
            elif player_guess in correct_guess_letters:
                for value in range(len(secret_list)):
                    for letter in range(len(correct_guess_letters)):
                        if secret_list[value] == correct_guess_letters[letter]:
                            final_list[value] = correct_guess_letters[letter]
                            
    elif len(player_guess) == 1 and player_guess in guessed_letters:
        print("You already guessed that letter.")
        guess_function(player_guess)
    
    else:
        print("Invalid input")
        guess_function(player_guess)
    
    for item in final_list:
        final_string += item
        
    print(final_string)
    
    if final_string == secret_message:
        print("You won!")
        
        if play_again() == "n" or "no":
           guesses = 20
    
    
def hangman():
    ''' Tells the player to guess a character or a whole phrase. Also ends the game when player runs out of guesses.'''
    secret_message_picker(theme_picker)
    if secret_message in cse_list:
        print("The theme of the game is CSE. Remember CAPITALIZATION counts!")
    elif secret_message in starwars_list:
        print("The theme of the game is Star Wars. Remember CAPITALIZATION counts!")
    elif secret_message in english_list:
        print("The theme of the game is English. Remember CAPITALIZATION counts!")
    global guesses
    guesses = 1
    while guesses < 21:
        if guesses == 1:
            player_guess = raw_input(str(guesses) + ". Please guess one letter: \n")
            guess_function(player_guess)
            guesses += 1
        elif guesses > 20:
            print("Sorry You could not guess the word." + "\n" + "Game Over")
            if play_again() == "n" or "no":
                break
        else:
            player_guess = raw_input(str(guesses) + ". Please guess one letter: \n")
            guess_function(player_guess)
            guesses += 1
            
hangman()