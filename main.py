import random
from art import logo

attempts = 5

def number_guessing(attempts):
    number = int(random.randint(0,101))
    attempts_list = []
    play_guessing = True
    lose = False

    print(logo + "\n")
    print("¡Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts remaining to guess the number.")

    while play_guessing:
        guess = int(input("Make a guess: "))

        if guess in attempts_list:
            print(f"You already tried this number before: {guess}\n")
        elif guess < 1 or guess > 100:
            print(f"Try a number inside the range 1-100: guess -> {guess}\n")
        else:
            if guess == number:
                print(f"You got It! The answer was {number}\n")
                play_guessing = False
                lose = False
                return lose
            elif guess > number:
                print("Too high.")
            elif guess < number:
                print("Too low.")
            print("Guess again.")
            attempts -= 1
            attempts_list.append(guess)

        if attempts == 0:
            print("You've run out of guesses, you lose.\n")
            play_guessing = False
            lose = True
            return lose

play_again = True
while play_again:
    lose = number_guessing(attempts)
    new_game = input("Do you wanna play again? (y/n): ").lower()

    if lose:
        attempts += 5

    if new_game == "n":
        play_again = False
