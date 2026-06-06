def recommend_career(skills):

    skills = [s.lower() for s in skills]

    if "power bi" in skills or "data analytics" in skills:
        return ["Data Analyst", "Business Analyst"]

    elif "python" in skills and "flask" in skills:
        return ["Python Developer", "Backend Developer"]

    elif "networking" in skills:
        return ["Network Engineer", "System Administrator"]

    elif "cyber security" in skills:
        return ["Cyber Security Analyst", "Security Engineer"]

    else:
        return ["Software Engineer", "IT Support Specialist"]