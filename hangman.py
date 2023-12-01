"""This game is a modified version of Hangman, whose rules / description 
can be found at https://github.com/rrice2004/Python-Hangman/tree/main
We adopted inspiration on how the gameflow would be (guessing and progress functions), and ignored
the narrations."""

"""INSERT DESCRIPTION/OBJECTIVE OF THE GAME HERE"""

import random
from hangman_art import stages, logo,plate,youwin
import fruits_veg
import protein
import carbs


print(logo)
lives = len(stages) - 1 #hangman stages from hangman art
guessed = [] #create an empty list

#set initilisation to default value (false)
game_is_finished = False
carb_finished = False
fruits_veg_finished = False
protein_finished = False
booll = False

name = input("Hey there! What's your name?:")

print(f"\nExcellent {name}!! Let's play a game called Hangman with healthy eating!")

"""The following code is for the quiz"""
def generate_quiz_pool():
    # Define questions and answers for each category
    carbohydrates_questions = [
        {"question": "Which of the following is a good source of fiber?", "options": ["a. White rice", "b. Oats", "c. Potato"], "correct_answer": "b"},
        {"question": "What is a complex carbohydrate?", "options": ["a. Sugar", "b. Starch", "c. Both a and b"], "correct_answer": "c"},
        {"question": "Which of the following is a whole grain?", "options": ["a. White bread", "b. Brown rice", "c. Pasta"], "correct_answer": "b"}
    ]

    fruits_vegetables_questions = [
        {"question": "How many servings of vegetables are recommended per day?", "options": ["a. 1-2 servings", "b. 3-4 servings", "c. 5 or more servings"], "correct_answer": "c"},
        {"question": "Which fruit is rich in potassium?", "options": ["a. Apple", "b. Banana", "c. Orange"], "correct_answer": "b"},
        {"question": "What is a cruciferous vegetable?", "options": ["a. Tomato", "b. Broccoli", "c. Carrot"], "correct_answer": "b"}
    ]

    protein_questions = [
        {"question": "Which of the following is a plant-based source of protein?", "options": ["a. Chicken breast", "b. Lentils", "c. Salmon"], "correct_answer": "b"},
        {"question": "What is a complete protein source?", "options": ["a. Eggs", "b. Quinoa", "c. Both a and b"], "correct_answer": "c"},
        {"question": "Which type of protein is found in beans?", "options": ["a. Animal-based protein", "b. Plant-based protein", "c. Fungal protein"], "correct_answer": "b"}
    ]

    return carbohydrates_questions, fruits_vegetables_questions, protein_questions

def run_quiz(category, questions):
    
    # Randomly select a question from the pool
    selected_question = random.choice(questions)

    # Display the question and options
    print(f"\n{category} Quiz:")
    print(selected_question["question"])
    for option in selected_question["options"]:
        print(option)

    # Get user input, lower 
    user_answer = input("Your answer (a, b, or c): ").lower()

    # Check if the answer is correct
    if user_answer == selected_question["correct_answer"]:
        print("You get 7 lives!")
        return True
        
    else:
        print(f"Incorrect. The correct answer is {selected_question['correct_answer']}.")

# Call function and store questions into variables
carbohydrates_questions, fruits_vegetables_questions, protein_questions = generate_quiz_pool()

#External while loop to check if all 3 categories are won, else, game continues until all 3 categories are won.
while (carb_finished and fruits_veg_finished and protein_finished) != True:
    
    print(plate) #plate ascii

    #get user input on category selection
    choice = input("Make selection(1/2/3):\n 1. Rice and Bread\n 2. Fruits and Vegetables\n 3. Meat and Others\n>>")
    
    #reset choice and word_list values respectively, to reference later
    match choice:
        case "1":
          word_list = carbs.word_list
          choice = "Rice and Bread" 
          
        case "2":
          word_list = fruits_veg.word_list
          choice = "Fruits and Vegetables"
          
        case "3":
          word_list = protein.word_list
          choice = "Meat and Others"
    
        #if user does not select 1,2,3, prompt again and give error    
        case default:
          print("Invalid Input, please select 1,2, or 3")
          continue
       
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    game_is_finished = False

    print(f'>>>Pssst, use the space bar to enter a space for dual words.<<<')

    #Initalise empty list. Display will be indicative underscores _ _ _ _ _ to facilitate Hangman 
    display = []
    for _ in range(word_length):
        display += "_"  
    
    """The code for this function was taken from: 
    https://github.com/rrice2004/Python-Hangman/blob/main/hangman.py"""

    #Gameplay starts from here:
    while not game_is_finished:
       
        print()
        print(f"You selected:{choice}")
        print(f"Incorrect guesses: {','.join(guessed)}")
        print(f"The word has {word_length} letters in it. ")
        guess = input("Guess a letter: ").lower()
        print()
        #Clear the screen
        input("enter to clear")
        print("\x1B[2J")
        print("cleared")
        print(logo)
        print()

        
        """Perform some data/user validation here"""
        #User input for guess cannot be > 1 letter at a time. 
        length = len(guess)
        if length > 1:
           print("Please enter 1 letter at a time")
           continue
        
        #if user has already guessed the letter...
        if guess in display:
            print(guess)
            print(f"You've already guessed {guess}")

        #display letter at it's rightful position(s), if user guessed correctly
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(f"{' '.join(display)}")

        #Decrement life if user guesses wrongly
        if guess not in chosen_word:
          print()
          guessed.append(guess)
          print(f"You guessed {guess}, that's not in the word. You lose a life. \nYou have {lives} lives left.")
          
          lives -= 1

          #After 7 chances are gone, user has a chance of redemption, with a quiz
          if lives == -1:
              print("You lose. You have ")
              print("Redeem a chance to continue, with 7 extra lives!")

              #run the respective quizzes, according to user's initial selection of category
              match choice:
                case "Rice and Bread":
                  print("hello")
                  booll = run_quiz("Carbohydrates", carbohydrates_questions) 
                  if booll == True:
                     lives = 6
                     continue
                  else:
                    carb_finished =  True
                    fruits_veg_finished = True
                    protein_finished = True
                    break
                      
                     
                case "Fruits and Vegetables":
                  booll = run_quiz("Fruits and Vegetables", fruits_vegetables_questions)
                  if booll == True:
                     lives = 6
                     continue
                  else:
                    carb_finished =  True
                    fruits_veg_finished = True
                    protein_finished = True
                    break

                case "Meat and Others":
                  run_quiz("Protein", protein_questions)
                  if booll == True:
                     lives = 6
                     continue
                  else:
                    print("YOU DIE LOGO!") #SRI HELP thanks <3
                    carb_finished = True
                    fruits_veg_finished = True
                    protein_finished = True
                    break
        
        #If there are no more _ , user has succesfully won this category
        if not "_" in display:
           game_is_finished = True
           print(youwin) #print ascii 

           #Update category win
           match choice:
              case "Rice and Bread":
                carb_finished = True
              case "Fruits and Vegetables":
                fruits_veg_finished = True
              case "Meat and Others":
                protein_finished = True

#print(carb_finished)
#print(fruits_veg_finished)
#print(protein_finished)
#print(stages[lives])