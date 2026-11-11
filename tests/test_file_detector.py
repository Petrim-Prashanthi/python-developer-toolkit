import unittest
from src.file_detector import detect_file_type


class TestFileDetector(unittest.TestCase):

    def test_pdf(self):
        self.assertEqual(detect_file_type("report.pdf"), "PDF")

    def test_csv(self):
        self.assertEqual(detect_file_type("data.csv"), "CSV")

    def test_json(self):
        self.assertEqual(detect_file_type("config.json"), "JSON")

    def test_txt(self):
        self.assertEqual(detect_file_type("notes.txt"), "TXT")

    def test_uppercase_extension(self):
        self.assertEqual(detect_file_type("REPORT.PDF"), "PDF")

    def test_unsupported_extension(self):
        with self.assertRaises(ValueError):
            detect_file_type("image.png")


if __name__ == "__main__":
    unittest.main()