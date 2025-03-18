import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)
game_over=False
c=[]
# TODO-1: - Use a while loop to let the user guess again.
while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

# TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            c.append(guess)
        elif letter in c:
            display+=letter
        else:
            display += "_"

    print(display)
    if "_" not in display:
        game_over=True
        print("You win")
