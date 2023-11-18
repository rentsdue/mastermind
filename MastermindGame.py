import random
import os

class MastermindGame:
    def __init__(self):
        self.attempts = 0
        self.answer = 0

    def clear_screen(self):
        # Clears the screen to hide the answer in multiplayer mode
        os.system('cls' if os.name == 'nt' else 'clear')

    def is_valid_number(self, number, allow_repeats):
        # Check if the number is a valid 4-digit number and adheres to repeat rules
        num_str = str(number)
        is_valid = 1000 <= number <= 9999 and not num_str.startswith('0')
        has_unique_digits = len(set(num_str)) == len(num_str)
        return is_valid and (allow_repeats or has_unique_digits)

    def get_unique_answer(self, allow_repeats):
        # Generate a random 4-digit number based on repeat rules
        while True:
            answer = random.randrange(1000, 10000)
            if self.is_valid_number(answer, allow_repeats):
                return answer

    def play_single_player(self, allow_repeats):
        # Start single player mode
        self.answer = self.get_unique_answer(allow_repeats)
        print("Welcome to Mastermind! Guess a 4-digit number.")
        self.play_game(allow_repeats)

    def play_multiplayer(self, allow_repeats):
        # Start multiplayer mode
        while True:
            try:
                self.answer = int(input("Enter a 4-digit number: "))
                if self.is_valid_number(self.answer, allow_repeats):
                    break
                else:
                    print("Invalid number. Ensure it's a 4-digit integer.")
            except ValueError:
                print("Invalid input. Enter a valid integer.")
        self.clear_screen()
        print("Number set. Opponent, start guessing.")
        self.play_game(allow_repeats)

    def play_game(self, allow_repeats):
        # The main game loop
        previous_attempts = set()
        while self.attempts < 10:
            try:
                guess = int(input("Your guess: "))
                if not self.is_valid_number(guess, allow_repeats):
                    if allow_repeats:
                        print("Invalid guess. Ensure it's a 4-digit integer.")
                    else:
                        print("Invalid guess. Ensure it's a 4-digit integer with unique digits.")
                    continue

                if guess in previous_attempts:
                    print("You've already guessed this number.")
                    continue

                previous_attempts.add(guess)
                self.attempts += 1

                if guess == self.answer:
                    print(f"Correct! You guessed in {self.attempts} attempts.")
                    break

                correct_positions = sum(a == b for a, b in zip(str(guess), str(self.answer)))
                correct_digits = sum(min(str(guess).count(d), str(self.answer).count(d)) for d in set(str(guess)))
                wrong_position = correct_digits - correct_positions

                print(f"{correct_positions} correct digits in the correct position.")
                print(f"{wrong_position} correct digits in the wrong position.")
                print(f"Attempts: {self.attempts}")

            except ValueError:
                print("Invalid input. Enter a valid integer.")

        if self.attempts >= 10:
            print(f"Maximum attempts reached. The answer was {self.answer}.")

    @staticmethod
    def start_game():
        # Game initialization and mode selection
        while True:
            mode = input("Type 1 for Single player or M for Multiplayer: ").lower()
            if mode in ["1", "m"]:
                allow_repeats = input("Allow repeats? (yes/no): ").lower() in ["yes", "y"]
                game = MastermindGame()
                if mode == "1":
                    game.play_single_player(allow_repeats)
                else:
                    game.play_multiplayer(allow_repeats)

                play_again = input("Play again? (yes/no): ").lower()
                if play_again not in ["yes", "y"]:
                    break
            else:
                print("Invalid input. Type 1 or M.")

if __name__ == "__main__":
    MastermindGame.start_game()
