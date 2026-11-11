from pathlib import Path

def detect_file_type(file_path):
    file = Path(file_path)
    extension = file.suffix.lower()
    if extension == '.pdf':
        return "PDF"
    elif extension == '.csv':
        return "CSV"
    elif extension == '.json':
        return "JSON"
    elif extension == '.txt':
        return "TXT"
    else:
        raise ValueError("Invalid type")
