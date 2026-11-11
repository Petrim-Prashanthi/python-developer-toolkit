import unittest
from src.content_cleaner import clean_txt, clean_csv, clean_json

class TestContentCleaner(unittest.TestCase):
    def test_clean_txt(self):
        content = "   Hello Python   \n"
        result = clean_txt(content)

        self.assertEqual(result, "Hello Python")

    def test_clean_csv(self):
        content = [
            [" name ", " age "],
            [" Alice ", " 22 "]
        ]

        result = clean_csv(content)

        self.assertEqual(result, [
            ["name", "age"],
            ["Alice", "22"]
        ])

    def test_clean_json(self):
        content = {
            "name": " Alice ",
            "skills": [" Python ", " SQL "]
        }

        result = clean_json(content)

        self.assertEqual(result, {
            "name": "Alice",
            "skills": ["Python", "SQL"]
        })