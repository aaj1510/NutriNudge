import random
from hangman_art import stages, logo
import hangman_words
import fruits_veg
import protein
import carbs
#from replit import clear

print(logo)
game_is_finished = False
lives = len(stages) - 1
guessed = []

choice = input("Make selection:\n 1. Rice and Bread\n 2. Fruits and Vegetables\n 3. Meat and Others\n>>")
match choice:
    case "1":
      word_list = carbs.word_list
    case "2":
      word_list = fruits_veg.word_list
    case "3":
      word_list = protein.word_list


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Hint
print(f'>>>Pssst, use the space bar to enter a space for dual words.<<<')

display = []
for _ in range(word_length):
    display += "_"  

while not game_is_finished:
    print()
    print(f"Incorrect guesses: {','.join(guessed)}")
    print(f"The word has {word_length} letters in it. ")
    guess = input("Guess a letter: ").lower()
    print()
    #Use the clear() function imported from replit to clear the output between guesses.
    #clear()
    input("enter to clear")
    print("\x1B[2J")
    print("cleared")
    print(logo)
    print()
    
    if guess in display:
        print(guess)
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
      print()
      guessed.append(guess)
      print(f"You guessed {guess}, that's not in the word. You lose a life. \nYou have {lives} lives left.")
      
      lives -= 1
      if lives == 0:
          game_is_finished = True
          print("You lose.")
          print(f"The word was {chosen_word}")
    
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])
