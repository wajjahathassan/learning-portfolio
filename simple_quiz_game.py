"""Module providing a function printing python version."""


def quiz_questions():
    question_to_ask = "Is python a snake?"
    correct_answer = "Yes"
    first_pair = {"Question": question_to_ask, "Answer": correct_answer}

    question_to_ask = "Are pythons venomous?"
    correct_answer = "No"
    second_pair = {"Question": question_to_ask, "Answer": correct_answer}

    quiz_bank = [first_pair, second_pair]

    return quiz_bank


def ask_question(question_to_ask, correct_answer):
    print(question_to_ask)

    player_answer = input("Enter your answer (Yes/No): ")

    if player_answer == correct_answer:
        return "Your answer is correct! Well done!"
    else:
        return "Sorry, that's not correct."


quiz_bank = quiz_questions()

first_pair = quiz_bank[0]
second_pair = quiz_bank[1]

first_result = ask_question(first_pair["Question"], first_pair["Answer"])
print(first_result)

second_result = ask_question(second_pair["Question"], second_pair["Answer"])
print(second_result)
