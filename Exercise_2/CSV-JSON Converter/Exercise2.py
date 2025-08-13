import csv
import json
import sys

# Function to convert CSV file to JSON file
def csv_to_json(csv_file_path, json_file_path):
    data = []

    # Open the CSV file for reading
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)  # Read rows as dictionaries

        # Append each row (as a dict) to the data list
        for row in reader:
            data.append(row)

    # Write the list of dictionaries to a JSON file
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)  # Pretty-print with indent

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python Exercise2.py <input_csv> <output_json>")
        sys.exit(1) 

    # Get input and output file paths from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Call the conversion function
    csv_to_json(input_file, output_file)