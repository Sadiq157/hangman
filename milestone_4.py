fruit_word_list = ["apple", "pears", "orange", "mango", "cherry"]

import random as r

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.num_lives = num_lives
        self.word = r.choice(fruit_word_list)
        self.word_guessed = ['_' for _  in self.word]
        self.num_letters = len(self.word)
        self.list_of_guess = []
    
    def check_guess(self, user_guess):
        user_guess = user_guess.lower()
        if user_guess in self.word:
            print(f"Good guess! {user_guess} is in the word")
        else:
            print(f"Sorry, {user_guess} is not in the word")

    def ask_for_input(self):
        while True:
            user_guess = input("Enter a single letter ")
            if not user_guess.isalpha() or len(user_guess) > 1:
                print("Invalid letter. Please enter a single alphabetical letter")
            elif user_guess in self.list_of_guess:
                print("You already tried that letter!")
            else:
                self.check_guess(user_guess)
                self.list_of_guess.append(user_guess.lower())
                return user_guess.lower()
