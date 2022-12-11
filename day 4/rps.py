#rock paper scissors game
import random
paper= ''' 
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|      '''

scissors= '''
          _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ /
|___/\___|_|___/___/\___/|_|  |___/
                                   '''

rock= '''  
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_/
                     
                     '''


a=[rock,paper,scissors]
while True:
    computer_output= random.choice(a)

    user_input= int(input("Choose 0 for rock, 1 for scissors and 2 for paper:\n"))
    if user_input == 0:
        print(f"Your choice is \n {rock}")
    elif user_input==1:
        print(f"Your choice is \n {scissors}")
    elif user_input==2:
        print(f"Your choice is \n {paper}")
    print(f"Computer choice is \n {computer_output}")

    if user_input==0 and computer_output==rock or user_input==1 and computer_output==scissors or user_input==2 and computer_output==paper:
        print("It is draw")
    elif user_input==0 and computer_output==scissors or user_input==1 and computer_output==paper or user_input==2 and computer_output==rock:
        print("You won")
    elif user_input== 0 and computer_output==paper or user_input==1 and computer_output==rock or user_input==2 and computer_output==scissors:
        print("You lost")



# print(user_input)



