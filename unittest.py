import unittest
import jsonex

class TestValidateJSON(unittest.TestCase):
    def test_valid_json(self):

        with open('valid_input.json', 'w') as file:
            file.write('{"Resource": "arn:aws:s3:::example_bucket"}')

        result = jsonex('valid_input.json')
        self.assertTrue(result)
        
    def test_invalid_json(self):

        with open('invalid_input.json', 'w') as file:
            file.write('{"Resource": "*"}')

        result = jsonex('invalid_input.json')
        self.assertFalse(result)

    def test_file_not_found(self):

        result = jsonex('non_existent_file.json')
        self.assertFalse(result)

    def test_invalid_json_format(self):

        with open('invalid_json_format.json', 'w') as file:
            file.write('{"Resource":')

        result = jsonex('invalid_json_format.json')
        self.assertFalse(result)

    def test_missing_resource_field(self):

        with open('missing_resource_field.json', 'w') as file:
            file.write('{"NotResource": "some_value"}')

        result = jsonex('missing_resource_field.json')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()