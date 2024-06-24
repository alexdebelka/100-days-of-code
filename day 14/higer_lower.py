from art import logo
from art import vs
from game_data import data
import random


print(logo)

def compare_follower(celeb_a, celeb_b):
    return celeb_a['follower_count'] > celeb_b['follower_count']
    
def get_user_input():
    guess= input('Who has more followers? Type "A" or "B" ').upper()
    return guess


def game():
    score=0
    game_should_continue= True
    celeb_a= random.choice(data)
    celeb_b= random.choice(data)
    while game_should_continue:
        while celeb_a==celeb_b:
            celeb_b= random.choice(data)
        print(f"Compare A: {celeb_a['name']}, {celeb_a['description']}, from {celeb_a['country']}")
        print(vs)
        print(f"Against B: {celeb_b['name']}, {celeb_b['description']}, {celeb_b['country']}")

        guess= get_user_input()

        if (guess=="A" and compare_follower(celeb_a,celeb_b)) or (guess=="B" and not compare_follower(celeb_a,celeb_b)):
            score+=1
            print(f'You are right! Curent score {score}')
            celeb_a=celeb_b
            celeb_b=random.choice(data)
        else:
            game_should_continue= False
            print(f"Sorry, that's wrong. Final score: {score}")
game()