logo = r'''               
   ___________
   \         /
    )_______(
    |"""""""|_.-._,.---------.,_.-._
    |       | | |               | | ''-.
    |       |_| |_             _| |_..-'
    |_______| '-' `'---------'` '-'
    )"""""""(
   /_________\
   `'-------'`
  .-------------.
 /_______________\
'''

bidder_info = {}
end_of_auction = False
max_value = 0
winner = ""

while not end_of_auction:
    print(logo)
    print("\nWelcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    
    bidder_info[name] = bid
    
    if input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() == "no":
        over = True
    else:
        print("\n" * 20)

for bidder in bidder_info:
    if bidder_info[bidder] > max_value:
        max_value = bidder_info[bidder]
        winner = bidder
        
print(f"The winner is {winner} with a bid of ${max_value}.")