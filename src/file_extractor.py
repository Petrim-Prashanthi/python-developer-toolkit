from pathlib import Path
import csv
import json
from pypdf import PdfReader
def extract_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

def extract_csv(file_path):
    with open(file_path, "r",encoding="utf-8",newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)
        return rows

def extract_json(file_path):
    with open(file_path,"r",encoding='utf-8') as file:
        document = json.load(file)
        return document

def extract_pdf(file_path):
    reader = PdfReader(file_path)
    content = []
    for page in reader.pages:
        text = page.extract_text()
        content.append(text)
    return "\n".join(content)
