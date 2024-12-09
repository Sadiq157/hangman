word_list = ["apple", "pears", "orange", "mango", "cherry"]

print(word_list)

import random as r

word = r.choice(word_list)

print(word)

guess = input("Enter a single letter ")

if not guess.isalpha() or len(guess) > 1:
    print("Oops! That is not a valid input")
else:
    print("Good guess!")
