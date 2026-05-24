import string
import art

"""
def encrypt(original_text, shift_amount):
    cipher_text = ""
    
    for i in range(len(original_text)):
        index = alphabet.index(original_text[i])
        index += shift_amount
        
        if index > len(alphabet):
            index -= len(alphabet)
            
        cipher_text += alphabet[index]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    output_text = ""
    
    for j in range(len(original_text)):
        index = alphabet.index(original_text[j])
        index -= shift_amount

        if index < 0:
            index += len(alphabet)
        
        output_text += alphabet[index]
    print(f"Here is the encoded result: {output_text}")
"""

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    for letter in original_text:
        if letter in alphabet:
            if encode_or_decode == "decode":
                shift_amount *= -1
            
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is the encoded result: {output_text}")

print(f"\n{art.logo}\n")

check = True

while check:
    
    alphabet = list(string.ascii_lowercase)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
    if restart == "no":
        check = False