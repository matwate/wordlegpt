import random
import string
from colorama import Fore, Style

class WordleGame:
    def __init__(self):
        self.word = self.load_word_list().lower()
        self.guesses = []
        self.difficulty = self.get_difficulty()

    def load_word_list(self):
        with open("words.txt", "r") as file:
            word_list = [word.strip() for word in file.readlines()]
        return random.choice(word_list)

    def play(self):
        while True:
            guess = self.get_user_guess()
            self.guesses.append(guess)

            if guess == self.word:
                print(f"{Fore.GREEN}Congratulations, you guessed the word!{Style.RESET_ALL}")
                break
            elif len(self.guesses) == 5:
                self.give_hint(guess)
                print(f"{Fore.RED}You ran out of guesses! The word was {self.word}.{Style.RESET_ALL}")
                break
            self.give_hint(guess)

    def get_user_guess(self):
        while True:
            guess = input(f"Guess N. {len(self.guesses) + 1}: ").lower()
            if len(guess) != len(self.word) or not all(char.isalpha() for char in guess):
                print("Invalid guess. Please enter a word with the same length as the target word.")
            else:
                return guess

    def get_difficulty(self):
        while True:
            difficulty = input("Enter difficulty level (easy, medium, hard): ").lower()
            if difficulty == "easy":
                return 6
            elif difficulty == "medium":
                return 3
            elif difficulty == "hard":
                return 0
            else:
                print("Invalid difficulty level. Please try again.")

    def give_hint(self, guess):
        word_hint = []
        letter_hint = []
        for char1, char2 in zip(guess, self.word):
            if char1 == char2:
                word_hint.append(f"{Fore.GREEN}{char1}{Style.RESET_ALL}")
            elif char1 in self.word:
                word_hint.append(f"{Fore.YELLOW}{char1}{Style.RESET_ALL}")
            else:
                word_hint.append(char1)

            letter_diff = abs(string.ascii_lowercase.index(char1) - string.ascii_lowercase.index(char2))
            if letter_diff <= self.difficulty:
                letter_hint.append(f"{Fore.RED}*{Style.RESET_ALL}")
            else:
                letter_hint.append(f"{Fore.BLUE}*{Style.RESET_ALL}")

        print(''.join(word_hint))
        print(''.join(letter_hint))

def main():
    game = WordleGame()
    game.play()

if __name__ == "__main__":
    main()