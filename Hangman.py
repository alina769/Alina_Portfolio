import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for i in range(len(chosen_word)):
    display += "_"
print(display)

lives = 6

end_of_game = False
while not end_of_game and lives > 0:
    print("\n")
    guess = input("Guess a letter: \n").lower()
    print("\n")
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")

    if guess not in display:
        lives -= 1
        print("You lost one life!")

    if lives <= 0:
        print("\n")
        print("You loose!")

    print(stages[lives])
