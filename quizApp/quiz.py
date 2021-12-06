from Question import Question

question_prompts = [
    "What is Dwight Shrewts Job Title?\n(a) Assistant Regional Manager\n(b) Assistant to the Regional Manager\n(c) Sales Person\n\n",
    "What is the name of Kevins Band?\n(a) Status Pro\n(b) Scrantonicity\n(c) Kevin & the Zits\n\n",
    "Where did Jim propose to Pam?\n(a) At Niagra Falls\n(b) On the office roof\n(c) At a gas station\n\n",
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]


def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got", score, "out of", len(questions))


run_quiz(questions)
