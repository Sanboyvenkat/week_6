import json
import pprint
from pathlib import Path

data_dir = Path.cwd() / 'data'

# Specify the path to your JSON file
file_path = data_dir / 'sample_1.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)  # Load JSON data as a Python dictionary


# Access and store specific values from the JSON data
firstName = data ['firstName']
age = data['age']
address = data['address']
courses = data['courses']

# Print the extracted values
print(f"First name: {firstName}")
print(f"age: {age}")# Print the 'age' value
for key, value in address.items():
    print(f"{key}:{value}")

for course in courses:
    print(f"course:{course}")