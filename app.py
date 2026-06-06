from flask import Flask, render_template, request
from PyPDF2 import PdfReader
from skills import extract_skills
from interview_questions import get_questions
from career_recommendation import recommend_career
from gemini_analyzer import analyze_resume
from flask import send_file
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

app = Flask(__name__)

last_report = {}

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["resume"]

    if not file:
        return "No File Uploaded"

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    reader = PdfReader(filepath)

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted
    print(text)
    skills = extract_skills(text)
    print("Detected Skills:", skills)

    questions = get_questions(skills)
    print("Questions:", questions)

    try:
        analysis = analyze_resume(text)

    except Exception:

        analysis = """
        <h3>📈 Strengths</h3>
        <ul>
        <li>Resume uploaded successfully</li>
        <li>Skills detected from resume</li>
        <li>Career recommendations generated</li>
        </ul>

        <h3>⚠ Areas To Improve</h3>
        <ul>
        <li>Add more technical skills</li>
        <li>Improve project experience</li>
        <li>Include measurable achievements</li>
        </ul>

        <h3>🚀 Next Steps</h3>
        <ul>
        <li>Learn recommended skills</li>
        <li>Practice interview questions</li>
        <li>Update resume regularly</li>
        </ul>
        """
    print(analysis)

    careers = recommend_career(skills)

    all_skills = [
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

    missing_skills = []

    for skill in all_skills:
        if skill not in skills:
           missing_skills.append(skill)

    missing_skills = missing_skills[:8]

    score = min(len(skills) * 10, 100)

    if score <= 40:
        score_status = "⚠ Needs Improvement"

    elif score <= 70:
        score_status = "👍 Good Resume"

    else:
        score_status = "🏆 Excellent Resume"
    

    global last_report

    last_report = {
        "score": score,
        "skills": skills,
        "missing_skills": missing_skills,
        "careers": careers,
        "questions": questions
    }


    return render_template(
        "result.html",
        skills=skills,
        score=score,
        questions=questions,
        careers=careers,
        missing_skills=missing_skills,
        analysis=analysis,
        score_status=score_status
    )

@app.route("/download-report")
def download_report():

    global last_report

    pdf_file = "Resume_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "🤖 AI Resume Analyzer Professional Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"<font color='green'><b>Resume Score: {last_report['score']}/100</b></font>",
            styles["Heading2"]
        )
    )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph("Detected Skills", styles["Heading2"])
    )

    for skill in last_report["skills"]:
        content.append(
            Paragraph(f"• {skill.title()}", styles["BodyText"])
        )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph("Recommended Skills", styles["Heading2"])
    )

    for skill in last_report["missing_skills"]:
        content.append(
            Paragraph(f"• {skill.title()}", styles["BodyText"])
        )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph("Recommended Careers", styles["Heading2"])
    )

    for career in last_report["careers"]:
        content.append(
            Paragraph(f"💼 {career}", styles["BodyText"])
        )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph("Interview Questions", styles["Heading2"])
    )

    for question in last_report["questions"]:
        content.append(
            Paragraph(f"• {question}", styles["BodyText"])
        )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph("AI Insights", styles["Heading2"])
    )

    content.append(
        Paragraph(
            "✓ Resume uploaded successfully",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "✓ Skills detected from resume",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "✓ Career recommendations generated",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 15))

    content.append(
        Paragraph(
            "<b>Generated by AI Resume Analyzer</b>",
            styles["Italic"]
        )
    )

    doc.build(content)

    return send_file(
        pdf_file,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)