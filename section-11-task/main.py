import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_over = False
user_current_score = 0
dealer_current_score = 0

user = []
dealer = []

def compare(user_score, dealer_score):
    if user_score > 21:
        print("You went over 21. You lose.")
    elif dealer_score > 21:
        print("Computer went over 21. You win.")
    elif user_score > dealer_score:
        print("You win.")
    elif user_score == dealer_score:
        print("Draw.")
    else:
        print("You lose.")

def add_card(object):
    object.append(random.choice(cards))

def current_score_print():
    print(f"Your cards: {user}, current score: {user_current_score}")
    print(f"Computer's first card: {dealer[0]}")
    compare(user_current_score, dealer_current_score)

for i in range(2):
    add_card(user)
    add_card(dealer)

while not game_over:
    user_current_score = sum(user)
    dealer_current_score = sum(dealer)
    
    print("\n" * 20)
    print(art.logo)
    print(f"Your cards: {user}, current score: {user_current_score}")
    print(f"Computer's first card: {dealer[0]}")
    
    if user_current_score > 26:
        current_score_print()
        game_over = True
        continue 
    
    choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    
    if choice == "n":
        while dealer_current_score > 17:
            add_card(dealer)
        
        user_current_score = sum(user)
        dealer_current_score = sum(dealer)
        
        print(f"Your final hand: {user}, final score: {user_current_score}")
        print(f"Computer's first hand: {dealer[0]}, final score: {dealer_current_score}")
        
        compare(user_current_score, dealer_current_score)
        
        game_over = True
    elif choice == "y":
        add_card(user)
    else:
        print("Type 'y' or 'n'")