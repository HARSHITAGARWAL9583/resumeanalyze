import pdfplumber
import requests
import tempfile
import os

def extract_text_from_pdf(url):
    try:
        response = requests.get(url, stream=True, timeout=15)
        response.raise_for_status()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
            f.write(response.content)
            path = f.name

        with pdfplumber.open(path) as pdf:
            text = "\n".join([page.extract_text() or '' for page in pdf.pages])

        os.remove(path)
        return text.strip()

    except Exception as e:
        print(f"Error parsing PDF: {e}")
        return None