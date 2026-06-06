from google import genai
import os

API_KEY = os.getenv("GEMINI_API_KEY")

def analyze_resume(text):
    client = genai.Client(api_key=API_KEY)

def analyze_resume(text):

    prompt = f"""
    Analyze this resume and provide:

    1. Detected Skills
    2. Resume Score out of 100
    3. Missing Skills
    4. Career Recommendations
    5. 10 Interview Questions

    Resume Text:
    {text}

    Return the response in clean HTML format using:
    <h2>, <h3>, <ul>, <li>, <p>

    Create a professional report layout.

    Use:
    <h2> for section titles
    <ul><li> for lists
    <p> for explanations

    Do not use markdown symbols like ### or **.
    Only return valid HTML.
    Do not return markdown.
    Do not return code blocks.
    """


    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    print("STARTING TEST")

    try:
        print(analyze_resume("""
Python
SQL
Flask
Data Analyticss
Power BI
Excel
Leadership
Communication
"""))
    except Exception as e:
        print("ERROR:")
        print(e)