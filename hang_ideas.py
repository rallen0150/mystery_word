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
