# Python

# Imported Modules
import random
import dictionary

# Get Difficulty Level
while True:
    difficulty = input('Welcome to Wordle, which difficulty do you want?\n'
                       'EASY\n'
                       'INTERMEDIATE\n'
                       'ADVANCED\n'
                       'INSANE\n')
    if difficulty.upper() == 'EASY':
        word = random.choice(dictionary.Easy)
        break

    elif difficulty.upper() == 'INTERMEDIATE':
        word = random.choice(dictionary.Intermediate)
        break

    elif difficulty.upper() == 'ADVANCED':
        word = random.choice(dictionary.Advanced)
        break

    elif difficulty.upper() == 'INSANE':
        word = random.choice(dictionary.Insane)
        break

    else:
        print('Oops, that\'s not a valid input. Please try again')

# Define variables
word_list = list(word)
word_with_spaces = ''
underscores = ''
attempts = 0

# Defining the underscores_list variable to always have the correct number of underscores
for index in range(len(word_list)):
    word_with_spaces = word_with_spaces + word_list[index] + " "
    underscores = underscores + '_'
underscores_list = list(underscores)

# Game Start
while True:
    guess = input(f'Here is your hint {underscores_list}, it has {len(word)} characters. Take a guess at the word: ')
    underscores_list = list(underscores)
    if len(guess) == len(word):
        guess_list = list(guess)
        for letter1 in range(len(word_list)):
            for letter2 in range(len(guess_list)):
                if word_list[letter2] == guess_list[letter2]:
                    underscores_list[letter2] = word_list[letter2].upper()
                else:
                    if word_list[letter1] == guess_list[letter2]:
                        underscores_list[letter2] = guess_list[letter2].lower()
        attempts = attempts + 1
        our_guesses = ' '.join([str(elem) for elem in underscores_list])
        our_guesses = our_guesses + ' '

        if our_guesses.upper() == word_with_spaces.upper():
            break
    else:
        print(f'That\'s not a valid input, it must be exactly {len(word)} characters in length, please try again!')
        attempts = attempts + 1

print(f'You guessed the word! It was {word.upper()}!\nIt took you {attempts} attempts')
