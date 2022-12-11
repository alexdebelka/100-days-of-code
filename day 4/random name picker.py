import random

name_in=input("Give me the names wihch want to play, seppareted by a comma: \n" )
name= name_in.split(", ")
print(f" The person who will pay is {random.choice(name)}")

