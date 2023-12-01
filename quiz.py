import random

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

    # Get user input
    user_answer = input("Your answer (a, b, or c): ").lower()

    # Check if the answer is correct
    if user_answer == selected_question["correct_answer"]:
        print("You get 5 lives! Exiting the game.")
        exit()
    else:
        print(f"Incorrect. The correct answer is {selected_question['correct_answer']}.")

# Generate the quiz pool
carbohydrates_questions, fruits_vegetables_questions, protein_questions = generate_quiz_pool()

# Run quizzes for each category
run_quiz("Carbohydrates", carbohydrates_questions)
run_quiz("Fruits and Vegetables", fruits_vegetables_questions)
run_quiz("Protein", protein_questions)
