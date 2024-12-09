fruit_word_list = ["apple", "pears", "orange", "mango", "cherry"]

print(fruit_word_list)

import random as r

random_word = r.choice(word_list)

print(random_word)

user_guess = input("Enter a single letter ")

if not user_guess.isalpha() or len(user_guess) > 1:
    print("Oops! That is not a valid input")
else:
    print("Good guess!")
