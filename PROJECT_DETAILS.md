# Smart Resume Screening and Candidate Ranking Tool

## 1. Project Title
Smart Resume Screening and Candidate Ranking Tool

## 2. Domain
Artificial Intelligence / Machine Learning / Natural Language Processing / Web Development

## 3. Abstract
The Smart Resume Screening and Candidate Ranking Tool is an AI-assisted recruitment application designed to reduce the time required to manually review resumes. The system accepts a job description and a candidate resume in PDF or TXT format. It extracts the resume text, identifies relevant technical and soft skills, and compares the resume with the job description using TF-IDF vectorization and cosine similarity. A match percentage is generated and the candidate is classified as Highly Recommended, Recommended, Needs Review, or Low Match. The application also identifies matched and missing skills and stores screened candidates in a local SQLite database for ranking.

## 4. Problem Statement
Manual resume screening is time-consuming, repetitive and difficult to standardize when many candidates apply for one job. Recruiters need a simple system that can quickly compare resumes against job requirements and prioritize candidates.

## 5. Objectives
1. Automate the initial stage of resume screening.
2. Extract useful information from resumes.
3. Compare resume content with a job description.
4. Generate an understandable match score.
5. Identify matched and missing skills.
6. Rank candidates according to their match score.
7. Provide a simple web interface for recruiters.

## 6. Existing System
In a traditional process, recruiters manually open resumes, read them, compare skills and make a shortlist. This can take significant time and can lead to inconsistent screening.

## 7. Proposed System
The proposed system uses NLP and machine learning techniques to automate the first-level screening process. It processes both resume and job-description text, converts the text into TF-IDF vectors, calculates cosine similarity and presents a score. Skill extraction provides additional explainability.

## 8. Technology Stack
- Frontend: HTML5, CSS3
- Backend: Python, Flask
- Machine Learning: Scikit-learn
- NLP: TF-IDF, cosine similarity, regular-expression based skill extraction
- PDF Processing: PyPDF2
- Database: SQLite
- Development Environment: VS Code / PyCharm
- Operating System: Windows, macOS or Linux

## 9. Hardware Requirements
- Dual-core processor or better
- 4 GB RAM minimum
- 1 GB free storage
- Internet is not required after dependencies are installed

## 10. Software Requirements
- Python 3.10 or newer
- pip
- Web browser
- VS Code or another Python IDE

## 11. Functional Modules
### Module 1: Resume Upload
Accepts PDF/TXT files and securely saves them.

### Module 2: Resume Text Extraction
Reads text from uploaded PDF/TXT files.

### Module 3: Job Description Processing
Accepts the recruiter’s job description.

### Module 4: Skill Extraction
Searches the processed text for a predefined skill vocabulary.

### Module 5: Similarity Analysis
TF-IDF represents the resume and job description as vectors. Cosine similarity calculates how close the vectors are.

### Module 6: Candidate Recommendation
The score is converted into a simple recommendation:
- 75–100: Highly Recommended
- 55–74.99: Recommended
- 35–54.99: Needs Review
- Below 35: Low Match

### Module 7: Candidate Ranking
Results are stored in SQLite and displayed in descending score order.

## 12. System Workflow
1. Recruiter opens the web application.
2. Recruiter enters a job description.
3. Recruiter uploads a resume.
4. System extracts resume text.
5. System detects skills in both texts.
6. System calculates TF-IDF vectors.
7. System calculates cosine similarity.
8. System generates a percentage score.
9. System identifies matched and missing skills.
10. System stores the result.
11. Recruiter can view the candidate ranking.

## 13. Algorithm
### TF-IDF
TF-IDF gives higher importance to words that are frequent in a document but less common across the comparison documents.

### Cosine Similarity
Cosine similarity measures the angle between two text vectors. A value closer to 1 means stronger similarity.

In simplified form:
similarity = (A · B) / (||A|| × ||B||)

The displayed score is:
match score = similarity × 100

## 14. Database
Table: candidates

Fields:
- id
- name
- email
- filename
- score
- recommendation
- matched_skills
- missing_skills
- created_at

## 15. Advantages
- Saves initial screening time
- Provides consistent scoring
- Highlights missing skills
- Easy to operate
- Low-cost technology stack
- Can be expanded into a major project

## 16. Limitations
- Skill extraction currently uses a predefined vocabulary.
- TF-IDF does not fully understand context or synonyms.
- Scanned image-only PDFs may require OCR.
- The score should support recruiter decisions rather than replace human judgment.

## 17. Future Scope
- Multiple job descriptions
- Multiple resume upload at once
- Semantic embeddings using sentence-transformers
- OCR for scanned resumes
- Login and role-based access
- MySQL/PostgreSQL deployment
- Recruiter analytics dashboard
- AI-generated candidate summaries
- Resume quality suggestions
- Export ranking to Excel/PDF
- Cloud deployment
- Bias and fairness monitoring

## 18. Testing
Test Case 1: Valid PDF + valid job description → result displayed.
Test Case 2: Missing resume → validation message.
Test Case 3: Missing job description → validation message.
Test Case 4: Unsupported file → validation message.
Test Case 5: Multiple candidates → ranking page sorts by score.

## 19. Conclusion
The Smart Resume Screening and Candidate Ranking Tool demonstrates how AI and NLP can be used in a practical recruitment workflow. The system automates first-level resume comparison, highlights relevant skills and provides a ranking mechanism. Its modular design makes it suitable for further development into a larger recruitment platform.

## 20. Viva Questions
1. Why did you choose this project?
2. What is NLP?
3. What is TF-IDF?
4. Why is cosine similarity used?
5. What is machine learning in this project?
6. How is the match percentage calculated?
7. What is the role of Flask?
8. Why did you use SQLite?
9. What are the limitations of TF-IDF?
10. How can the project be improved using embeddings?
11. What happens if a PDF contains only scanned images?
12. How would you deploy this application?
