import random

r = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


p = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

s = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice = ["rock", "paper", "scissors"]

computer = random.randint(0,len(choice)-1)

user = int(input('What do you choose? '
                 'Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

if user > 2:
    print("Error")
    exit(1)

if choice[computer] == "rock":
    if choice[user] == "rock":
        print(f"{r}\nComputer chose:\n{r}\nDraw")
    elif choice[user] == "paper":
        print(f"{p}\nComputer chose:\n{r}\nYou win")
    else:
        print(f"{s}\nComputer chose:\n{r}\nYou lose")
elif choice[computer] == "paper":
    if choice[user] == "rock":
        print(f"{r}\nComputer chose:\n{p}\nYou lose")
    elif choice[user] == "paper":
        print(f"{p}\nComputer chose:\n{p}\nDraw")
    else:
        print(f"{s}\nComputer chose:\n{p}\nYou win")
elif choice[computer] == "scissors":
    if list[user] == "rock":
        print(f"{r}\nComputer chose:\n{s}\nYou win")
    elif list[user] == "paper":
        print(f"{p}\nComputer chose:\n{s}\nYou lose")
    else:
        print(f"{s}\nComputer chose:\n{s}\nDraw")