import random

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
print("There are {} letters in the word".format(letter_count))

guess = 0
while guess < 8 and hidden != word:
    print(hidden)
    print("You have {}/8 guesses wrong!".format(guess))
    print("Wrong Letters: {}".format(wrong_letters))

    # User Input
    user_let = input("Enter a single letter: ").lower()

    if user_let in word:
        print("Correct Letter")
        space_holder = ""
        for space in range(len(word)):
            if user_let == word[space]:
                space_holder += user_let
            else:
                space_holder += hidden[space]
        hidden = space_holder

    else:
        print("Wrong Letter")
        guess += 1
        wrong_letters.append(user_let)

if guess == 8:
    print("YOU LOSE!")
    print("The word was {}".format(word))
else:
    print("YOU GUESSED THE CORRECT WORD WHICH WAS {}!".format(word))
