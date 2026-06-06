QUESTIONS = {
    "python": [
        "What is OOP in Python?",
        "What are Python lists and tuples?"
    ],
    "excel": [
        "What is VLOOKUP?",
        "What are Pivot Tables?"
    ],
    "communication": [
        "Tell me about yourself.",
        "How do you handle team conflicts?"
    ],
    "leadership": [
        "Describe a leadership experience.",
        "How do you motivate a team?"
    ],
    "teamwork": [
        "What role do you usually play in a team?",
        "Describe a successful team project."
    ]
}

def get_questions(skills):
    result = []

    for skill in skills:
        if skill in QUESTIONS:
            result.extend(QUESTIONS[skill])

    return result