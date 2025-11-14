"""Module providing a function printing python version."""
import random


def get_8_ball_answer():
    user_question = input("Ask you question: ")

    answers = ["Yes! It is certain.", "My sources say no.",
               "No idea (Says in Severus Snape style)", "Yes!", "May be!"]

    computer_response = random.choice(answers)
    return computer_response


computer_response = get_8_ball_answer()
print(f"The 8-ball says: {computer_response}")
