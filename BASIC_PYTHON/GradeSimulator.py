# QUIZ_GAME_PROJECT
file_name = "high_score.txt"

score = 0
high_score = 0


# Load high score from file
def load_high_score():
    global high_score
    try:
        file = open(file_name, "r")
        high_score = int(file.read())
        file.close()
    except:
        # If file does not exist or is empty,
        # high_score will remain 0
        high_score = 0


# Save high score to file
def save_high_score():
    file = open(file_name, "w")
    file.write(str(high_score))
    file.close()


# Play Quiz
def play_quiz():
    global score
    score = 0   # reset score each time quiz starts

    questions = [
        "What is the capital of India?",
        "Which language is used for web development?",
        "What is 5 + 3?",
        "Which keyword is used to define a function in Python?"
    ]

    answers = [
        "delhi",
        "python",
        "8",
        "def"
    ]

    for i in range(len(questions)):
        print("\nQ.", questions[i])
        user_answer = input("Your answer: ").lower()

        if user_answer == answers[i]:
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
            print("Correct answer is:", answers[i])


# Main program
def main():
    global high_score

    # Load previous high score
    load_high_score()

    # Ask player name
    name = input("Enter your name: ")

    # Start quiz
    play_quiz()

    # Show final score
    print("\nQuiz Over")
    print(name, "your score is:", score)

    # Compare with high score
    if score > high_score:
        high_score = score
        save_high_score()
        print("🎉 New High Score!")
    else:
        print("High score is:", high_score)


main()
