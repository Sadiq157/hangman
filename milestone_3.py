fruit_word_list = ["apple", "pears", "orange", "mango", "cherry"]

print(f"A random fruit from the following selection will be chosen: {fruit_word_list}")

import random as r

random_word = r.choice(fruit_word_list)

print(random_word) # This is to check whether the game is running as intended and the letter is in the word
# Obviously this won't appear in the game.

while True:
    user_guess = input("Enter a single letter ")
    if not user_guess.isalpha() or len(user_guess) > 1:
            print("Invalid letter. Please enter a single alphabetical letter")
    else:
        print("Letter registered") # I have added this as a confirmation that it has worked as intended.
        break

if user_guess in random_word:
     print(f"Good guess! {user_guess} is in the word")
else:
     print(f"Sorry, {user_guess} is not in the word")


def check_guess(user_guess):
     user_guess = user_guess.lower()
     if user_guess in random_word:
        print(f"Good guess! {user_guess} is in the word")
     else:
        print(f"Sorry, {user_guess} is not in the word")

def ask_for_input():
     while True:
          user_guess = input("Enter a single letter ")
          if not user_guess.isalpha() or len(user_guess) > 1:
            print("Invalid letter. Please enter a single alphabetical letter")
          else:
            return(user_guess)
               
user_guess = ask_for_input()
check_guess(user_guess)
