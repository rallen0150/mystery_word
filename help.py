import random# for random.choice
dictionary = ['COMPUTER', 'LAPTOP', 'IDEAS', 'NANYANG', 'COLLEGE']
word = random.choice(dictionary)
original = list(word)
temp = list(word)
guess = []# null list
trial = int(0)# for keeping track of guessess
userinput = ''
counter = int(0)# keeping track of position of element in list (if found)

for i in range(len(original)):# creating the '_ _**....' list
    if ((original[i] == 'A') or (original[i] == 'E') or (original[i] == 'I') or (original[i] == 'O') or
        (original[i] == 'U'):)
        guess.append("*")# * for vowels
    else:
        guess.append("_")# _ for all other alphabets

print guess

while trial < 9:
    userinput = str.upper(raw_input('Input : '))

    if len(userinput)>1: #checking for multiple characters
        print 'Error : Input only a single character'
        continue

    if userinput in original:

        while userinput in temp:# loop for checking redundant characters
            counter = temp.index(userinput)
            guess[counter] = userinput
            temp.remove(userinput)
            temp.insert(counter, '_')

        counter = 0

        for i in range(0, len(temp)):
            if temp[i] == '_':
                counter += 1

        if counter == len(original):# if guess matches original
            print 'Correct\t', guess
            print 'You Win !'
            trial = 10
            break

        print 'Correct\t', guess, '\tTrials left: ', (9-trial)

    else:
        trial += 1
        print 'Incorrect', '\tTrials left: ', (9-trial)
else:
    print 'You Lose !'
    print 'Correct answer was\t', original
