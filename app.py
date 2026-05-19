
import pandas as pd
import sqlite3
from pathlib import Path

REQUIRED_SKILLS = ["Python", "SQL"]

reports_path = Path("reports")
reports_path.mkdir(exist_ok=True)

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    skills TEXT,
    experience INTEGER
)
''')

df = pd.read_csv("candidates.csv")

df.to_sql("candidates", conn, if_exists="replace", index=False)

def calculate_score(skills):
    score = 0
    for skill in REQUIRED_SKILLS:
        if skill.lower() in skills.lower():
            score += 1
    return score

df["score"] = df["skills"].apply(calculate_score)

shortlisted = df[df["score"] >= 2]

shortlisted.to_csv("reports/shortlisted_candidates.csv", index=False)

print("\nShortlisted Candidates:\n")
print(shortlisted[["name", "email", "skills", "score"]])

conn.close()
