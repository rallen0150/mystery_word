import random

open_file = open("/usr/share/dict/words")
words = open_file.read().lower()
open_file.close()

word_list = []
random_word = words.split("\n")

num = random.randint(2, 15)

for pull_word in random_word:
    if len(pull_word) == num:
        word_list.append(pull_word)

letter_count = num
print("There are {} letters in the word".format(letter_count))

word = random.choice(word_list)
print(word)
hidden = "-" * len(word)
print(hidden)
user_let = input("\nEnter a single letter: ").lower()
space_holder = ""

if user_let in word:
    print("Correct Letter\n")
    for space in range(len(word)):
        if user_let == word[space]:
            space_holder += user_let
        else:
            space_holder += hidden[space]
    hidden = space_holder
    find_word = hidden
    # used_letters.append(user_let)
    # unused = unused.replace(user_let, "")

else:
    print("Wrong Letter\n")
    # guess += 1
    # wrong_letters.append(user_let)
    # used_letters.append(user_let)
    # unused = unused.replace(user_let, "")

print(hidden)

for take_word in word_list:
    if find_word != word_list[take_word]:
        word_list.remove(take_word)

word = random.choice(word_list)
print(word)
