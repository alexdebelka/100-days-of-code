#print welcome message
print("Welcome to love calculator!")
#input names
s=input("1st name\n").lower()
t= input("2nd name\n").lower()
#calculate how many times does the letter from the words "True" and "Love" appear in the names
x=s.count("t") +s.count("r") + s.count("u") + s.count("e") + s.count("l") + s.count("o") + s.count("v") +s.count("e")
z=t.count("t") + t.count("r") + t.count("u") + t.count("e") + t.count("l") + t.count("o") + t.count("v") + t.count("e")
#adding the 2 numbers
final=x+z
#interpretation 
if final<10 or final>90:
    print("You are compatible as coke and mentos")
elif final>=40 and final<=50:
    print("You are meh, but comaptible")
else:
    print("You are compatible")