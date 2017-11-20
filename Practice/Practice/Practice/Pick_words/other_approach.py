# import the random library
import random

# read all the list of words
words = []
with open('sowpods.txt', 'r') as f:
    line = f.readline().strip()
    words.append(line)
    while line:
        line = f.readline().strip()
        words.append(line)

# generate a random number
random_index = random.randint(0, len(words))

# take the word
print("Random word: ", words[random_index])