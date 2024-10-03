import json
from pathlib import Path

data_dir = Path.cwd() / 'data'  # Directory where your JSON file is located
input_file_path = data_dir / 'sample_2.json'

with open(input_file_path, 'r', encoding='utf8') as file:
    data = json.load(file)

contact_info = data["patient"]["contactInfo"]

output_file_path = data_dir / 'contact.json'
with open(output_file_path, 'w', encoding='utf8') as file:

    json.dump(contact_info, file, indent=4)

print(f"Transferring Contact information written to  {output_file_path}")