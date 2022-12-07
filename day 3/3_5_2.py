print("Welcome to love calculator!")
#input names
name1=input("1st name\n").lower()
name2= input("2nd name\n").lower()

#combining the names
combined_string=name1+name2

#searching for the letters
t= combined_string.count("t")
r= combined_string.count("r")
u= combined_string.count("u")
e= combined_string.count("e")

true=t+r+u+e

l= combined_string.count("l")
o= combined_string.count("o")
v= combined_string.count("v")
e= combined_string.count("e")

love=l+o+v+e

#concatenating the 2 results and turning it to int
final=int(str(true)+ str(love))

#interpretation 
if final<10 or final>90:
    print(f"Your fainal score is {final}, and you are compatible as coke and mentos")
elif final>=40 and final<=50:
    print(f"Your final score is {final},and you are comaptible")
else:
    print(f"You final score is {final}")

#verifying the functionality with 2 names: Angela Yu and Jack Bauer
#it should be 53 ("5" for Anglea Yu and "3" for Jack Bauer)