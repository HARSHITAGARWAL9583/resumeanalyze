from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_score(resume_text, jd_text):
    if not resume_text or not jd_text:
        return 0.0, "Resume or JD not parsable"

    embeddings = model.encode([resume_text, jd_text])
    score = util.cos_sim(embeddings[0], embeddings[1]).item()

    # Map cosine similarity to 1–10 scale
    rating = int(min(max(round(score * 10), 1), 10))

    # Reasoning: based on keyword overlap (simple version)
    keywords = ['machine learning', 'python', 'nlp', 'llm', 'api', 'deployment']
    matched = [kw for kw in keywords if kw.lower() in resume_text.lower()]
    reason = "Matched skills: " + ", ".join(matched) if matched else "Basic match found"

    return rating, reason