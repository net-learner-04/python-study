import random
from art import logo

NUMBER = random.randint(1,100)
EASY_LEVEL = 10
HARD_LEVEL = 5

game_over = False

def level_check():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "hard":
        return HARD_LEVEL
    elif level == "easy":
        return EASY_LEVEL
    else:
        print("Only type 'easy' or 'hard'.")

print(logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")
    
life = level_check()    

while not game_over:
    print(f"You have {life} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > NUMBER:
        print("Too high.\nGuess again.")
        life -= 1
    elif guess < NUMBER:
        print("Too low.\nGuess again.")
        life -=1
    else:
        game_over = True
        print(f"You got it! The answer was {guess}.")
        
    if life == 0:
        game_over = True
        print("You've run out of guesses. Refresh the page to run again.")