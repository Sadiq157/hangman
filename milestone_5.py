import random as r

fruit_word_list = ["apple", "pears", "orange", "mango", "cherry"]

print(f"One fruit will be chosen from {fruit_word_list}. You have 3 attempts to guess the letters in the chosen fruit")

class Hangman:
    def __init__(self, word_list, num_lives=3):
        self.num_lives = num_lives
        self.word = r.choice(word_list)  
        self.word_guessed = ['_' for _ in self.word]  
        self.num_letters = len(self.word)
        self.list_of_guesses = [] 

    def check_guess(self, guess):
        guess = guess.lower()  
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"Number of lives left: {self.num_lives}")

    def ask_for_input(self):
        while True:
            guess = input("Enter a single letter: ") 
            if not guess.isalpha() or len(guess) > 1:  
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses: 
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)  
                break  

def play_game(word_list):
    num_lives = 3
    game = Hangman(word_list, num_lives)  
    game.num_lives = num_lives  

    while True:  
        if game.num_lives == 0:
            print(f"You lost! The word was: {game.word}")
            break

        if "_" not in game.word_guessed:
            print(f"Congratulations. You won the game! The word was: {game.word}")
            break

        game.ask_for_input()

play_game(fruit_word_list)