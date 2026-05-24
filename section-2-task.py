print("Welcome to the tip calculator!")

total_bil = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))

tip_calculate = total_bil * (tip / 100)

result = round(((tip_calculate + total_bil) / people), 2)

print(f"Each person should pay: ${result}")