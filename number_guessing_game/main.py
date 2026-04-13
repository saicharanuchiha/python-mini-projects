import random
from art import logo

EASY_TURNS = 10
HARD_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high")
        return turns -1
    elif guess < answer:
        print("Too low")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}")

def set_difficulty():
    difficulty = input("Choose a difficulty: Type 'easy' or 'hard' ")
    if difficulty == "easy":
        return EASY_TURNS
    elif difficulty == "hard":
        return HARD_TURNS

def game():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")
    turns = set_difficulty()
    guess = 0
    while guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining to gues the number")
        guess = int(input("make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You ran out of guesses")
        elif guess != answer:
            print("Guess again")

game()