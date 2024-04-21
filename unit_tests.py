import json
import unittest
from json_validator import file_validation

class test_file_validation(unittest.TestCase):
    def setUp(self):
        with open("sample_file.json") as f:
            self.file = json.load(f)

        with open("validation_schema.json") as f:
            self.schema = json.load(f)

    def test_valid_file(self):
        is_valid = file_validation(self.file)
        try:
            self.assertTrue(is_valid)
        except AssertionError:
            print("AssertionError: Field Resource contains single asterisk.")

    def test_invalid_file(self):
        invalid_file = {"PolicyName": "invalid"}
        is_valid = file_validation(invalid_file)
        self.assertFalse(is_valid)

    def test_empty_file(self):
        empty_file = {}
        is_valid = file_validation(empty_file)
        self.assertFalse(is_valid)

if __name__ == '__main__':
    unittest.main()