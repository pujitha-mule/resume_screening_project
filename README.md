# Resume Screening & Candidate Evaluation System

Automated candidate evaluation and reporting system built using Python, SQL, and CSV-based profile processing. The system processes candidate datasets, applies keyword-based profile classification, filters applicants based on required skills, and generates shortlisted candidate reports.

---

## Features

- Candidate profile screening using CSV datasets
- SQL database integration using SQLite
- Keyword extraction and profile classification
- Automated candidate filtering and evaluation
- Report generation for shortlisted profiles
- Structured backend workflow for recruitment automation

---

## Tech Stack

- Python
- SQL (SQLite)
- Pandas
- CSV Processing

---

## Project Structure

```bash
resume_screening_project/
│
├── app.py
├── candidates.csv
├── database.db
├── requirements.txt
├── reports/
│   └── shortlisted_candidates.csv
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/pujitha-mule/resume_screening_project.git
```

Navigate to the project folder:

```bash
cd resume_screening_project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python app.py
```

---

## Functional Workflow

1. Reads candidate data from CSV files
2. Stores records in SQLite database
3. Applies skill-based evaluation logic
4. Filters candidates based on required criteria
5. Generates shortlisted candidate reports

---

## Sample Evaluation Criteria

- Python
- SQL
- Java
- Machine Learning
- REST APIs
- Communication Skills

---

## Sample Output

```bash
Shortlisted Candidates:

     name               email                          skills  score
0   Rahul    rahul@gmail.com             Python SQL Java      3
1   Sneha    sneha@gmail.com      Java SpringBoot SQL      2
```

---

## Future Improvements

- Resume PDF parsing
- Weighted candidate scoring system
- Flask API integration
- Dashboard for recruiter analytics
- AI-based profile ranking

---

## Author

PUJITHA MULE

GitHub: https://github.com/pujitha-mule  
LinkedIn: https://linkedin.com/in/pujitha-mule
