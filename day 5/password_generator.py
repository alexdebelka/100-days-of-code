import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))


output_string= ""
while nr_letters !=-1 or nr_numbers !=-1 or nr_symbols !=-1:
    if nr_letters !=-1:
        output_string+=letters[random.randint(0, len(letters)-1)]
        nr_letters-=1
   
    if nr_numbers!=-1:
        output_string += numbers[random.randint (0, len(numbers)-1)]
        nr_numbers-=1

    if nr_symbols !=-1:
        output_string+= symbols[random.randint(0, len(symbols)-1)]
        nr_symbols-=1
    
print(output_string)
# edcba43210$#!
# e4$d3#c2!b1a0       