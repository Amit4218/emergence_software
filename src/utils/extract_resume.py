from pathlib import Path

from pypdf import PdfReader


def extract_resume_text() -> str:
    """extracts the text from resume"""

    resume_text = ""

    resume_pdf = Path("resume/resume-amit-bhagat.pdf")
    reader = PdfReader(resume_pdf)
    for p in range(len(reader.pages)):
        page = reader.pages[p]
        resume_text += page.extract_text()
    return resume_text
