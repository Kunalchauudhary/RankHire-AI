# 🚀 RankHire-AI

**AI-Powered Resume Screening & Candidate Ranking System**

RankHire-AI is a web-based AI-powered resume screening system that helps recruiters quickly analyze and rank candidates based on a given job description. 

The system uses Natural Language Processing (NLP) techniques such as **TF-IDF** and **Cosine Similarity** to compare resumes with job requirements and generate a candidate matching score.

---

## 📌 Project Overview

Recruiters often receive hundreds of resumes for a single job position. Manually reviewing every resume can be time-consuming and inefficient. **RankHire-AI** automates the initial resume screening process.

The recruiter provides a Job Description and uploads candidate resumes. The system then:
1. Extracts text from resumes.
2. Processes and cleans the extracted text.
3. Compares resumes with the Job Description.
4. Calculates a similarity score using TF-IDF and Cosine Similarity.
5. Ranks candidates according to their matching scores.
6. Displays the results through a web interface.

---

## ✨ Features

* 📄 **Resume Upload & Processing:** Easily upload candidate resumes.
* 📝 **Job Description Input:** Provide custom job descriptions to match against.
* 🤖 **AI/NLP-Based Matching:** Uses text vectorization and matrix math for precise scoring.
* 📊 **Candidate Ranking:** Instant sorting from highest to lowest relevance.
* 🔍 **Skill & Keyword Matching:** Evaluates overlapping skill sets.
* 💾 **Database Integration:** SQLite backend to track and manage uploads.
* 🌐 **Flask Web Interface:** Clean and intuitive UI built on Python Flask.

---

## 🛠️ Technologies Used

| Category | Tools / Technologies |
| :--- | :--- |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Backend** | Python, Flask |
| **AI / Machine Learning** | NLP, TF-IDF Vectorization, Cosine Similarity |
| **Database** | SQLite |
| **Parsing & Utilities** | PyPDF2, Git, GitHub |

---
## 🏗️ System WorkfloW
*
                 ┌──────────────────────┐
                 │     Job Description  │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Text Preprocessing │
                 └──────────┬───────────┘
                            │
                            │
┌─────────────────┐         ▼
│ Candidate Resume│ ──► Resume Text Extraction
└─────────────────┘         │
                            ▼
                 ┌──────────────────────┐
                 │   NLP Processing     │
                 │      TF-IDF          │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Cosine Similarity    │
                 │    Calculation       │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Candidate Match Score│
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Candidate Ranking    │
                 └──────────────────────┘
---

## 🧠 How the AI Works

RankHire-AI converts both the Job Description and candidate resumes into numerical feature vectors using **TF-IDF** (Term Frequency-Inverse Document Frequency).

1. **Text Extraction:** Extracts raw text from uploaded files (PDF/Text).
2. **Text Preprocessing:** Cleans text by converting to lowercase, removing punctuation, handling stop words, and tokenizing.
3. **TF-IDF Vectorization:** Evaluates word significance relative to the document set.
4. **Cosine Similarity:** Computes the angular similarity distance between the Job Description vector and each candidate vector.
5. **Candidate Ranking:** Formulates a sorted response based on matching scores.

| Rank | Candidate | Match Score |
| :---: | :--- | :---: |
| 🥇 **1** | Candidate A | **87%** |
| 🥈 **2** | Candidate B | **76%** |
| 🥉 **3** | Candidate C | **64%** |

---

## 📂 Project Structure

RankHire-AI/
│
├── app.py
├── requirements.txt
├── resume_screening.db
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   └── js/
│
├── uploads/
│
├── PROJECT_DETAILS.md
├── RUN_GUIDE.txt
├── Project_Report.docx
├── Project_Presentation.pptx
└── README.md
