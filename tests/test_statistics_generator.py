import unittest
from src.statistics_generator import generate_statistics


class TestStatisticsGenerator(unittest.TestCase):
    def test_txt_statistics(self):
        content = "Hello Python\nWelcome"
        result = generate_statistics(content, "TXT")

        self.assertEqual(result["character_count"], 20)
        self.assertEqual(result["word_count"], 3)
        self.assertEqual(result["line_count"], 2)

    def test_csv_statistics(self):
        content = [
            ["name", "age", "city"],
            ["Alice", "22", "Hyderabad"],
            ["Bob", "24", "Chennai"]
        ]

        result = generate_statistics(content, "CSV")

        self.assertEqual(result["row_count"], 2)
        self.assertEqual(result["column_count"], 3)

    def test_json_statistics(self):
        content = {
            "name": "Alice",
            "age": 22,
            "city": "Hyderabad"
        }

        result = generate_statistics(content, "JSON")

        self.assertEqual(result["key_count"], 3)