# jsontext
# AWS IAM Role JSON Validator

This Python script validates input JSON data against the AWS IAM Role Policy definition. It checks if the input JSON data contains a valid "Resource" field based on specific criteria.

## How to Run

Follow the instructions below to run the script:

### Prerequisites

- Python 3.x installed on your system.
- Clone or download this repository to your local machine.

### Running the Script

1. Open a terminal or command prompt.
2. Navigate to the directory where you have cloned or downloaded this repository.
3. Run the script using the following command:

```bash
python your_script.py input.json

Replace your_script.py with the name of your Python script file containing the validate_json method, and input.json with the path to your input JSON file.

If the input JSON file is valid according to the criteria mentioned in the script, it will output Input JSON is valid: True. Otherwise, it will output Input JSON is valid: False.

### Running Unit Tests
  1. Open a terminal or command prompt.
  2. Navigate  to the directory where you have cloned or downloaded this repository.
  3. Run the following command to execute the unit tests:

```python -m unittest test_your_script.py

Replace test_your_script.py with the name of the file containing your unit tests.

The unit tests will validate various scenarios and edge cases of the validate_json method and provide feedback on their outcomes.

