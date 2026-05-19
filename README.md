
# Resume Screening & Candidate Evaluation System

Automated candidate evaluation and reporting system built using Python, SQL, and CSV-based profile processing.

## Features
- Resume dataset processing using CSV and SQL
- Candidate profile validation and filtering
- Keyword extraction and classification logic
- Automated evaluation scoring
- Report generation for shortlisted candidates

## Tech Stack
- Python
- SQLite
- Pandas
- CSV Processing

## Project Structure

```
resume_screening_project/
│
├── app.py
├── requirements.txt
├── candidates.csv
├── database.db
├── reports/
│   └── shortlisted_candidates.csv
└── README.md
```

## How to Run

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the project
```bash
python app.py
```

## Functionalities
- Reads candidate data from CSV
- Stores candidate information in SQLite
- Filters profiles based on skills and experience
- Generates shortlisted candidate reports
- Applies keyword-based evaluation logic

## Sample Evaluation Criteria
- Python
- SQL
- Java
- REST APIs
- Machine Learning
- Communication Skills

## Output
Shortlisted candidate reports are generated inside the `reports/` folder.
