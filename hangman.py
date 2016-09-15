import random

open_file = open("/usr/share/dict/words")
words = open_file.read().lower()
open_file.close()

random_word = words.split("\n")

# Creates a Random Word
word = random.choice(random_word)

# Random word place-holder
keep_word = word
print(word)

letter_count = 0

# Replaces the letters in the word with a "_"
for char in word:
    hidden = word.replace(char, "_")
    word = hidden
    letter_count += 1

print("There are {} letters in the word".format(letter_count))
print(hidden)

n = 0
# User Input
user_let = input("Enter a single letter: ")

for char in keep_word:
    if user_let == keep_word[n]:
        print("Correct letter")
    else:
        print("Incorrect letter")

    user_let = input("Enter another letter: ")
    n += 1
