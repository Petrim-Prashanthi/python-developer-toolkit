import unittest
import json
from src.multiple_file_processor import process_single_file, process_multiple_files

class TestMultipleFileProcessor(unittest.TestCase):
    def test_process_single_file(self):
        result = process_single_file("sample_data/sample.txt")
        parsed_result = json.loads(result)

        self.assertEqual(parsed_result["file_name"], "sample.txt")
        self.assertEqual(parsed_result["file_type"], "TXT")
        self.assertIn("content", parsed_result)

    def test_process_multiple_files(self):
        file_paths = [
            "sample_data/sample.txt",
            "sample_data/sample.csv",
            "sample_data/sample.json"
        ]

        results = process_multiple_files(file_paths)

        self.assertEqual(len(results), 3)

        for result in results:
            parsed_result = json.loads(result)
            self.assertIn("file_name", parsed_result)

    def test_missing_file(self):
        result = process_single_file("sample_data/missing.txt")

        self.assertEqual(
            result,
            "File not found : sample_data/missing.txt"
        )