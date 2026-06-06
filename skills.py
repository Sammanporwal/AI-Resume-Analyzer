SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "mysql",
    "html",
    "css",
    "javascript",
    "flask",
    "linux",
    "networking",
    "cyber security",
    "machine learning",
    "data science",
    "data analytics",
    "power bi",
    "leadership",
    "technical skills",
    "soft skills",
    "excel",
    "communication",
    "teamwork",
    "problem solving"
]

def extract_skills(text):
    found_skills = []

    text = text.lower()

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills