import pandas as pd
from resume_parser import extract_text_from_pdf
from job_matcher import get_score

def run_agent(csv_path, jd_path, output_path="output.csv"):
    df = pd.read_csv(csv_path)
    with open(jd_path, "r", encoding="utf-8") as f:
        jd_text = f.read()

    ratings, reasons = [], []

    for _, row in df.iterrows():
        resume_text = extract_text_from_pdf(row['resume_link'])
        rating, reason = get_score(resume_text, jd_text)
        ratings.append(rating)
        reasons.append(reason)

    df['rating'] = ratings
    df['reason'] = reasons
    df.to_csv(output_path, index=False)
    print(f"✅ Done! Saved at {output_path}")

# Example usage:
# run_agent("data/sample_resumes.csv", "data/sample_job_description.txt")