from game_data import data
from art import logo
import random
a=random.choice(data)
b=random.choice(data)
if a==b:
    b=random.choice(data)
def acc(at):
    name=at["name"]
    des=at["description"]
    c=at["country"]
    return f"{name},a {des} from {c}"
def ans(guess,act,bct):
    if act>bct:
        return guess=="a"
    else:
        return guess=="b"
score=0
play_game=True
b = random.choice(data)
while play_game:
    a = b
    b = random.choice(data)
    if a == b:
        b = random.choice(data)
    print(f"Compare A: {acc(a)}.")
    print("vs")
    print(f"Against B: {acc(b)}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n"*20)
    print(logo)
    act=a["follower_count"]
    bct=b["follower_count"]
    is_correct = ans(guess, act, bct)

    # Give user feedback on their guess.
    # score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        play_game = False



