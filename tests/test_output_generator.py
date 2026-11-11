import unittest
import json
from src.output_generator import generate_output


class TestOutputGenerator(unittest.TestCase):
    def test_generate_output(self):
        statistics = {
            "character_count": 20,
            "word_count": 3,
            "line_count": 2
        }

        content = "Hello Python\nWelcome"

        result = generate_output(
            "sample.txt",
            "TXT",
            statistics,
            content
        )

        parsed_result = json.loads(result)

        self.assertEqual(parsed_result["file_name"], "sample.txt")
        self.assertEqual(parsed_result["file_type"], "TXT")
        self.assertEqual(parsed_result["statistics"], statistics)
        self.assertEqual(parsed_result["content"], content)