
from flask import Flask, render_template, request, redirect, url_for, flash
import os, re, sqlite3
from datetime import datetime
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(BASE_DIR, "resume_screening.db")
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
ALLOWED_EXTENSIONS = {"pdf", "txt"}

app = Flask(__name__)
app.secret_key = "fsp-resume-screening-demo"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

SKILLS = [
    "python","java","c++","c#","javascript","typescript","html","css","react",
    "angular","node.js","node","express","flask","django","spring boot",
    "sql","mysql","postgresql","mongodb","oracle","git","github","docker",
    "aws","azure","machine learning","deep learning","natural language processing",
    "nlp","tensorflow","pytorch","scikit-learn","pandas","numpy","data analysis",
    "data structures","algorithms","rest api","api","power bi","excel",
    "communication","leadership","problem solving","java dsa","full stack"
]

def init_db():
    con = sqlite3.connect(DB)
    con.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            filename TEXT,
            score REAL,
            recommendation TEXT,
            matched_skills TEXT,
            missing_skills TEXT,
            created_at TEXT
        )
    """)
    con.commit()
    con.close()

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text(path):
    ext = path.rsplit(".", 1)[1].lower()
    if ext == "pdf":
        reader = PdfReader(path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def find_email(text):
    m = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    return m.group(0) if m else "Not detected"

def find_name(text):
    for line in text.splitlines():
        line = line.strip()
        if 2 <= len(line.split()) <= 4 and not re.search(r"@|\d", line):
            if len(line) < 60:
                return line
    return "Candidate"

def find_skills(text):
    lower = clean_text(text)
    found = []
    for skill in SKILLS:
        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"
        if re.search(pattern, lower):
            found.append(skill)
    return sorted(set(found))

def calculate_score(resume_text, job_description):
    resume = clean_text(resume_text)
    job = clean_text(job_description)
    if not resume or not job:
        return 0.0
    try:
        vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        matrix = vectorizer.fit_transform([resume, job])
        return round(float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0] * 100), 2)
    except ValueError:
        return 0.0

def recommendation(score):
    if score >= 75:
        return "Highly Recommended"
    if score >= 55:
        return "Recommended"
    if score >= 35:
        return "Needs Review"
    return "Low Match"

def save_candidate(data):
    con = sqlite3.connect(DB)
    con.execute("""
        INSERT INTO candidates
        (name,email,filename,score,recommendation,matched_skills,missing_skills,created_at)
        VALUES (?,?,?,?,?,?,?,?)
    """, (
        data["name"], data["email"], data["filename"], data["score"],
        data["recommendation"], ", ".join(data["matched"]),
        ", ".join(data["missing"]), datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    con.commit()
    con.close()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        job_description = request.form.get("job_description", "").strip()
        resume = request.files.get("resume")

        if not job_description:
            flash("Please enter a job description.", "error")
        elif not resume or resume.filename == "":
            flash("Please upload a resume.", "error")
        elif not allowed_file(resume.filename):
            flash("Only PDF and TXT files are supported.", "error")
        else:
            filename = secure_filename(resume.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            resume.save(path)

            text = extract_text(path)
            resume_skills = find_skills(text)
            job_skills = find_skills(job_description)
            matched = sorted(set(resume_skills) & set(job_skills))
            missing = sorted(set(job_skills) - set(resume_skills))
            score = calculate_score(text, job_description)
            rec = recommendation(score)

            result = {
                "name": find_name(text),
                "email": find_email(text),
                "filename": filename,
                "score": score,
                "recommendation": rec,
                "resume_skills": resume_skills,
                "matched": matched,
                "missing": missing
            }
            save_candidate(result)
            flash("Resume screened successfully.", "success")

    return render_template("index.html", result=result)

@app.route("/candidates")
def candidates():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    rows = con.execute("SELECT * FROM candidates ORDER BY score DESC, id DESC").fetchall()
    con.close()
    return render_template("candidates.html", candidates=rows)

@app.route("/about")
def about():
    return render_template("about.html")

init_db()

if __name__ == "__main__":
    app.run(debug=True)
