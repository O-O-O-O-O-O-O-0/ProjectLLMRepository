import json

def create_input_output_pairs(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    input_output_pairs = []
    for i in range(len(lines) - 1):
        input_text = lines[i].strip()
        output_text = lines[i + 1].strip()
        input_output_pairs.append((input_text, output_text))

    return input_output_pairs

# Replace 'your_text_file.txt' with the actual path to your text file
file_path = 'Output.txt'
pairs = create_input_output_pairs(file_path)

json_file_path = 'InputOutputPairsTest.json'

# Print the generated input-output pairs
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(pairs, json_file, ensure_ascii=False, indent=2)