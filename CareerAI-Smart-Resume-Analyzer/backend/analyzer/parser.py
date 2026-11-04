from pathlib import Path
import fitz
from docx import Document
def extract_text(uploaded_file):
    ext=Path(uploaded_file.name).suffix.lower()
    uploaded_file.seek(0)
    if ext==".pdf":
        data=uploaded_file.read()
        with fitz.open(stream=data,filetype="pdf") as doc:
            text="\n".join(page.get_text() for page in doc)
    elif ext==".docx":
        doc=Document(uploaded_file)
        text="\n".join(p.text for p in doc.paragraphs)
        for table in doc.tables:
            for row in table.rows: text += "\n" + " ".join(cell.text for cell in row.cells)
    else: raise ValueError("Only PDF and DOCX files are supported.")
    if not text.strip(): raise ValueError("No readable text found. The file may be scanned; use a text-based PDF.")
    return text[:100000]
