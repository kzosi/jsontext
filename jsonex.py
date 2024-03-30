import json

def validate_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

    #edge cases:
    except FileNotFoundError:
        print("File not found.")
        return False
    except json.JSONDecodeError:
        print("Invalid JSON format.")
        return False
    #
    
    if 'Resource' in data:
        if data['Resource'] == '*':
            return False
        else:
            return True
    else:
        print("Input JSON does not contain Resource field.")
        return False
    
file_path = 'input.json'  # Provide the path to your JSON file
result = validate_json(file_path)
print("Input JSON is valid:", result)


