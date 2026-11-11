import unittest
from src.file_extractor import extract_txt, extract_csv, extract_json

class TestFileExtractor(unittest.TestCase):
    def test_extract_txt(self):
        content = extract_txt("sample_data/sample.txt")

        self.assertIsInstance(content, str)
        self.assertIn("Python Developer Toolkit", content)

    def test_extract_csv(self):
        content = extract_csv("sample_data/sample.csv")

        self.assertIsInstance(content, list)
        self.assertEqual(len(content), 4)
        self.assertEqual(content[0], ["name", "age", "city"])

    def test_extract_json(self):
        content = extract_json("sample_data/sample.json")

        self.assertIsInstance(content, dict)
        self.assertEqual(content["name"], "Alice")
        self.assertEqual(content["age"], 22)