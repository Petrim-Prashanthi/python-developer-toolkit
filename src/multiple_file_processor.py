from src.file_detector import detect_file_type
from src.file_extractor import (extract_txt,extract_csv,extract_json,extract_pdf)
from src.content_cleaner import (clean_json,clean_csv,clean_pdf,clean_txt)
from src.statistics_generator import generate_statistics
from src.output_generator import generate_output
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import json
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def process_multiple_files(file_paths):
    results = []
    with ThreadPoolExecutor(max_workers=3) as executor:
            
        results = list(executor.map(process_single_file,file_paths))
        return results

    for file_path in file_paths:
        file_type = detect_file_type(file_path)

        if file_type == "TXT":
            content = extract_txt(file_path)
            cleaned_content = clean_txt(content)
            statistics = generate_statistics(cleaned_content,file_type)
            output = generate_output(Path(file_path).name,file_type,statistics,cleaned_content)

        elif file_type == "CSV":
            content = extract_csv(file_path)
            cleaned_content = clean_csv(content)
            statistics = generate_statistics(cleaned_content,file_type)
            output = generate_output(Path(file_path).name,file_type,statistics,cleaned_content)

        elif file_type == "JSON":
            content = extract_json(file_path)
            cleaned_content = clean_json(content)
            statistics = generate_statistics(cleaned_content,file_type)
            output = generate_output(Path(file_path).name,file_type,statistics,cleaned_content)

        elif file_type == "PDF":
            content = extract_pdf(file_path)
            cleaned_content = clean_pdf(content)
            statistics = generate_statistics(cleaned_content,file_type)
            output = generate_output(Path(file_path).name,file_type,statistics,cleaned_content)

        results.append(output)

    return results

def process_single_file(file_path):
    try:
        file_type = detect_file_type(file_path)

        logging.info(f"Processing started: {file_path}")
        
        if file_type == "TXT":
            content = extract_txt(file_path)
            cleaned_content = clean_txt(content)
            statistics = generate_statistics(cleaned_content,file_type)
            output = generate_output(Path(file_path).name,file_type,statistics,cleaned_content)
        
        elif file_type == "CSV":
            content = extract_csv(file_path)
            cleaned_content = clean_csv(content)
            statistics = generate_statistics(cleaned_content,file_type)
            output = generate_output(Path(file_path).name,file_type,statistics,cleaned_content)
        
        elif file_type == "JSON":
            content = extract_json(file_path)
            cleaned_content = clean_json(content)
            statistics = generate_statistics(cleaned_content,file_type)
            output = generate_output(Path(file_path).name,file_type,statistics,cleaned_content)
        
        elif file_type == "PDF":
            content = extract_pdf(file_path)
            cleaned_content = clean_pdf(content)
            statistics = generate_statistics(cleaned_content,file_type)
            output = generate_output(Path(file_path).name,file_type,statistics,cleaned_content)

        logging.info(f"Processing completed: {file_path}")
        return output

    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return f"File not found : {file_path}"

    except json.JSONDecodeError:
        logging.error(f"Invalid JSON file: {file_path}")
        return f"Invalid JSON file : {file_path}"
    
    except ValueError as e:
        logging.error(f"Processing error: {e}")
        return f"Error : {e}"

    except Exception as e :
        logging.exception(f"Unexpected error while processing: {file_path}")
        return f"Error processing {file_path} : {e}"
            
