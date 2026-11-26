# Online Examination System

def start_exam():

    questions = [
        "1. Which language is used for Python programming?",
        "2. Which data type stores multiple values?",
        "3. Which keyword is used to define a function?",
        "4. Which symbol is used for comments in Python?",
        "5. Which function is used to display output?"
    ]

    options = [
        ["a. Java", "b. Python", "c. C++", "d. HTML"],
        ["a. List", "b. Integer", "c. Float", "d. Boolean"],
        ["a. class", "b. return", "c. def", "d. print"],
        ["a. //", "b. /*", "c. $", "d. #"],
        ["a. input()", "b. print()", "c. scan()", "d. display()"]
    ]

    answers = ['b', 'a', 'c', 'd', 'b']

    score = 0
    correct = 0
    wrong = 0
    skipped = 0

    print("\n================================")
    print("     ONLINE EXAMINATION SYSTEM")
    print("================================")

    name = input("Enter student name: ")

    print("\nWelcome", name)
    print("Total Questions:", len(questions))
    print("Each Question: 2 Marks")
    print("Passing Percentage: 40%")

    print("\nExam Started!\n")

    for i in range(len(questions)):

        print(questions[i])

        for option in options[i]:
            print(option)

        user_answer = input("Enter your answer (a/b/c/d): ")
        user_answer = user_answer.lower().strip()

        if user_answer == "":
            print("Question Skipped!\n")
            skipped += 1

        elif user_answer not in ['a', 'b', 'c', 'd']:
            print("Invalid Input! Question Skipped.\n")
            skipped += 1

        elif user_answer == answers[i]:
            print("Correct Answer!\n")
            correct += 1
            score += 2

        else:
            print("Wrong Answer!\n")
            wrong += 1

    total_marks = len(questions) * 2
    percentage = (score / total_marks) * 100

    print("\n================================")
    print("          EXAM RESULT")
    print("================================")

    print("Student Name:", name)
    print("Total Questions:", len(questions))
    print("Correct Answers:", correct)
    print("Wrong Answers:", wrong)
    print("Skipped Questions:", skipped)
    print("Total Score:", score, "/", total_marks)
    print("Percentage:", percentage, "%")

    if percentage >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")

    print("================================")
    print("       EXAM COMPLETED")
    print("================================")
start_exam()