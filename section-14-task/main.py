import random
import art
import game_date

def compare(compare, against):
    if compare["follower_count"] > against["follower_count"]:
        score[0] = score[0] + 1
        print(f"You're right! Current score: {score[0]}")
    elif compare["follower_count"] < against["follower_count"]:
        print(f"Sorry, that's wrong. Final score: {score[0]}")
        game_over[0] = True

def format(info):
    info_name = info["name"]
    info_description = info["description"]
    info_country = info["country"]
    return f"{info_name}, a {info_description}, from {info_country}"

score = [0]
game_over = [False]

compare_a = {}
against_b = {}

compare_a = random.choice(game_date.data)

while not game_over[0]:
    against_b = random.choice(game_date.data)
    
    while compare_a == against_b:
        against_b = random.choice(game_date.data)
    
    print(art.logo)
    print(f"Compare A: {format(compare_a)}.")
    print(art.vs)
    print(f"Against B: {format(against_b)}.")
    
    select = input("Who has more followers? Type 'A' or 'B': ").upper()
    
    print("\n" * 40)
    print(art.logo)
    
    if select == "A":
        compare(compare_a, against_b)
        against_b = compare_a
    elif select == "B":
        compare(against_b, compare_a)
    
    if not game_over[0]:
        compare_a = against_b