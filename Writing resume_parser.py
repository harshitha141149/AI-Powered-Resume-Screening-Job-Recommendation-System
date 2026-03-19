%%writefile resume_parser.py
import pdfplumber

def extract_text_from_resume(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text
