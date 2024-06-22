#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
logo= """  /$$$$$$                                                 /$$     /$$                                                         /$$                          
 /$$__  $$                                               | $$    | $$                                                        | $$                          
| $$  \__/ /$$   /$$  /$$$$$$   /$$$$$$$ /$$$$$$$       /$$$$$$  | $$$$$$$   /$$$$$$        /$$$$$$$  /$$   /$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ 
| $$ /$$$$| $$  | $$ /$$__  $$ /$$_____//$$_____/      |_  $$_/  | $$__  $$ /$$__  $$      | $$__  $$| $$  | $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$|_  $$| $$  | $$| $$$$$$$$|  $$$$$$|  $$$$$$         | $$    | $$  \ $$| $$$$$$$$      | $$  \ $$| $$  | $$| $$ \ $$ \ $$| $$  \ $$| $$$$$$$$| $$  \__/
| $$  \ $$| $$  | $$| $$_____/ \____  $$\____  $$        | $$ /$$| $$  | $$| $$_____/      | $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$_____/| $$      
|  $$$$$$/|  $$$$$$/|  $$$$$$$ /$$$$$$$//$$$$$$$/        |  $$$$/| $$  | $$|  $$$$$$$      | $$  | $$|  $$$$$$/| $$ | $$ | $$| $$$$$$$/|  $$$$$$$| $$      
 \______/  \______/  \_______/|_______/|_______/          \___/  |__/  |__/ \_______/      |__/  |__/ \______/ |__/ |__/ |__/|_______/  \_______/|__/      
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           """



# Allow the player to submit a guess for a number between 1 and 100.
difficulty= input("You want it easy or hard? \n")
computer_choice= random.choice(range(101))
print(f"The computer's choice is {computer_choice}")
guess= int(input("Guess a number between 1 and 100: \n"))
chances=0
guess_again=0

if difficulty== "easy":
    difficulty=0
    chances=10
elif difficulty== "hard":
    difficulty=1
    chances=5
else:
    print("You didn't choose the right difficulty. Bye!")

def choices(guess, computer_choice):
    if guess<computer_choice:
        print("Too low")
    elif guess>computer_choice:
        print("Too high")
    elif guess==computer_choice:
        print(f"You guessed the number, it is {computer_choice}")

while difficulty==0 and chances!=0:
    if chances==10:
        choices(guess,computer_choice)
    else:
        guess_again= int(input("Try an other number:\n"))
        guess=guess_again
        choices(guess, computer_choice)
    if guess==computer_choice or guess_again==computer_choice:
        break

    chances-=1
    if chances>0:
        print(f"You have {chances} attempts to go!")
    elif chances==0:
        print("You ran out of attempts.")
        break

while difficulty==1 and chances!=0:
    if chances==5:
        choices(guess,computer_choice)
    else:
        guess_again= int(input("Try an other number:\n"))
        guess=guess_again
        choices(guess, computer_choice)
    if guess==computer_choice or guess_again==computer_choice:
        break

    chances-=1
    if chances>0:
        print(f"You have {chances} attempts to go!")
    elif chances==0:
        print("You ran out of attempts.")
        break


# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).