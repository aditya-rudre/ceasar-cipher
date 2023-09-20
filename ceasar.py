from art import (logo, alphabet)


print(logo)

def ceasar(plain_text, shift_count, chosen_destination):
    final_word=""
    for letter in plain_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            if chosen_destination=="encode":
                new_position= position + shift_count
            elif chosen_destination=="decode":
                new_position= position - shift_count
            final_word+=alphabet[new_position]
        else:
            final_word+=letter

    print(f"Here's is your {chosen_destination}d result : {final_word}") 
    
should_continue = True

while should_continue:
    choose=input("Type 'encode' to incrypt and 'decode' to decrypt : ")
    text=input("Type the word that you want to cipher/decipher : ").lower()
    shift=int(input("Type the shift number:"))
    shift=shift%26
    ceasar(plain_text=text, shift_count=shift, chosen_destination=choose)
    output=input("Type 'yes' if you want to go again, otherwise please type 'no' : ").lower()
    if output=="no":
        should_continue=False
        print("Goodbye! See you Again :)")






       
        
