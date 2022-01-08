words = ['food' , 'shelter', 'cloths']

import random

chosen_word = random.choice(words)
print("chosen_word : ",chosen_word)

display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Enter a letter: ").lower()

    for l in range(len(chosen_word)):
        if guess == chosen_word[l]:
            display[l] = guess
    print(display)

    if '_' not in display:
        end_of_game = True
        print("Ÿou won")
