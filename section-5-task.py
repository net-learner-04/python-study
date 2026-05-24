import string
import random

print(r'''
     .--------.
    / .------. \
   / /        \ \
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  | YALE |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'LGB
'.________________.'
''')

print("Welcome to the PyPassword Generator!")

letters = list(string.ascii_lowercase) + list(string.ascii_uppercase)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

passwd = []

for i in range(0, nr_letters):
    passwd.append(letters[random.randint(0, len(letters) - 1)])
    
for j in range(0, nr_symbols):
    passwd.append(symbols[random.randint(0, len(symbols) - 1)])
    
for k in range(0, nr_numbers):
    passwd.append(numbers[random.randint(0, len(numbers) - 1)])

random.shuffle(passwd)

result = ""
for char in passwd:
    result += char

print(f"Here is your password: {result}")