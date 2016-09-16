import random
from string import ascii_lowercase

open_file = open("/usr/share/dict/words")
words = open_file.read().lower()
open_file.close()

random_word = words.split("\n")

regame = "yes"

easy = []
medium = []
hard = []

for pull_word in random_word:
    if len(pull_word) > 1 and len(pull_word) < 6:
        easy.append(pull_word)
    elif len(pull_word) >= 6 and len(pull_word) < 10:
        medium.append(pull_word)
    else:
        hard.append(pull_word)

while regame == "yes" or regame == "y":

    diff = input("Select a Difficulty's Number (1-Easy, 2-Medium, 3-Hard): ")

    if diff == "1":
        word = random.choice(easy)
    elif diff == "2":
        word = random.choice(medium)
    elif diff == "3":
        word = random.choice(hard)
    else:
        ("Invalid Option")

    # Replaces the letters in the word with a "_" and forms a new variable
    hidden = "_" * len(word)

    letter_count = len(word)

    wrong_letters = []
    used_letters = []
    unused = ascii_lowercase

    print("\nThere are {} letters in the word".format(letter_count))

    guess = 0
    while guess < 8 and hidden != word:
        print(hidden)
        print("You have {}/8 guesses wrong!".format(guess))
        print("Wrong Letters: {}".format(wrong_letters))
        print("Unused Letters: {}\n".format(unused + " "))

        # User Input
        user_let = input("Enter a single letter: ").lower()
        while len(user_let) > 1:
            user_let = input("Invalid Letter!\n\nEnter a single letter: ")

        # Place holder for an empty string to put inputted characters
        space_holder = ""

        if user_let in used_letters:
            for space in range(len(used_letters)):
                if user_let == used_letters[space]:
                    print("\nAlready used that letter!\n")
                    user_let = input("Enter another letter: ").lower()
                    while len(user_let) > 1:
                        user_let = input("Invalid Letter!\n\nEnter a single letter: ")

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

    regame = input("Play Again? yes / no : ").lower()

print("Thanks for playing!")
