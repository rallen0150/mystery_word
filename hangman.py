import random
from string import ascii_lowercase

open_file = open("/usr/share/dict/words")
words = open_file.read().lower()
open_file.close()

random_word = words.split("\n")

# Creates a Random Word
word = random.choice(random_word)

# Replaces the letters in the word with a "_" and forms a new variable
hidden = "_" * len(word)

letter_count = len(word)

wrong_letters = []
used_letters = []
unused = ascii_lowercase
print("There are {} letters in the word".format(letter_count))

guess = 0
while guess < 8 and hidden != word:
    print(hidden)
    print("You have {}/8 guesses wrong!".format(guess))
    print("\nWrong Letters: {}".format(wrong_letters))
    print("Unused Letters: {}".format(unused))

    # User Input
    user_let = input("\nEnter a single letter: ").lower()

    # Place holder for an empty string to put inputted characters
    space_holder = ""

    if user_let in used_letters:
        for space in range(len(used_letters)):
            if user_let == used_letters[space]:
                print("\nAlready used that letter!\n")
                user_let = input("\nEnter another letter: ").lower()

    # Checks to see if inputted character is in the word
    if user_let in word:
        print("Correct Letter\n")
        for space in range(len(word)):
            if user_let == word[space]:
                space_holder += user_let
            else:
                space_holder += hidden[space]
        hidden = space_holder
        used_letters.append(user_let)
        unused = unused.replace(user_let, "")

    else:
        print("Wrong Letter\n")
        guess += 1
        wrong_letters.append(user_let)
        used_letters.append(user_let)
        unused = unused.replace(user_let, "")

if guess == 8:
    print("YOU LOSE!")
    print("The word was {}".format(word))
else:
    print("YOU GUESSED THE CORRECT WORD WHICH WAS {}!".format(word))
