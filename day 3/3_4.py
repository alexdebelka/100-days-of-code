print("Welcome to Python Pizza!")
print("Select your Pizza Size!")
size= input("S,M, or L\n")
bill=0
if size== "L":
    bill=20
    print("It costs $20")
elif size=="M":
    bill=15
    print("It costs $15")
elif size == "S":
    bill=10
    print("It costs $10")

add_pepperoni= input("Do you want extra pepperoni? Y or N\n")

if add_pepperoni=="Y":
    bill+=3

add_cheese= input ("Do you want extra cheese? Y or N\n")

if add_cheese=="Y":
    bill+=4

print(f"Your total bill is ${bill}")