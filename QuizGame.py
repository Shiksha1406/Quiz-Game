import random
questions = [
            {
                "question": "What is the capital of France?",
                "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
                "answer": "B"
                },
                {
                    "question": "Which planet is known as the Red Planet?",
                    "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
                    "answer": "B"
                    }
                    ]
print("Welcome to the quiz game!")
print("Test your knowledge and win!")
print("Here's how to play: ")
print("1. You will be presented with multiple-choice questions.")
print("2. Choose your answer by entering the corresponding number.")
print("3. The game will keep track of your score.")
print("4. You can play as many rounds as you want.")

user_name=input("Enter your Username: ")
print("Welcome", user_name,"to the quiz game!")
while True:
     print("QUIZ GAME MENU")
     print("1. Start the quiz game")
     print("2. Add questions")
     print("3. Exit the quiz game")
    
     choice = input("Enter your choice (1-3): ")
     if choice == "1":
        Answer=input("Are you ready to play? (yes/no): ").lower()
        if Answer=="yes":
            print("Let's start the game!")
        else:
            print("Okay, maybe next time!")
        your_score=0
        print("YourScore:",your_score)
        shuffled_questions = random.sample(questions, len(questions))
        while True:
            for question in shuffled_questions:
                print(question["question"])
                for option in question["options"]:
                    print(option)
                while True:
                    user_answer = input("\nYour answer: ").upper()
                    if user_answer in ["A", "B", "C", "D"]:
                        break
                    print("Invalid input. Please enter A, B, C, or D.")
            
                if user_answer == question["answer"]:
                    print("Correct!\n")
                    your_score += 1
                    print("YourScore:",your_score)
                else:
                    print(f"Wrong! The correct answer is {question['answer']}.")
                print("YourScore:",your_score)
            play_again = input("Would you like to play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thanks for playing! Your Score is",your_score)
                break 
     elif choice == "2":
        print("Add a new question")
        question_text = input("Enter the question: ")
        options = []
        letters = ["A", "B", "C", "D"]
        for letter in letters:
            option = input(f"Enter option {letter}: ")
            options.append(f"{letter}. {option}")
        while True:
            correct_answer = input("Which option is correct? (A/B/C/D): ").upper()
            if correct_answer in letters:
                break
            print("Invalid input. Please enter A, B, C, or D.")
        new_question = {
                "question": question_text,
                "options": options,
                "answer": correct_answer
            }
        questions.append(new_question)
        print("Question added successfully!")
     elif choice == "3":
        print("Goodbye!!")
        break
     else:
        print("Invalid choice. Please choose a valid option.")