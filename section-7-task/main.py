import random
from words import word_list
from ascii_art import logo, HANGMANPICS

print(f"{logo}\n")

word = random.choice(word_list)

for char in word_list:
    print(f"{char} ", end="")
print("\n")

status = []
for a in range(len(word)):
    status.append("_")

for i in range(len(word)):
    print("_", end="")
    if i == len(word) - 1:
        print("\n")

game_over = False

life = 6
stage = 0
letter_check = []

while not game_over:
    word_check = False
    
    print(HANGMANPICS[stage])
    
    print(f"\n******************** < {life} > / 6 Lives Left ********************")
    guess = input("\nGuess a letter: ").lower()
    
    if guess in letter_check:
        print(f"You've already guessed {guess}")
    
    for j in range(len(word)):
        if word[j] == guess:
            status[j] = word[j]
            letter_check.append(guess)
            word_check = True
        print(status[j], end="")
    print("\n")
    
    if not word_check:
        life -= 1
        stage += 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
    
    if life == 0:
        game_over = True
        print(HANGMANPICS[stage])
        print(f"\n******************** It Was < {word} >, You lose. ********************\n")
    
    if list(word) == status:
        game_over = True
        print("******************** You win. ********************\n")

for k in range(len(status)):
    print(f"{status[k]}", end="")