from question import Question
import random

question_prompts = [
    "What color are apples?\n(a) Red\n(b) Green\n(c) Pink\n(d) Yellow\n",
    "Which animal is known as the King of the Jungle?\n(a) Tiger\n(b) Lion\n(c) Elephant\n(d) Bear\n",
    "How many days are there in a week?\n(a) 5\n(b) 6\n(c) 7\n(d) 8\n",
    "What planet do we live on?\n(a) Mars\n(b) Venus\n(c) Earth\n(d) Jupiter\n",
    "Which shape has three sides?\n(a) Square\n(b) Circle\n(c) Triangle\n(d) Rectangle\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "c"),
]
random.shuffle(questions)

def run_test(questions):
    score = 0
    for question in questions:
        ans = input(question.prompt + "Enter your answer: ")
        if ans == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
